import sqlite3

con = sqlite3.connect("BB.db")
print("Database opened successfully")

con.execute("create table BBINDEX_LOSS_PERCENT (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, amount INT NOT NULL, duration INT NOT NULL, working_time INT NOT NULL, loss_percent INT NOT NULL)")

print("Table created successfully")

con.close()
