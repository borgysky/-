import db_conn

import tkinter as tk
from tkinter import ttk

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Школа искусств")
        self.geometry("700x800")
        self.connect = db_conn.connect("art school", "postgres", "postgresql", "localhost", "5432")
        self.created_windows = {}
        
        def open_or_show_window(window_title):
            if window_title not in self.created_windows:
                new_window = New_window(window_title, self.connect)
                new_window.title(window_title)
                self.created_windows[window_title] = new_window
                new_window.protocol("WM_DELETE_WINDOW", lambda: on_window_close(window_title))
            else:
                self.created_windows[window_title].deiconify()

        def on_window_close(window_title):
            self.created_windows[window_title].withdraw()

        button_texts = ["classes", "teachers", "students",
                        "groups", "subjects"]

        for text in button_texts:
            ttk.Button(text=text, command=lambda t=text: open_or_show_window(t)).pack(expand=True, pady=0)


class New_window(tk.Toplevel):
    def __init__(self, table_name, connect):
        super().__init__()
        self.add_button = ttk.Button(self, text='add', command=lambda: add_button(self))
        self.rm_button = ttk.Button(self, text="rm", command=lambda: rm_button())
        self.edit_button = ttk.Button(self, text="edit")
        self.columns_names = db_conn.check_columns(connect,table_name)
        self.table = ttk.Treeview(self, columns= self.columns_names)
        for name in self.columns_names:
            self.table.heading(name, text=name)
        self.table.pack(expand=True, fill=tk.BOTH)
        self.add_button.pack(anchor='w')
        self.rm_button.pack(anchor='w')
        self.edit_button.pack(anchor='w')

        def add_button(self):
            self.table.insert('', 'end', text='1', values=('123', 'dfasd', 'asdasd', '3234523', 'sadhdfg', '3123', 'asdasd'))

        def rm_button():
            highlited_row = self.table.selection()
            if highlited_row:
                self.table.delete(highlited_row)
        
        def edit_button(self):
            pass
        
