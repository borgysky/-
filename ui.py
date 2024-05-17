import sys, os
from sys import path
import datetime

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

textstyle = ("Segoe", 18)

class app(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Школа искусств")
        global combobox
        tables = ["Занятия", "Группы", "Ученики", "Предметы", "Учителя"]
        combobox = ttk.Combobox(values=tables, state="readonly")
        combobox.pack(anchor="nw")
        frame = tk.Frame(self)
        frame.pack(side="top", fill="both", expand=True)
        frame.grid_rowconfigure(0, weight=2)
        frame.grid_columnconfigure(0, weight=2)
        self.frames = {}
        for instance in (ViewStudents, ViewClasses):
            frame = instance(frame, self)
            frame.grid(row= 0, column=0, sticky="nsew")



class ViewStudents(tk.Frame):



class ViewClasses(tk.Frame):
