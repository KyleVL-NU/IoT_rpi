# Copyright (c) 2022 Kyle Lopin <kylel@nu.ac.th>

""" Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a mqtt communication channel
"""

__author__ = "Kyle Vitautas Lopin"

# standard libraries / modules / packages
import tkinter as tk


class StatusButton:
    """ Display the status using a canvas

    Attributes:
        circle: object used to display the status
        canvas (tk.Canvas): canvas the circle is in
        color (str): color the circle will show

    """
    def __init__(self, parent):
        self.color = 'red'
        self.canvas = tk.Canvas(parent, width=120, height=120)
        self.circle = self.canvas.create_oval(10, 10, 110, 110,
                                              fill=self.color)
        self.canvas.pack()

    def toggle_color(self):
        """ Toggle the color between red and green """
        if self.color == 'red':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'red'
        self.canvas.itemconfig(self.circle, fill=self.color)


app = tk.Tk()  # application a class of tkinter.Tk
# geometry is a method of the tkinter.Tk class that
# sets the size of the app window.  It takes a
# string as an argument.
app.geometry("400x400")
status_btn = StatusButton(app)
print(status_btn)
status_btn2 = StatusButton(app)
print(status_btn2)

# make a button [tkinter class] and put it in the app
# Button takes 3 arguments, app-where to put the button
# text - key word argument
tk.Button(app, text="Toggle Circle 1",
          command=status_btn.toggle_color).pack()
tk.Button(app, text="Toggle Circle 2",
          command=status_btn2.toggle_color).pack()

app.mainloop()  # mainloop is method of tkinter.Tk
# methods are functions of classes
