# Copyright (c) 2022 Kyle Lopin <kylel@nu.ac.th>

""" 
Run unit tests on the StatusButton class in the main_gui file
"""

# __author__ = "Kyle Vitautas Lopin"

# standard libraries
import os
import sys
import unittest
# print(os.getcwd())
# print(os.path.abspath(os.path.join("..", "..", "src", "app")))

sys.path.append(os.path.join("..", "..", "src", "app"))
# # local files
from src.app import main_gui


class TestStatusButton(unittest.TestCase):
    def test_toggle_color(self):
        status_button = main_gui.StatusButton(None, "Kyle")
        color = status_button.canvas.itemcget(status_button.circle,
                                              'fill')
        self.assertEqual(color, "red",
                         msg="StatusButton color not initialized correctly")
        self.assertEqual(status_button.color, "red",
                         msg="Status color not initialized correctly")

        status_button.toggle_color(True)
        color = status_button.canvas.itemcget(status_button.circle,
                                              'fill')
        self.assertEqual(color, "green",
                         msg="StatusButton color not changed correctly")
        self.assertEqual(status_button.color, "green",
                         msg="Status color not changed correctly")

        status_button.toggle_color(True)
        color = status_button.canvas.itemcget(status_button.circle,
                                              'fill')
        self.assertEqual(color, "green",
                         msg="StatusButton color not changed correctly")
        self.assertEqual(status_button.color, "green",
                         msg="Status color not changed correctly")

        status_button.toggle_color(False)
        color = status_button.canvas.itemcget(status_button.circle,
                                              'fill')
        self.assertEqual(color, "red",
                         msg="StatusButton color not changed correctly for False")
        self.assertEqual(status_button.color, "red",
                         msg="Status color not changed correctly for False")


if __name__ == '__main__':
    unittest.main()
