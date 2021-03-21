import sqlite3
conn=sqlite3.connect("data.db")
print("Database created successfully")
conn.execute("CREATE TABLE students(Name TEXT,Address TEXT,City TEXT,PinCode TEXT)")
print("table created")
conn.close()