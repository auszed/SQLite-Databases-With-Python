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
c.execute("INSERT INTO custumers VALUES('John', 'Elder', 'John@JON.bom')")


# aADDING A LOT OF ELEMENTS AT THE SAME TIME
many_custumers = [
    ('lucas', 'karla', 'lucas@gm.com'),
    ('karla', 'kuewa', 'karla@gm.com' ),
    ('maria', 'pas', 'maria@gm.com' ),
    ('luisa', 'rels', 'luisa@gm.com' )
]
# ussing a place holñder to creatr a custumers vbalues into the databases
c.executemany("INSERT INTO custumers VALUES(?,?,?)", many_custumers)


# we can print on the screen so we know that its all working correctly
print("adding the row correctly...")

# commint the connection to the data base, this mean connecting all
conn.commit()

# also we need to always try to close the connection
conn.close()





