import requests
import zipfile
import http.client as hc

hc.HTTPConnection.debuglevel = 1

url = "https://borealisdata.ca/api/access/dataset/:persistentId"
rpi_id = "doi:10.5683/SP3/GOZAJE"
params = {
    "persistentId": rpi_id,
}

with requests.get(url, params=params, stream=True) as resp:
    if resp.status_code != 200:
        print("request fail")
    else:
        with open("foo.zip", "wb") as f:
            for chunk in resp.iter_content(16384):
                f.write(chunk)

assert zipfile.is_zipfile("foo.zip")

zipfile.ZipFile("foo.zip").extractall("foo")
