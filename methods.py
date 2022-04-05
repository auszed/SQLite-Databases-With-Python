# importing the sql platform
import sqlite3


# here we havee all the method of this app


# -----------------------------------
# query data base with all the results
def show_all():
    # This create a database in memory
    conn = sqlite3.connect('custumer.db')
    # create a cursor
    c = conn.cursor()
    # using or // and 
    c.execute("SELECT rowid,* FROM custumers")
    # print on the screen
    items = c.fetchall()
    for item in items:
        print(item)
    # commint the connection to the data base, this mean connecting all
    conn.commit()
    # also we need to always try to close the connection
    conn.close()


# -----------------------------------
# ADD ITEMS TO THE TABLE
def add_one(first, last, email):
    # This create a database in memory
    conn = sqlite3.connect('custumer.db')
    # create a cursor
    c = conn.cursor()
    c.execute("""
    INSERT INTO custumers VALUES (?,?,?)""",
    (first, last, email)
    )
    # commint the connection to the data base, this mean connecting all
    conn.commit()
    # also we need to always try to close the connection
    conn.close()


# -----------------------------------
# delete a row
def delete_one(id):
    # This create a database in memory
    conn = sqlite3.connect('custumer.db')
    # create a cursor
    c = conn.cursor()

    c.execute("DELETE FROM custumers WHERE rowid = (?)", id )

    # commint the connection to the data base, this mean connecting all
    conn.commit()
    # also we need to always try to close the connection
    conn.close()

# -----------------------------------
# adding many records to a table 
def many_records(list):
    # This create a database in memory
    conn = sqlite3.connect('custumer.db')
    # create a cursor
    c = conn.cursor()
    c.executemany("""
    INSERT INTO custumers VALUES (?,?,?)""",
    (list)
    )
    # commint the connection to the data base, this mean connecting all
    conn.commit()
    # also we need to always try to close the connection
    conn.close()


# -----------------------------------
# filtering
def email_lookup(email):
    # This create a database in memory
    conn = sqlite3.connect('custumer.db')
    # create a cursor
    c = conn.cursor()
    c.execute("SELECT * FROM custumers WHERE email = (?)", (email,))
    # print on the screen
    items = c.fetchall()
    for item in items:
        print(item)
    # commint the connection to the data base, this mean connecting all
    conn.commit()
    # also we need to always try to close the connection
    conn.close()


