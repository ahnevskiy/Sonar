from tkinter import *
from tkinter.ttk import Checkbutton, LabelFrame


class MyCheckBox(object):
    def __init__(self, parent, group, command, x=0, y=0):
        self.state = BooleanVar(False)
        self.object = Checkbutton(parent.container, var=self.state, command=command, width=0)
        self.group = group
        self.x = x
        self.y = y
        self.object.place(x=self.x, y=self.y)
        self.buf_state = self.object["state"]
