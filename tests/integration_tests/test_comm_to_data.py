# Copyright (c) 2023 Kyle Lopin <kylel@nu.ac.th>

""" 
Integration tests that inputs to the communications class
get passed to the data class correctly
"""

__author__ = "Kyle Vitautas Lopin"

# standard libraries
from datetime import datetime
import os
import sys
import unittest
from unittest import mock

# installed libraries
import paho.mqtt.client as mqtt

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import comm_mqtt
from src.app import sensor_data


class TestCommToData(unittest.TestCase):
    def test_comm_msg_to_data(self):
        mock_root = mock.Mock()
        mock_root.data = sensor_data.SensorHubData(None)
        print(f"mock data: {mock_root.data}")
        print(f"mock add_data: {mock_root.data.add_data}")
        comm = comm_mqtt.MQTTConn(mock_root)
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Kyle/data"
        msg.payload = b'{"datetime": "2023-02-08 10:48:32", "device": "device 2", "temperature": 30}'
        return_code = comm.on_message(None, None, msg)
        now = datetime(2023, 2, 8, 10, 48, 32)
        print(f"return code: {return_code}")
        print(f"add_data: {comm.root.data.add_data}")
        print(mock_root.data)
        print(mock_root.data.sensors)

        _sensor_data = mock_root.data.sensors["device 2"]
        print(f"data time: {_sensor_data.time}")
        print(f"data temperature: {_sensor_data.temperature}")
        self.assertListEqual([now], _sensor_data.time)
        self.assertListEqual([30], _sensor_data.temperature)


if __name__ == '__main__':
    unittest.main()
