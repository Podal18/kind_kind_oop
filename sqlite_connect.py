import sqlite3

connection = sqlite3.connect("qq.db")

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS WORKER(
ID_W INTEGER PRIMARY KEY,
NAME TEXT,
AGE INTEGER)''')
connection.commit()
connection.close()


