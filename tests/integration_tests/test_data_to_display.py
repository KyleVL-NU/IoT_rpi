# Copyright (c) 2023 Kyle Lopin <kylel@nu.ac.th>

""" 
Test that when data is input to the sensor_data.Sensor data that
it is passed and handled correctly by the display.Display class
"""

__author__ = "Kyle Vitautas Lopin"


# standard libraries
from datetime import datetime
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import display
from src.app import sensor_data


class TestDataToDisplay(unittest.TestCase):
    def test_data_to_display(self):
        """
        Test that adding data to the data class makes the
        pyplot graph have the correct xy data
        """
        sensor_class = sensor_data.SensorHubData(None)
        print(f"START {sensor_class.display.lines['device 2'].get_xydata()}")
        # add 1 data point and check it is added correctly
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data("device 2", now, 5)
        print("==")
        print(sensor_class.display.lines)
        xy_data = sensor_class.display.lines["device 2"].get_xydata().tolist()
        # TODO: calculate how datetime is converted to a float
        self.assertListEqual([[19381.45152777778, 5.0]], xy_data)

    def test_draw_is_called(self):
        # initialize the sensor class
        sensor_class = sensor_data.SensorHubData(None)
        # to check if a method is called mock it first
        sensor_class.display.canvas.draw = mock.Mock()
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data("device 2", now, 5)
        # check that the draw function is called
        sensor_class.display.canvas.draw.assert_called()


if __name__ == '__main__':
    unittest.main()
