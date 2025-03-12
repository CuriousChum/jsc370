'''
Created on July 21, 2022
@author: Ruslan Kain (r.kain@queensu.ca)
'''

Documentation

This file describes Version 1.0 of the "Resource Usage of Applications Running on Raspberry Pi Devices" dataset, the data collection process, and the logged measurements.

The information included in this documentation is as follows:

- Dataset Description
- Data Collection Devices
- Data Collection Software
- Data Size and Format
- Collected Recordings
- File Structure
- Dataset Download
- References
- License

Dataset Description

The collection and construction of this dataset was organized by the Queen's Telecommunications Research Lab (TRL) and lead by Ruslan Kain, a Ph.D. student at TRL. The dataset includes dynamic resource usage information associated with running edge-native applications on a set of 4 heterogeneous Raspberry Pi 4 Devices.

Data Collection Devices

Four Raspberry Pi 4 devices, with 2, 4, and 8 GB RAM sizes, and CPU frequency of 1200, 1500, and 1800 MHz were used. This is to establish heterogeneity of the devices used and collected data and to enable data-based applications for Edge Computing Research.

Data Collection Software

A python package called PsUtil [1] was used for obtaining the resource usage measurements with a five-second granularity.


Data Size and Format

We managed to collect more than 550 thousand unique data points representing the 768 hours of running applications on Raspberry Pi Devices. Our dataset is publicly available on Borealis platform in an effort to help other researchers in the field conduct edge computing resource usage analysis. The size of the dataset is around 444 MB, and it consists of 74 comma-separated values (CSV) file. The file name is formatted as "Raspberry-Pi-Specifications_Data-Title_Application-Sequence-Type_recording-Period.csv". An example is "RPi4B8GB_1800MHz_res_usage_data_rvp_random_48hr.csv", which implies that the data was collected using a Raspberry Pi with 8 GB of RAM and 1800 MHz CPU frequency for a random sequence of applications for 48 hours.

Collected Recordings

The collected recordings include the user, system, and idle CPU time, memory percent usage, network upload and download size and rates, disk IO, device temperature, WiFi frequency, bit rate, link quality, maximum link quality, and signal level.  The resource usage information is associated with the resource usage states in the datasets using the labels "game", "stream", "augmented reality", "mining", and "idle".

Additional pre-process dataset is generated, indicated in the csv file names with words "train" and "test". The original datasets are split 70% for training and 30% for testing. New features were engineered which are the difference of consequent samples for user, system, and idle CPU times and network upload and download byte sizes. In the testing dataset the prediction ("predicted states") and model confidence ("log likelihood") results are stored for all tested step sizes, namely, 1, 2, 5, 10, 15, 30, and 60 step, in addition to multi-step labels, all are stored in the form of lists.


The following list provides the names of the logged parameters and their description:

• time_stamp: precise time when the measurement is taken.
• time: time as a floating-point number expressed in seconds since the epoch (UTC)
• cpu_freq: system-wide CPU cycle frequency (MHz)
• cpu: system-wide CPU utilization as a percentage (%)
• cpu_user_time: time spent by normal processes executing in user mode, including guest time (seconds)
• cpu_idle_time: time spent doing nothing (seconds)
• cpu_system_time: time spent by processes executing in kernel mode (seconds)
• memory: memory currently in use or very recently used, and so it is in RAM (%)
• net_sent: number of overall bytes sent 
• net_recv: number of overall bytes received
• net_upload_rate: number of bytes sent in last time interval / time interval (MBytes/s)
• net_download_rate:  number of bytes received in last time interval / time interval (MBytes/s)
• temp: temperature (Degree Celsius)
• wifi_freq: operating frequency or channel of Wifi in the device (GHz) 
• bit_rate:  speed at which bits are transmitted over the medium (bit/s)
• link_quality: overall quality of the link. May be based on the level of contention or interference, the bit or frame error rate, how good the received signal is, some timing synchronization, or other hardware metric.
• link_quality_max: maximum possible quality of the link
• gpu: GPU utilization as a percentage (%)
• gpu_memory: GPU memory currently in use or very recently used (%)
• (resource)_diff: resource (CPU times, memory usage, etc.) usage in the last interval (difference between current aggregate and previously measured aggregate values)
• net: label feature for type of network access technology used, WiFi or 4G LTE
• state: label feature for resource usage state of the device associated with running application
• label - (step size) step: numerical label given to represent resource usage state from current state and to the next (step size) labels
• predicted states - (step size) step: numerical label predicted by the prediction model (RUMP or HBPSHPO) to represent resource usage state from current state and to the next (step size) labels
• log_likelihood - (step size) step: the joint probability of the observed data as a function of the parameters of the chosen statistical model for the predictions made with (step size) steps ahead

