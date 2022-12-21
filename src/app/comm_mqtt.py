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

# local file
import main_gui  # for type hinting

HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC = "Naresuan/Kyle"
SUBSCRIBE_TOPIC = "Naresuan/+"


class MQTTConn:
    def __init__(self, root: main_gui.SensorUI):
        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        self.client.on_message = self.on_message
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, message):
        self.client.publish(PUBLISH_TOPIC, message)

    def on_connection(self, *args):
        """ Call back for when mqtt connects to the broker
         and prints out an acknowledgement and subscribes """
        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)

    def on_message(self, client, user_data, msg: mqtt.MQTTMessage):
        print("got message: ", msg.payload)
        print("from topic: ", msg.topic)
        name = msg.topic.split('/')[-1]
        print("message from: ", name)
        if msg.payload == b"On":
            sensor_state = True
        else:
            sensor_state = False
        self.root.change_status(name,
                                sensor_state)


if __name__ == '__main__':
    client = MQTTConn()
    while True:
        client.publish(PUBLISH_TOPIC,
                       "hello this is Kyle")
        time.sleep(10)
