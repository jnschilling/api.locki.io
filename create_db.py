import sqlite3
import uuid

# Connect to the SQLite database (it will create a new file named "mydatabase.db")
conn = sqlite3.connect('locki.db')
cursor = conn.cursor()
# columns
col = [
    " uid TEXT PRIMARY KEY NOT NULL",
    " bech32 STRING NOT NULL",
    " herotag STRING",
    " creation_timestamp DATETIME",
    " log_timestamp DATETIME"
]

# delete table
drop_table_cmd = f"DROP TABLE user"
conn.execute(drop_table_cmd)

# Create a new table with a UUID column
create_table_cmd = f"CREATE TABLE user ({','.join(col)})"
conn.execute(create_table_cmd)
# Commit the changes and close the connection
conn.commit()
conn.close()


def insert_record(user_data):
    conn = sqlite3.connect('locki.db')
    cursor = conn.cursor()

    # Generate a new UUID
    # user_data = user_data + ({uuid.uuid4()},)

    print(user_data)
    insert_cmd = f"INSERT INTO user VALUES ({user_data})"
    cursor.execute(insert_cmd)

    conn.commit()
    conn.close()

    # "erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th": {
    #     "bech32": "erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th",
    #     "herotag": "alice",
    #     "timestamp": get_timestamp(),
    # },
    # "erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx": {
    #     "bech32": "erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx",
    #     "herotag": "bob",
    #     "timestamp": get_timestamp(),


addresses = [
    "'erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th', 'alice', '2022-10-08 09:15:10','2022-10-08 09:15:10'",
    "'erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx', 'Bob', '2022-10-08 09:16:13','2022-10-08 09:15:10'",
    "'erd10000gx', 'sample', '2022-10-08 09:15:27','2022-10-08 09:15:10'",
]

# Prepend a UUID to each address tuple string
new_addresses = [f"'{uuid.uuid4()}', {address}" for address in addresses]

for user_data in new_addresses:
    insert_record(user_data)
