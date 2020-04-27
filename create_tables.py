import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# CREATE TABLE
create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price int)"
cursor.execute(create_items_table)

'''

users = [
    (1, 'username1', 'password1'),
    (2, 'username2', 'password2')   
]


items = [
    {
        'name': 'Bread',
        'price': 20
    },
    {
        'name': 'Soap',
        'price': 30
    }
]

INSERT RECORDS
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.executemany(insert_query, users)

PRINT USERS
select_query = "SELECT * from users"
iterator = cursor.execute(select_query)

for user in iterator:
    print(user)

'''

connection.commit()
connection.close()

