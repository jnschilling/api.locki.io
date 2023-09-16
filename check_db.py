import sqlite3
conn = sqlite3.connect("locki.db")
cur = conn.cursor()
cur.execute("SELECT * FROM user")

users = cur.fetchall()
for wallet in users:
    print(wallet)
