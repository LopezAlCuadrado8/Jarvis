import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Create a table sys_command if not exist
query = "CREATE TABLE IF NOT EXiSTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# Create a table web_command if not exist
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# # Insert into table sys_command
# query = "INSERT INTO sys_command VALUES (null,'android','C:\\Program Files\\Notepad++\\notepad++.exe')"
# cursor.execute(query)
# con.commit()

# # Insert into table web_command
# query = "INSERT INTO web_command VALUES (null,'canva','canva.com')"
# cursor.execute(query)
# con.commit()


