import mysql.connector as con

# Establish a connection
db = con.connect(
    host="localhost",   # Change if using a different host
    user="root",        # Your MySQL username
    password="",  # Your MySQL password
    database="project"  # Replace with your actual database name
)

# Check connection
if db.is_connected():
    print("Connected successfully!")
else:
    print("Connection failed.")

# Close connection
db.close()