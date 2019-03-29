import calendar
import datetime
import os
import requests
import sys

from time import time as timer
from multiprocessing.pool import ThreadPool

POOL_SIZE = 4

start = timer()

year, month = map(int, sys.argv[1].split("-"))


def download_file(url):
    def path(url):
        return "data/" + url.rsplit("/")[-1]

    filename = path(url)
    if not os.path.exists(filename):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filename, "wb") as f:
                for chunk in r:
                    f.write(chunk)
        return filename


def urls(year, month):
    def days(year, month):
        nb_days = calendar.monthrange(year, month)[1]
        return [datetime.date(year, month, day) for day in range(1, nb_days + 1)]

    urls = []
    dates = days(year, month)
    for date in dates:
        for hour in range(0, 24):
            url = "http://data.gharchive.org/{}-{}.json.gz"
            urls.append(url.format(date.strftime("%Y-%m-%d"), hour))

    return urls


results = ThreadPool(POOL_SIZE).imap_unordered(download_file, urls(year, month))
for path in results:
    print(path)

print(f"Elapsed Time: {timer() - start}")
