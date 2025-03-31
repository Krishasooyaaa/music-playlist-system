import sqlite3

# Connect to the SQLite database
def connect_to_db(db_path='project.db'):
    try:
        conn = sqlite3.connect(db_path)
        print("Connected to the database successfully!")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Fetch all table names in the database
def get_table_names(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        return [table[0] for table in tables]  # Extract table names from the result
    except sqlite3.Error as e:
        print(f"Error fetching table names: {e}")
        return []

# Fetch and print all rows from a table
def print_table_contents(conn, table_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Print table name and column names
        print(f"\nTable: {table_name}")
        column_names = [description[0] for description in cursor.description]
        print("Columns:", ", ".join(column_names))

        # Print rows
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error fetching data from table {table_name}: {e}")

# Main function to check the database
def check_database(db_path='project.db'):
    conn = connect_to_db(db_path)
    if not conn:
        return

    # Get all table names
    tables = get_table_names(conn)
    if not tables:
        print("No tables found in the database.")
        return

    # Print contents of each table
    for table in tables:
        print_table_contents(conn, table)

    

    # Close the connection
    conn.close()
    print("\nDatabase connection closed.")

# Run the script
if __name__ == "__main__":
    check_database()