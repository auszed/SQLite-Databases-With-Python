import methods


# add an item in the table
methods.add_one("jose", "mar", "rerex@get.com")

# delete method but as string
methods.delete_one('9')


# list of items to add
stuff = [
    ('brenda', 'smith', 'bren@io.com'),
    ('yosh', 'near', 'uoner@yonit.de')
    ]

# # add many records
methods.many_records(stuff)


# print on screen
methods.show_all()


# looking for the email
methods.email_lookup("bren@io.com")