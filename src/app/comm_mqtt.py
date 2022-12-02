# Copyright (c) 2022 Kyle Lopin <kylel@nu.ac.th>

""" 
Communicate with the HIVEMQ broker to receive
sensor data, using the paho mqtt library
"""

__author__ = "Kyle Vitautas Lopin"

# standard libraries
import time

# installed library
import paho.mqtt.client as mqtt

HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC = "Naresuan/Kyle"
SUBSCRIBE_TOPIC = "Naresuan/+"


def on_subscription(*args):
    print("subscribed: ", args)


def on_connection(*args):
    """ Call back for when mqtt connects to the broker
     and prints out an acknowledgement and subscribes """
    print("Connected")
    client.subscribe(SUBSCRIBE_TOPIC)


def on_message(client, user_data, msg: mqtt.MQTTMessage):
    print("got message: ", msg.payload)


client = mqtt.Client()
client.on_connect = on_connection
client.on_subscribe = on_subscription
client.on_message = on_message
client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
client.loop_start()
while True:
    client.publish(PUBLISH_TOPIC,
                   "hello this is Kyle")
    time.sleep(10)
