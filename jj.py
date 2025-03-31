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

# Insert sample songs into the songs table
def populate_songs(conn):
    try:
        cursor = conn.cursor()

        # Sample songs data for Anirudh Ravichandran
        songs_data = [
               ('Abhi Mujh Mein Kahin', 'Sonu Nigam', '/mp3/sn_abhimujh.mp3'),
('Chak De', 'Sonu Nigam', '/mp3/sn_chakde.mp3'),
('Do Pal', 'Sonu Nigam', '/mp3/sn_dopal.mp3'),
('Ishq Hua', 'Sonu Nigam', '/mp3/sn_ishqhua.mp3'),
('Maahi Ve', 'Sonu Nigam', '/mp3/sn_mahive.mp3'),
('Main Hoon Na', 'Sonu Nigam', '/mp3/sn_mainhoona.mp3'),
('Saathiya', 'Sonu Nigam', '/mp3/sn_sathiya.mp3'),
('Sun Zara', 'Sonu Nigam', '/mp3/sn_sunzara.mp3'),
('Tere Bin', 'Sonu Nigam', '/mp3/sn_terebin.mp3'),
('Tum Dekho Naa', 'Sonu Nigam', '/mp3/sn_tumhidekh.mp3')
        ]

        # Insert songs into the songs table
        cursor.executemany('''
            INSERT INTO songs (title, artist, file_path)
            VALUES (?, ?, ?)
        ''', songs_data)

        # Commit the transaction
        conn.commit()
        print("Songs inserted successfully!")
    except sqlite3.Error as e:
        print(f"Error inserting songs: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

# Main function to populate the songs table
def main():
    conn = connect_to_db()
    if conn:
        populate_songs(conn)

# Run the script
if __name__ == "__main__":
    main()