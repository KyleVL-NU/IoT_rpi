# Copyright (c) 2022 Kyle Lopin <kylel@nu.ac.th>

""" Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a mqtt communication channel
"""

__author__ = "Kyle Vitautas Lopin"

# libraries / modules / packages
import tkinter

# make a variable to change color
color = 'red'  # = assignment; assign 'red' to color

# make a python function to print "Hello World"
# def - define
def hello_world():
    # make it go green -> yellow -> red
    global color
    print("Hello World")
    if color == 'red':  # == is a comparison
        color = 'green'
    # if (color == 'green') {  arduino like
    # code in here;
    # }
    elif color == 'green':  # else if
        color = 'red'
    canvas.itemconfig(circle, fill=color)

app = tkinter.Tk()  # application a class of tkinter.Tk
# geometry is a method of the tkinter.Tk class that
# sets the size of the app window.  It takes a
# string as an argument.
app.geometry("400x400")
canvas = tkinter.Canvas(app, width=120, height=120)
circle = canvas.create_oval(10, 10, 110, 110,
                            fill=color)
canvas.pack()

# make a button [tkinter class] and put it in the app
# Button takes 3 arguments, app-where to put the button
# text - key word argument
tkinter.Button(app, text="Hello World",
               command=hello_world).pack()

app.mainloop()  # mainloop is method of tkinter.Tk
# methods are functions of classes
