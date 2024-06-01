import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Execute the update query
update_query = "UPDATE table_name SET column_name = ? WHERE condition"
new_value = "your_new_value"
cursor.execute(update_query, (new_value,))

# Commit the changes and close the connection
conn.commit()
conn.close()