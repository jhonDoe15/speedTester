from json.decoder import JSONDecodeError
import math
from datetime import datetime
import time
import json
import subprocess

SLEEP_TIMEOUT = 600 # 10 minutes in seconds, (60 seconds per minute) * 10

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("b", "Kb", "Mb", "Gb", "Tb", "Pb", "Eb", "Zb", "Yb")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
   

while True:
    try:
        speedtest_output = subprocess.run(
                ["speedtest", "-f", "json"], capture_output=True)
        json_output = json.loads(speedtest_output.stdout)
        speed_in_bits = json_output['download']['bandwidth'] * 8
        bits_per_second = convert_size(speed_in_bits)
        print("Download Speed is ", bits_per_second, "/s")
        with open("results.txt", "a") as results_file:
            results_file.write(str(datetime.now()) + " " + bits_per_second + "/s")
            results_file.write("\n")
        time.sleep(SLEEP_TIMEOUT)
    except Exception as e:
        print(e)