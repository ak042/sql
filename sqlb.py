# INSERT Command

# import the sqlite3 lib
import sqlite3

# create the conn
conn = sqlite3.connect("new.db")

# get a cursor obj 
cursor = conn.cursor()


# insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

conn.commit()
conn.close()