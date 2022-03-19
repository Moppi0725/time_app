from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from Clock import Clock
from Timer import Timer


class Time_app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.Clock = Clock(self.master)
        self.Timer = Timer(self.master)
        self.Clock.update_clock()
        self.Timer.update_timer()
        
            
if __name__ == "__main__":
    root = tk.Tk()
    app = Time_app(root)
    app.mainloop()