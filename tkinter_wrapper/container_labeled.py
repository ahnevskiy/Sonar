from tkinter import *
from tkinter.ttk import Checkbutton, LabelFrame


class MyContainerLabeled(object):
    def __init__(self, parent, name, del_name, label, x, y, width, height):
        self.container = LabelFrame(parent, text=label, width=width, height=height)
        parent.children[name] = parent.children.pop(del_name)
        self.container.place(x=x, y=y)
        self.buf_access = self.collect_access()

    def collect_access(self):
        result = {}
        for obj in self.container.children.values():
            result[obj] = obj["state"]
        return result

    def add_objects(self, objects):
        self.objects += objects

    def disable_all(self):
        for obj in self.objects:
            obj.object.configure(state="disabled")

    def enable_all(self):
        for obj in self.objects:
            obj.object.configure(state="normal")

    def restore_state_all(self):
        for obj in self.objects:
            obj.object.configure(state=obj.buf_state)
