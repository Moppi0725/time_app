from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
class Timer():
    def __init__(self, root):
        self.root = root
        self.set_time = -1
        self.input_timer = Entry(self.root)
        self.input_timer.pack()
        self.input_timer.insert(END, "Timer:何秒はかりますか？")
        self.time_set_button = Button(self.root, text = "OK", command = self.set_time_button)
        self.time_set_button.pack()
        self.timer_label = tk.Label(self.root)
        self.timer_label["bg"] = "#43676b"
        self.timer_label["fg"] = "#eaf4fc"
        self.timer_label.pack(side="top")

    def set_time_button(self):
        self.set_time = int(self.input_timer.get())
        self.update_timer()

    def update_timer(self):
        if(self.set_time>0):
            print(self.set_time)
            self.timer_label.configure(text="{}".format(self.set_time))
            self.set_time = self.set_time-1
            self.root.after(1000, self.update_timer)
        elif(self.set_time == 0):
            self.timer_label.configure(text="{}".format(self.set_time))
            mb.showinfo("alart","時間になりました!")