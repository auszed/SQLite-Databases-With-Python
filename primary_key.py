# importing the sql platform
import sqlite3

# this allow to create the database in memorry but dont save it
# conn = sqlite3.connect(':memoty:')


# This create a database in memory
conn = sqlite3.connect('custumer.db')

# create a cursor
c = conn.cursor()

# making a query showing the primary Key
c.execute("SELECT rowid, * FROM custumers")


# filter the table with all words that end with gm.com
c.execute("SELECT * FROM custumers WHERE email LIKE '%gm.com'")


# estoy filtrando la row 1 para que solo me muestre el apellido
items = c.fetchall()


for item in items:
    print(item)


# commint the connection to the data base, this mean connecting all
conn.commit()

# also we need to always try to close the connection
conn.close()





