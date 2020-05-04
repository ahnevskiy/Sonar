from tkinter import *


class MyButton(object):
    def __init__(self, parent, command, text="", x=0, y=0, bg=None, fg="black"):
        self.object = Button(parent, text=text, state="disabled", command=command, bg=bg, fg=fg)
        self.x = x
        self.y = y
        self.object.place(x=self.x, y=self.y)
        self.buf_state = self.object["state"]



