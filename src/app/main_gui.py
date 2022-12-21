# Copyright (c) 2022 Kyle Lopin <kylel@nu.ac.th>

""" Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a mqtt communication channel
"""

__author__ = "Kyle Vitautas Lopin"

# standard libraries / modules / packages
import tkinter as tk

# local files
import comm_mqtt

NAMES = ["Kyle", "Chatpon", "Tao", "Sudarat"]


class SensorUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)  # initialize parent class
        self.comm = comm_mqtt.MQTTConn(self)
        status_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=5)
        self.status_buttons = []
        for i in range(4):
            status_btn = StatusButton(status_frame, NAMES[i])
            self.status_buttons.append(status_btn)
        status_frame.pack(side=tk.TOP)
        # make a button [tkinter class] and put it in the app
        # Button takes 3 arguments, app-where to put the button
        # text - key word argument
        self.running = False
        self.button = tk.Button(self, text="Turn On",
                                command=self.button_click,
                                width=20)
        self.button.pack(side=tk.TOP)

    def button_click(self):
        if self.running:  # if True turn off the sensor
            self.running = False
            msg = "Off"
            self.button.config(text="Turn on")
        else:
            self.running = True
            msg = "On"
            self.button.config(text="Turn off")
        self.change_status("Kyle", self.running)
        self.comm.publish(msg)

    def change_status(self, name, _running):
        index = NAMES.index(name)  # ดัชนี
        self.status_buttons[index].toggle_color(_running)


class StatusButton(tk.Frame):
    """ Display the status using a canvas

    Attributes:
        circle: object used to display the status
        canvas (tk.Canvas): canvas the circle is in
        color (str): color the circle will show

    """
    def __init__(self, parent, name):
        tk.Frame.__init__(self, master=parent)
        self.color = 'red'
        self.canvas = tk.Canvas(self, width=120, height=120)
        self.circle = self.canvas.create_oval(10, 10, 110, 110,
                                              fill=self.color)
        self.canvas.pack(side=tk.TOP)
        tk.Label(self, text=name, font=42).pack(side=tk.TOP)
        self.pack(side=tk.LEFT)

    def toggle_color(self, state):
        """ Toggle the color between red and green """
        if state:
            self.color = 'green'
        else:
            self.color = 'red'
        self.canvas.itemconfig(self.circle, fill=self.color)


if __name__ == "__main__":
    app = SensorUI()  # application a class of tkinter.Tk
    # geometry is a method of the tkinter.Tk class that
    # sets the size of the app window.  It takes a
    # string as an argument.
    app.geometry("600x400")
    app.mainloop()  # mainloop is method of tkinter.Tk
    # methods are functions of classes
