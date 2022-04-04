# importing the sql platform
import sqlite3
# This create a database in memory
conn = sqlite3.connect('delete_table.db')

# create a cursor
c = conn.cursor()

# # create a table in SQL
# c.execute("INSERT INTO delete_table VALUES('John', 'Elder', 'John@JON.bom')")
# c.execute("SELECT rowid,* FROM delete_table")

# # print on the screen
# items = c.fetchall()
# for item in items:
#     print(item)

    # here its where we drop the table
c.execute("DROP TABLE delete_table")




# we can print on the screen so we know that its all working correctly
print("table was dropped already")

# commint the connection to the data base, this mean connecting all
conn.commit()

# also we need to always try to close the connection
conn.close()





