# Copyright (c) 2023 Kyle Lopin <kylel@nu.ac.th>

""" 
Make a class to hold and process incoming sensor data
"""

__author__ = "Kyle Vitautas Lopin"

# standard libraries
from dataclasses import dataclass
from datetime import datetime
import random
import tkinter as tk

# local file
import display


@dataclass
class SensorData:
    """
    Data class to hold 1 sensors time series data

    Attributes:
        time (list[datetime]): time stamps of when teh sensor read data
        temperature (list[floats]): sensor data
        display (Display): child that will display the data of this class
    """
    time = []
    temperature = []

    def __init__(self, _parent: tk.Tk):
        self.display = display.Display(_parent)
        self.display.pack()

    def add_data(self, time: datetime, temp: float):
        """
        Append new received data from a sensor and add it to the existing data.
        Call the Display child to update the user's view of the data
        """
        self.time.append(time)
        self.temperature.append(temp)
        self.display.update_line(self.time, self.temperature)


if __name__ == '__main__':
    parent = tk.Tk()  # main_gui
    sensor_data = SensorData(parent)

    # use a lambda function to pass arguments
    tk.Button(parent, text="Update data",
              command=lambda: sensor_data.add_data(
                  datetime.now(), random.randrange(20, 35))
              ).pack()
    parent.mainloop()
