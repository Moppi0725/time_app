from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from Clock import Clock
from Timer import Timer


class Time_app():
    def __init__(self):
        self.root = tk.Tk()
        self.Clock = Clock(self.root)
        self.Timer = Timer(self.root)
        self.Clock.update_clock()
        self.Timer.update_timer()
        self.root.mainloop()
            
app = Time_app()