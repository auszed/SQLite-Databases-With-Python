# importing the sql platform
import sqlite3

# this allow to create the database in memorry but dont save it
# conn = sqlite3.connect(':memoty:')


# This create a database in memory
conn = sqlite3.connect('custumer.db')

# create a cursor
c = conn.cursor()

# making a query
c.execute("SELECT * FROM custumers")

# to actually see the data we need the next commands Fetchall
# the are all the possibilitys to print the Database
# c.fetchone()
# c.fetchall()
# c.fetchmany(2)

# estoy filtrando la row 1 para que solo me muestre el apellido
print(c.fetchone()[1])


# this its one way
items = c.fetchall()
for item in items:
    print(item[0] + " " + item[1] + " " + item[2] + " ")


# This its other way of printing
print("NAME "+ "\t\tEMAIL")
print("-------- "+ "\t\t--------")

for item in items:
    print(item[0] + " " + item[1] + "\t\t" + item[2] + " ")


# commint the connection to the data base, this mean connecting all
conn.commit()

# also we need to always try to close the connection
conn.close()





