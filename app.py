from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_here'  # Change this for production!

# Database initialization
def get_db():
    return sqlite3.connect('project.db')

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS playlists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                file_path TEXT NOT NULL
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS playlist_songs (
                playlist_id INTEGER NOT NULL,
                song_id INTEGER NOT NULL,
                FOREIGN KEY(playlist_id) REFERENCES playlists(id),
                FOREIGN KEY(song_id) REFERENCES songs(id)
            )
        ''')
        db.commit()

init_db()

# Routes
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.htm', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        db = get_db()
        user = db.execute('SELECT id, username, password FROM users WHERE username = ?', (username,)).fetchone()
        db.close()
        
        if user:
            if check_password_hash(user[2], password):
                session['user_id'] = user[0]
                session['username'] = user[1]
                return jsonify({'success': True, 'redirect': url_for('index')})
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Missing credentials'}), 400
    
    hashed_pw = generate_password_hash(password)
    db = get_db()
    
    try:
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_pw))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Account created successfully'}), 201
    except sqlite3.IntegrityError:
        db.close()
        return jsonify({'error': 'Username already exists'}), 409

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET'])
def show_signup():
    return render_template('signup.htm')

@app.route('/login', methods=['GET'])
def show_login():
    return render_template('login.htm')

@app.route('/index', methods=['GET'])
def show_index():
    return render_template('index.htm')

@app.route('/playlist')
def playlist():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('playlist.htm')

@app.route('/createplaylist')
def favorites():
    return render_template('create_playlist.htm')

@app.route('/taylor-swift')
def taylor_swift():
    return render_template('twsongs.htm')

@app.route('/ed-sheeran')
def ed_sheeran():
    return render_template('essongs.htm')

@app.route('/sidsriram')
def sidsriram():
    return render_template('sidsriramsongs.htm')

@app.route('/kpopsongs')
def kpopsongs():
    return render_template('kpopsongs.htm')

@app.route('/jbsongs')
def jbsongs():
    return render_template('jbsongs.htm')

@app.route('/sonusongs')
def sonusongs():
    return render_template('sonusongs.htm')

@app.route('/arjithsongs')
def arjithsongs():
    return render_template('arjithsongs.htm')

@app.route('/shreyasongs')
def shreyasongs():
    return render_template('shreyasongs.htm')

@app.route('/arrahmansongs')
def arrahmansongs():
    return render_template('arrahmansongs.htm')

@app.route('/charlie-puth')
def charlie_puth():
    return render_template('cpsongs.htm')

@app.route('/anirudh')
def anirudh():
    return render_template('anirudhsongs.htm')

@app.route('/hiphop-tamizha')
def hiphop_tamizha():
    return render_template('hhtsongs.htm')

@app.route('/happy')
def happy():
    return render_template('happy.htm')

@app.route('/broken')
def broken():
    return render_template('broken.htm')

@app.route('/romantic')
def romantic():
    return render_template('romantic.htm')

@app.route('/vibey')
def vibey():
    return render_template('vibey.htm')

@app.route('/english')
def english():
    return render_template('english.htm')

@app.route('/hindi')
def hindi():
    return render_template('hindi.htm')

@app.route('/tamil')
def tamil():
    return render_template('tamil.htm')

@app.route('/telugu')
def telugu():
    return render_template('telugu.htm')

@app.route('/create-playlist')
def show_create_playlist():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('create_playlist.htm')

@app.route('/about/charlie-puth')
def about_charlie():
    return render_template('abtcharlie.htm')

@app.route('/about/taylor-swift')
def about_taylor():
    return render_template('abttaylor.htm')

@app.route('/about/ed-sheeran')
def about_edsheeran():
    return render_template('abtedsheeran.htm')

@app.route('/about/anirudh')
def about_anirudh():
    return render_template('abtanirudh.htm')

@app.route('/about/hiphop-tamizha')
def about_hiphop():
    return render_template('abthht.htm')

@app.route('/about/arrahman')
def about_arrahman():
    return render_template('abtrahman.htm')

@app.route('/about/sidsriram')
def about_sidsriram():
    return render_template('abtsidsriram.htm')

@app.route('/about/shreya')
def about_shreya():
    return render_template('abtshreya.htm')

@app.route('/about/arjith')
def about_arjith():
    return render_template('abtarjith.htm')

@app.route('/about/justin')
def about_justin():
    return render_template('abtjustin.htm')

@app.route('/about/jkpop')
def about_bts():
    return render_template('abtbts.htm')

@app.route('/about/blackpink')
def about_bp():
    return render_template('abtbp.htm')

@app.route('/about/txt')
def about_txt():
    return render_template('abttxt.htm')

@app.route('/about/sonu')
def about_sonu():
    return render_template('abtsonu.htm')


@app.route('/get_songs')
def get_songs():
    db = get_db()
    songs = db.execute('SELECT id, title FROM songs').fetchall()
    db.close()
    return jsonify([{'id': song[0], 'title': song[1]} for song in songs])

@app.route('/get_playlists')
def get_playlists():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Not logged in'}), 401
    
    db = get_db()
    playlists = db.execute('SELECT id, name FROM playlists WHERE user_id = ?', (user_id,)).fetchall()
    db.close()
    return jsonify([{'id': playlist[0], 'name': playlist[1]} for playlist in playlists])


    

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    data = request.get_json()
    playlist_name = data.get('playlist_name')
    user_id = session.get('user_id')

    if not playlist_name or not user_id:
        return jsonify({'success': False, 'error': 'Missing data'}), 400

    db = get_db()
    try:
        db.execute('INSERT INTO playlists (name, user_id) VALUES (?, ?)', (playlist_name, user_id))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Playlist created successfully'})
    except sqlite3.IntegrityError:
        db.close()
        return jsonify({'success': False, 'error': 'Playlist already exists'}), 409

@app.route('/get_playlists_with_songs')
def get_playlists_with_songs():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Not logged in'}), 401

    db = get_db()
    
    # Fetch playlists for the user
    playlists = db.execute('''
        SELECT id, name FROM playlists WHERE user_id = ?
    ''', (user_id,)).fetchall()

    # Fetch songs for each playlist
    playlists_with_songs = []
    for playlist in playlists:
        playlist_id = playlist[0]
        songs = db.execute('''
            SELECT s.id, s.title, s.artist 
            FROM songs s
            JOIN playlist_songs ps ON s.id = ps.song_id
            WHERE ps.playlist_id = ?
        ''', (playlist_id,)).fetchall()

        playlists_with_songs.append({
            'id': playlist_id,
            'name': playlist[1],
            'songs': [{'id': song[0], 'title': song[1], 'artist': song[2]} for song in songs]
        })

    db.close()
    return jsonify(playlists_with_songs)

@app.route('/get_ed_sheeran_songs')
def get_ed_sheeran_songs():
    db = get_db()
    songs = db.execute('SELECT id, title FROM songs WHERE artist = ?', ('Ed Sheeran',)).fetchall()
    db.close()
    return jsonify([{'id': song[0], 'title': song[1]} for song in songs])


@app.route('/add_song_to_playlist', methods=['POST'])
def add_song_to_playlist():
    data = request.get_json()
    playlist_id = data.get('playlist_id')
    song_id = data.get('song_id')
    
    if not playlist_id or not song_id:
        return jsonify({'success': False, 'error': 'Missing data'}), 400
    
    db = get_db()
    try:
        # Debug: Log the received data
        print(f"Received request to add song_id={song_id} to playlist_id={playlist_id}")

        # Check if the song is already in the playlist
        existing = db.execute('''
            SELECT * FROM playlist_songs 
            WHERE playlist_id = ? AND song_id = ?
        ''', (playlist_id, song_id)).fetchone()

        if existing:
            # Debug: Log that the song is already in the playlist
            print(f"Song {song_id} is already in playlist {playlist_id}")
            db.close()
            return jsonify({'success': False, 'error': 'Song already in playlist'}), 409

        # Insert the song into the playlist
        db.execute('''
            INSERT INTO playlist_songs (playlist_id, song_id) 
            VALUES (?, ?)
        ''', (playlist_id, song_id))
        db.commit()
        db.close()
        # Debug: Log successful addition
        print(f"Song {song_id} added to playlist {playlist_id} successfully")
        return jsonify({'success': True, 'message': 'Song added to playlist successfully'})
    except Exception as e:
        # Debug: Log any exceptions
        print(f"Error adding song to playlist: {e}")
        db.close()
        return jsonify({'success': False, 'error': str(e)}), 500
    
@app.route('/remove_song_from_playlist', methods=['POST'])
def remove_song_from_playlist():
    data = request.get_json()
    playlist_id = data.get('playlist_id')
    song_id = data.get('song_id')
    
    if not playlist_id or not song_id:
        return jsonify({'success': False, 'error': 'Missing data'}), 400
    
    db = get_db()
    try:
        # Check if the song exists in the playlist
        existing = db.execute('''
            SELECT * FROM playlist_songs 
            WHERE playlist_id = ? AND song_id = ?
        ''', (playlist_id, song_id)).fetchone()

        if not existing:
            db.close()
            return jsonify({'success': False, 'error': 'Song not found in playlist'}), 404

        # Delete the song from the playlist
        db.execute('''
            DELETE FROM playlist_songs 
            WHERE playlist_id = ? AND song_id = ?
        ''', (playlist_id, song_id))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Song removed from playlist successfully'})
    except Exception as e:
        db.close()
        return jsonify({'success': False, 'error': str(e)}), 500
    
@app.route('/update_playlist_name', methods=['POST'])
def update_playlist_name():
    data = request.get_json()
    playlist_id = data.get('playlist_id')
    new_name = data.get('new_name')
    
    if not playlist_id or not new_name:
        return jsonify({'success': False, 'error': 'Missing data'}), 400
    
    db = get_db()
    try:
        # Update the playlist name
        db.execute('''
            UPDATE playlists 
            SET name = ? 
            WHERE id = ?
        ''', (new_name, playlist_id))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Playlist name updated successfully'})
    except Exception as e:
        db.close()
        return jsonify({'success': False, 'error': str(e)}), 500
    
@app.route('/delete_playlist', methods=['POST'])
def delete_playlist():
    data = request.get_json()
    playlist_id = data.get('playlist_id')
    
    if not playlist_id:
        return jsonify({'success': False, 'error': 'Missing data'}), 400
    
    db = get_db()
    try:
        # Delete the playlist and its associated songs
        db.execute('DELETE FROM playlist_songs WHERE playlist_id = ?', (playlist_id,))
        db.execute('DELETE FROM playlists WHERE id = ?', (playlist_id,))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Playlist deleted successfully'})
    except Exception as e:
        db.close()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/play-song/<int:song_id>')
def play_song(song_id):
    db = get_db()
    
    # Set row factory to access columns by name
    db.row_factory = sqlite3.Row
    
    song = db.execute('SELECT * FROM songs WHERE id = ?', (song_id,)).fetchone()
    db.close()
    
    if not song:
        return render_template('error.htm', message='Song not found'), 404
    
    return render_template('play-song.htm',
                         song_title=song['title'],
                         artist=song['artist'],
                         file_path=url_for('static', filename=song['file_path']))

def get_db():
    db = sqlite3.connect('project.db')
    db.row_factory = sqlite3.Row  # Add this line
    return db

if __name__ == '__main__':
    app.run(debug=True)