import pymysql
import tkinter as tk
from tkinter import ttk

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.Cursor
        )
        self.cursor = self.conn.cursor()

    def execute_proc(self):
        self.cursor.execute("CALL GetComponentHierarchy()")
        return self.cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()

class TreeViewDemo(tk.Tk):
    def __init__(self, db):
        super().__init__()

        self.title("Components Tree")
        self.geometry("600x400")

        self.db = db

        # Создание виджета Treeview
        self.tree = ttk.Treeview(self, columns=('Amount'), show='tree headings')
        self.tree.heading('#0', text='Component')
        self.tree.heading('Amount', text='Amount')
        self.tree.column('Amount', width=100, anchor=tk.CENTER)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
      
        self.populate_tree()

    def populate_tree(self):
        rows = self.db.execute_proc()

        components_dict = {}
        for row in rows:
            parent_id, parent_name, child_id, child_name, amount = row

            if parent_id not in components_dict:
                parent_item = self.tree.insert('', 'end', text=parent_name)
                components_dict[parent_id] = parent_item

            if child_id is not None:
                child_item = self.tree.insert(components_dict[parent_id], 'end', text=child_name, values=(amount,))
                components_dict[child_id] = child_item

    def on_close(self):
        self.db.close()
        self.destroy()

if __name__ == '__main__':
    
    db = Database(
        host='localhost',
        user='root',
        password='root',
        database='podik'
    )
    db.connect()
  
    app = TreeViewDemo(db)
    app.protocol("WM_DELETE_WINDOW", app.on_close) 
    app.mainloop()
