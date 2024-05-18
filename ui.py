import db_conn
import tkinter as tk
from tkinter import ttk, messagebox

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Школа искусств")
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

        button_texts = ["Занятия", "Учителя", "Ученики",
                        "Группы", "Предметы"]
        table_titles = ["classes", "teachers", "students",
                        "groups", "subjects"]
        button_height = 30
        button_width = 200
        button_spacing = 10
        window_height = len(button_texts) * (button_height + button_spacing) - button_spacing
        window_width = button_width + 70 
        self.geometry(f"{window_width}x{window_height}")
        for labels, text in enumerate(table_titles):
            ttk.Button(text=button_texts[labels], command=lambda t=text: open_or_show_window(t)).pack(expand=True, pady=0)


class New_window(tk.Toplevel):
    def __init__(self, table_name, connect):
        super().__init__()
        self.connect = connect
        self.table_name = table_name
        self.add_button = ttk.Button(self, text='Добавление', command=lambda: self.add_button_action())
        self.rm_button = ttk.Button(self, text="Удаление", command=lambda: self.rm_button_action())
        self.edit_button = ttk.Button(self, text="Редактирование", command=lambda: self.edit_button_action())
        self.columns_names = db_conn.check_columns(connect, table_name)
        self.table = ttk.Treeview(self, columns=self.columns_names, show='headings')
        for name in self.columns_names:
            self.table.heading(name, text=name)
        self.table.pack(expand=True, fill=tk.BOTH)
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.add_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.rm_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.edit_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.edit_dialog = None
        self.entries = []
        self.current_item = None
        self.rows = db_conn.read_entry(connect, table_name)
        for row in self.rows:
            self.load_data(row)
      
    def edit_button_action(self):
        highlight = self.table.focus()
        if not highlight:
            messagebox.showwarning("Внимание", f"Выберите строку")
            return
        data = self.table.item(highlight, 'values')
        uid = data[0]
        self.current_item = highlight
        if self.edit_dialog is not None:
            self.edit_dialog.destroy()
        self.edit_dialog = tk.Toplevel(self)
        self.edit_dialog.title("Редактировать")
        column_count = len(self.table["columns"])
        self.entries = [] 
        for i in range(column_count):
            column_name = self.table["columns"][i]
            label = tk.Label(self.edit_dialog, text=f"Введите значение для {column_name}:")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(self.edit_dialog)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)
        for i in range(len(data)):
            if i < len(self.entries):  
                self.entries[i].insert(0, data[i])
        save_btn = tk.Button(self.edit_dialog, text="Save", command=lambda : self.save_changes(uid))
        save_btn.grid(row=column_count, columnspan=2, pady=10)

    def save_changes(self, uid):
        new_values = [entry.get() for entry in self.entries]
        data = [tuple(new_values)]
        exception = db_conn.update_entry(self.connect, self.table_name, data, uid)
        if exception == None:
            self.table.item(self.current_item, values=new_values)
        self.edit_dialog.destroy()
        self.edit_dialog = None

    def add_button_action(self):
        if not hasattr(self, 'add_dialog'):
            self.add_dialog = tk.Toplevel(self)
            self.add_dialog.title("Add")
            column_count = len(self.table["columns"])
            self.entries = []
            for i in range(column_count):
                column_name = self.table["columns"][i]
                label = tk.Label(self.add_dialog, text=f"Введите значение для {column_name}:")
                label.grid(row=i, column=0, padx=5, pady=5)
                entry = tk.Entry(self.add_dialog)
                entry.grid(row=i, column=1, padx=5, pady=5)
                self.entries.append(entry)
            add_btn = tk.Button(self.add_dialog, text="Добавить", command=lambda: self.add_record(self.entries, self.add_dialog))
            add_btn.grid(row=column_count, columnspan=2, pady=10)
            self.add_dialog.protocol("WM_DELETE_WINDOW", self.close_add_dialog)
        else:
            tk.messagebox.showinfo("Внимание", "Завершите добавление текущей записи перед созданием новой.")

    def close_add_dialog(self):
        if hasattr(self, 'add_dialog'):
            self.add_dialog.destroy()
            del self.add_dialog

    def add_record(self, entries, add_dialog):
        try:
            new_values = [entry.get() for entry in entries]
            data = [tuple(new_values)]
            exception = db_conn.add_entry(self.connect, self.table_name, data)
            if exception == None:
                self.table.insert('', 'end', values=new_values)
            add_dialog.destroy()
            del self.add_dialog
        except Exception as e:
            messagebox.showerror("Ошибка", f"The error '{e}' occurred")
    
    def load_data(self, entry):
        rows = []
        i = 0
        while i != len(entry):
            i+=1
            rows.append(entry[i-1])
        self.table.insert('', 'end', values=rows)

    def rm_button_action(self):
        try:
            selected_item = self.table.focus()
            if not selected_item:
                messagebox.showwarning("Внимание", f"Выберите строку")
                return
            if selected_item:
                item_text = self.table.item(selected_item, 'values')
                confirm = messagebox.askyesno("Подтверждение удаления",
                                              f"Вы уверены, что хотите удалить запись {item_text}?")
                if confirm:
                    self.table.delete(selected_item)
                    db_conn.delete_entry(self.connect, self.table_name, item_text)
        except Exception as e:
            messagebox.showerror("Ошибка", f"The error '{e}' occurred")
