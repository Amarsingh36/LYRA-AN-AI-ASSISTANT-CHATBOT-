import csv
import sqlite3
from unittest import result

con = sqlite3.connect("lyra.db")

cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCAHR(100),path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'','')"
# cursor.execute(query)
# con.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200),mobile_no VARCHAR(255),email VARCHAR(255) NULL)''')
# desired_columns_indices =[0,18]
# with open(r"C:\Users\amart\Desktop\major project 3\engine\contacts.csv", 'r', encoding='utf-8') as csvfile:

# # with open ('contacts.csv','r',encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute('''INSERT INTO contacts (id,'name','mobile_no') VALUES (null,?,?);''',tuple(selected_data))


# con.commit()
# con.close()

# query = 'ansh'
# query = query.strip()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE? OR LOWER(name) LIKE?",('%'+ query+'%',query+'%'))
# results = cursor.fetchall()
# print(results[0][0])