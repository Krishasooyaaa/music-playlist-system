from pyscript import document, display, js
import json

api_url = "http://127.0.0.1:5000"  # Flask Backend URL

def save_playlist():
    """Send playlist name to the Flask API without songs"""
    playlist_name = document.querySelector("#playlistName").value
    if not playlist_name:
        js.alert("Please enter a playlist name")
        return

    data = {
        "playlist_name": playlist_name,
        "song_ids": []  # Empty array since we're only creating the name
    }

    js.fetch(f"{api_url}/create_playlist", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data)
    }).then(
        lambda response: response.json()
    ).then(
        lambda result: handle_response(result)
    ).catch(
        lambda error: handle_error(error)
    )

def handle_response(result):
    """Handle the response from the server"""
    if result.get("success"):
        js.alert("Playlist Created Successfully!")
        js.window.location.replace("playlist.htm")  # Redirect to playlists page
    else:
        js.alert(f"Error: {result.get('error', 'Unknown error')}")

def handle_error(error):
    """Handle any fetch errors"""
    js.console.error("Fetch error:", error)
    js.alert("An error occurred while creating the playlist.")