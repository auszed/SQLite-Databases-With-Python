# importing the sql platform
import sqlite3

# this allow to create the database in memorry but dont save it
# conn = sqlite3.connect(':memoty:')


# This create a database in memory
conn = sqlite3.connect('custumer.db')

# create a cursor
c = conn.cursor()

# create a table in SQL
# we can use a only 2 quote marks"" nut we will need to add all the sql querys insdie one row
c.execute("""
CREATE TABLE custumers(
    first_name text, 
    last_name text,
    email text
)

""")

# commint the connection to the data base, this mean connecting all
conn.commit()

# also we need to always try to close the connection
conn.close()





