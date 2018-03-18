#!/usr/bin/python
from Tkinter import *
from phue import Bridge
import datetime
import time
import sys


b = Bridge("192.168.1.163") # Enter bridge IP here.
#b.connect()
light_names = b.get_light_objects('name')

#define lights -- by name
pepper = light_names["Pepper Light"]
herb = light_names["Herb Light"]

def on():
    if herb.on == True:
        return

    pepper.on = herb.on = True
    pepper.colortemp = 154
    herb.colortemp = 154
    pepper.brightness = 254
    herb.brightness = 254
    print("Turning on.")

def off():
    if herb.on == False:
        return
    pepper.on = herb.on = False
    print("Turning off.")

# loop for growlight service
# lights on at 06:00
# lights off at 21:00
# 15h grow cycle at 6500k light temp
def loop():
    while True:
        currentTime = datetime.datetime.now().time()
        if datetime.time(21,0) > currentTime >= datetime.time(6,0):
            #print("Turning lights on.")
            on()
        elif datetime.time(6,0) < currentTime >= datetime.time(21,0):
            #print("Turning lights off.")
            off()
        time.sleep(30) # check time every 30s, which is sufficient for our required accuracy

# parse input and loop or turn the grow lights on/off
if len(sys.argv) > 1:
    if sys.argv[1] == "loop":
        loop()
    elif sys.argv[1] == "on":
        on()
    elif sys.argv[1] == "off":
        off()
else:
    print("  ===============================================")
    print("  |                    USAGE                    |")
    print("  ===============================================")
    print("  |                                             |")
    print("  |            lights.py <command>              |")
    print("  |                 commands:                   |")
    print("  |                                             |")
    print("  |        on -- turn the grow lights on        |")
    print("  |       off -- turn the grow lights off       |")
    print("  |        loop -- start the service loop       |")
    print("  ===============================================")