Check PsUtil documentation in [1] for the full list of measurements that can be captured by python package and their descriptions.

File Structure

The following files are included in the current version of the dataset:

data/
+-- RPi4B2GB1/
    +-- RPi4B2GB1_600MHz_res_usage_data_12hr_screen_eth.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_rvp_pattern_48hr.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_rvp_pattern_48hr_2.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_rvp_pattern_48hr_3.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_rvp_pattern_48hr_4.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_rvp_random_48hr.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_rvp_random_48hr_2.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_test_pred_rvp_pattern_48hr.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_test_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_test_pred_rvp_pattern_48hr_3.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_test_pred_rvp_pattern_48hr_4.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_test_pred_rvp_random_48hr.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_test_pred_rvp_random_48hr_2.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_train_pred_rvp_pattern_48hr.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_train_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_train_pred_rvp_pattern_48hr_3.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_train_pred_rvp_pattern_48hr_4.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_train_pred_rvp_random_48hr.csv
    +-- RPi4B2GB1_1200MHz_res_usage_data_train_pred_rvp_random_48hr_2.csv
+-- RPi4B2GB2/
    +-- RPi4B2GB2_800MHz_res_usage_data_pattern_test_12h.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_rvp_pattern_48hr.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_rvp_pattern_48hr_2.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_rvp_random_48hr.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_rvp_random_48hr_2.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_test_pred_rvp_pattern_48hr.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_test_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_test_pred_rvp_random_48hr.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_test_pred_rvp_random_48hr_2.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_train_pred_rvp_pattern_48hr.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_train_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_train_pred_rvp_random_48hr.csv
    +-- RPi4B2GB2_1500MHz_res_usage_data_train_pred_rvp_random_48hr_2.csv
+-- RPi4B4GB/
    +-- RPi4B4GB_1200MHz_res_usage_data_12hr.csv
    +-- RPi4B4GB_1200MHz_res_usage_data_pattern_test_12h.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_rvp_pattern_48hr.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_rvp_pattern_48hr_2.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_rvp_pattern_48hr_3.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_rvp_random_48hr.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_rvp_random_48hr_2.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_test_pred_rvp_pattern_48hr.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_test_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_test_pred_rvp_pattern_48hr_3.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_test_pred_rvp_random_48hr.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_test_pred_rvp_random_48hr_2.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_train_pred_rvp_pattern_48hr.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_train_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_train_pred_rvp_pattern_48hr_3.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_train_pred_rvp_random_48hr.csv
    +-- RPi4B4GB_1500MHz_res_usage_data_train_pred_rvp_random_48hr_2.csv
+-- RPi4B8GB/
    +-- RPi4B8GB_1800MHz_res_usage_data.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_24hr.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_pattern_test.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_pattern_test_6h.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_pattern_test_18h.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_rvp_random_48hr.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_rvp_random_48hr_2.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_test_pred.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_test_pred_rvp_pattern_48hr.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_test_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_test_pred_rvp_random_48hr.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_test_pred_rvp_random_48hr_2.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_train_pred.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_train_pred_rvp_pattern_48hr.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_train_pred_rvp_pattern_48hr_2.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_train_pred_rvp_random_48hr.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_train_pred_rvp_random_48hr_2.csv
    +-- RPi4B8GB_1800MHz_res_usage_data_train_pred_y.csv   
    +-- RPi4B8GB_1800MHz_res_usage_data_x.csv   
    +-- RPi4B8GB_1800MHz_res_usage_data_y.csv   
    +-- RPi4B8GB_res_usage_data_pred.csv   
    +-- RPi4B8GB_res_usage_data_test.csv   
    +-- RPi4B8GB_res_usage_data_train.csv   
+-- LICENSE.txt
+-- README.txt

Dataset Download

To download the dataset from Borealis, it is recommended to select all files and download them at once in their original format. This ensures that the file structure described in the previous section is preserved.

References

[1] PsUtil documentation:
https://psutil.readthedocs.io/en/latest/

License

The "Resource Usage of Applications Running on Raspberry Pi Devices" dataset is Copyright © 2022 Queen's TRL. It is an open dataset, Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0), and may be redistributed under the terms specified in the LICENSE.txt file and at https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode.
