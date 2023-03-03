# Copyright (c) 2023 Kyle Lopin <kylel@nu.ac.th>

""" 

"""

__author__ = "Kyle Vitautas Lopin"

# standard libraries
from datetime import datetime as dt
import json
import time

# installed libraries
import paho.mqtt.client as mqtt
from gpiozero import CPUTemperature

# local files
from config import *

client = mqtt.Client()
client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
client.loop_start()

while True:
    temperature = CPUTemperature()
    payload = {"datetime": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
               "device": "device Kyle",
               "temperature": temperature}
    client.publish(PUBLISH_DATA_TOPIC, json.dumps(payload))
    # sleep for 15 seconds
    time.sleep(15)
