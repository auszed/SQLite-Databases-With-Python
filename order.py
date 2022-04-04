# importing the sql platform
import sqlite3

# this allow to create the database in memorry but dont save it
# conn = sqlite3.connect(':memoty:')


# This create a database in memory
conn = sqlite3.connect('custumer.db')

# create a cursor
c = conn.cursor()



# QUERY ORDER BY
c.execute("SELECT rowid,* FROM custumers ORDER BY email ASC")
# print on the screen
items = c.fetchall()
for item in items:
    print(item)


# commint the connection to the data base, this mean connecting all
conn.commit()

# also we need to always try to close the connection
conn.close()





