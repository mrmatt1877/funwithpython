import sqlite3

conn = sqlite3.connect('pets.db')
cur = conn.cursor()
query = 'select * from pets'
rows = cur.execute(query).fetchall()

#print all rows
print(rows)
#print the first 5 items, shortest code
print(rows[:5])
#print the first 5 items, cleaner output
x = 0
for row in rows:
    if x < 5:
        print(row)
        x = x + 1
