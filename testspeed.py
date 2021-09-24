import speedtest
import math
from datetime import datetime
import time

SLEEP_TIMEOUT = 600 # 10 minutes in seconds, (60 seconds per minute) * 10

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
   

adapter = speedtest.Speedtest()

while True:
    download_figure = adapter.download()
    decorated_figure = convert_size(download_figure)
    print("Download Speed is ", decorated_figure)
    with open("results.txt", "a") as results_file:
        results_file.write(str(datetime.now()) + " " + decorated_figure + "/s")
        results_file.write("\n")
    time.sleep(SLEEP_TIMEOUT)