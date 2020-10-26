"""
Use this file if you want to download the raw file from the given url.
"""

import gzip
import json
import base64
import urllib.request, urllib.response, urllib.error, urllib.parse

dataset = "GSE2018"  # case-sensitive, must match dataset name that is being requested!
dataset_file_name = "GSE2018_new_url"  # chosen name for file that will be downloaded
file_name = "{}.tab".format(dataset_file_name)
url = "https://gemma.msl.ubc.ca/rest/v2/datasets/GSE2018/design".format(dataset)  # request URL
r = urllib.request.urlopen(url)

with open(file_name, 'wb') as file:
    file.write(r.read())  # writes file from URL request
