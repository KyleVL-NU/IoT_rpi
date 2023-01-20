# Copyright (c) 2023 Kyle Lopin <kylel@nu.ac.th>

"""
Display the data coming in from the sensors
Wrap a matplotlib pyplot in a tkinter frame
"""

__author__ = "Kyle Vitautas Lopin"

# standard libraries
from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import tkinter as tk

# installed libraries
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 40, 80, 160]


class Display(tk.Frame):
    """
    Display for sensor data implemented in a matplotlib.pyplot and
    wrapped in a tkinter Frame

    Attributes:
        figure (matplotlib.Figure): figure of the displayed data
        axis (matplotlib.axes): axis the data is plotted on
        lines (list[matplotlib.lines]): lines objects of the data
        canvas (FigureCanvasTkAgg): canvas displaying the data
    """
    def __init__(self, _parent: tk.Tk):
        tk.Frame.__init__(self, master=_parent)
        self.figure = plt.Figure(figsize=(6, 4))
        self.axis = self.figure.add_subplot()
        self.axis.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.lines = self.axis.plot([], [])
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def update_line(self, x_data: list, y_data: list):
        """
        Update the data to be displayed and re-draw the canvas

        Args:
            x_data (list[floats]): x-axis coordinates of the data
            y_data (list[floats]): y-axis coordinates of the data
        """
        self.lines[0].set_xdata(x_data)
        self.lines[0].set_ydata(y_data)
        print(self.lines[0].get_xydata())
        now = x_data[-1]
        self.axis.set_xlim([now - timedelta(minutes=5),
                            now + timedelta(minutes=5)])
        self.axis.set_ylim([0, 40])
        self.canvas.draw()


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
        self.display = Display(_parent)
        self.display.pack()

    def add_data(self):
        """
        Append new received data from a sensor and add it to the existing data.
        Call the Display child to update the user's view of the data
        """
        self.time.append(datetime.now())
        self.temperature.append(random.randrange(20, 35))
        self.display.update_line(self.time, self.temperature)


if __name__ == '__main__':
    parent = tk.Tk()  # main_gui
    sensor_data = SensorData(parent)
    tk.Button(parent, text="Update data",
              command=sensor_data.add_data).pack()
    parent.mainloop()
