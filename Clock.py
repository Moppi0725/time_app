from tkinter import *
import tkinter as tk
import datetime
class Clock():
    def __init__(self, root):
        self.root = root
        self.Clock_label = tk.Label(self.root)
        self.Clock_label["bg"] = "#43676b"
        self.Clock_label["fg"] = "#eaf4fc"
        self.Clock_label.pack(side="top")
        

    def update_clock(self):
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.Clock_label.configure(text=now)
        self.root.after(1000, self.update_clock)