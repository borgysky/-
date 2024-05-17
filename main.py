

#import ui
import tkinter as tk
from tkinter import ttk
# app = ui.app()
# app.mainloop()

class aaaa(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("aaaa")
        self.geometry("700x800")

        classes = ttk.Button(text="classes")
        classes.pack()

        teachers = ttk.Button(text="teachers")
        teachers.pack()
        
        students = ttk.Button(text="students")
        students.pack()

        groups = ttk.Button(text="groups")
        groups.pack()

        subjects = ttk.Button(text="subjects")
        subjects.pack()

if __name__ == '__main__':
    root = aaaa()
    root.mainloop()


