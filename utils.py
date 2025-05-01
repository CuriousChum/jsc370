import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
import gc
import re

import requests
import zipfile


def get_data_from_remote(url, params):
    __CHUNK_SIZE = 16384
    with requests.get(url, params=params, stream=True) as resp:
        if resp.status_code != 200:
            print("request fail")
        else:
            with open("data.zip", "wb") as f:
                for chunk in resp.iter_content(__CHUNK_SIZE):
                    f.write(chunk)
    
    assert zipfile.is_zipfile("data.zip")

    zipfile.ZipFile("data.zip").extractall("data")

DATA_DIR = Path("data")
def get_filenames(srcdir=DATA_DIR):
    return sorted([f for f in srcdir.rglob("*.tab") if "res_usage_data_rvp" in f.name])

GET_DEV_ALIAS = {
    "RPi4B2GB1_1200MHz": "dev0",
    "RPi4B2GB2_1500MHz": "dev1",
    "RPi4B4GB_1500MHz": "dev2",
    "RPi4B8GB_1800MHz": "dev3",
}
def get_pi_id(path):
    path = path.name.split("_")
    return GET_DEV_ALIAS[path[0] + "_" + path[1]]
    
    
def load_one(path, run_id, cols=None):
    df = (pl.read_csv(path, separator="\t")
            .with_columns([
                pl.col("time_stamp").str.to_datetime(),
                pl.lit(run_id).alias("run_id"),
                pl.lit(get_pi_id(path)).alias("pi_id")
             ])
         )
    if cols is None:
        return df
    df = df.select(cols + ["run_id", "pi_id"]).sort("time")
    return df

__DEFAULT_INSPECT_REG = re.compile(r"(cpu|temp|time|mem|sent|recv|state)")
def inspect(df, exclude_pattern=None, verbose=False):
    if exclude_pattern is None:
        exclude_pattern = __DEFAULT_INSPECT_REG
    if verbose:
        print(f"Inspecting dataframe with {len(df)} rows, {df.shape[1]} columns")
    for col in df.columns:
        if re.match(exclude_pattern, col):
            continue
        mask = df[col] > 1e-12
        if mask.sum() > 10: # arbitrary to find anything print(f"col: {col} ({mask.sum()} / {len(df)} ({mask.sum() / len(df):.2f}))")
            print(df[mask][col].head(3))
    if verbose:
        print("========= done =========")
        
__STATE_COLORS = {
    'augmented_reality': 'tab:blue',
    'game': 'tab:orange',
    'idle': 'tab:green',
    'mining': 'tab:red',
    'stream': 'tab:cyan',
}
def plot_facet(df, datacol, states=None):
    fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(12, 3))
    for i, state in enumerate(states):
        sns.histplot(df.filter(df["state"] == state)[datacol], bins=30, kde=True, ax=ax[i])
        ax[i].set_title(f'state: {state}')
    fig.suptitle(f"{datacol} distribution")
    plt.tight_layout()
    plt.show()

def plot_time_series(plotdf, colname, ax=None, show=True, retpatches=False):
    if ax is None:
        fig, ax = plt.subplots(figsize=(16, 3))
    data = plotdf[colname]
    ax.plot(plotdf["time"], data)

    legend_patches = []
    for state, color in __STATE_COLORS.items():
        ax.fill_between(plotdf["time"], data.min(), data.max(), where=(plotdf["state"] == state), color=color, alpha=0.5)
        legend_patches.append(plt.Rectangle((0,0), 1, 1, fc=color, alpha=0.3, label=state))
        
    ax.set_xbound(plotdf["time"][0], plotdf["time"][-1])
    if not retpatches:
        ax.legend(handles=legend_patches, loc='upper right', title="states")
    if show:
        plt.show()
    return legend_patches if retpatches else None

def plot_mult_time_series(df, colnames, ylabs=None, titles=None, suptitle=None):
    fig, axs = plt.subplots(nrows=len(colnames), figsize=(12, 3 * len(colnames)))
    if suptitle is not None:
        fig.suptitle(suptitle)
    ylabs = colnames if ylabs is None else ylabs
    for i, col in enumerate(colnames):
        ax_ = axs if len(colnames) == 1 else axs[i]
        patches = plot_time_series(df, col, ax=ax_, show=False, retpatches=True)
        ax_.set_xlabel('time (ticks)')
        ax_.set_ylabel(ylabs[i])
    fig.legend(handles=patches, loc='upper right', title="states")
    plt.tight_layout()
    return fig, axs