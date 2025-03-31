from pyscript import document

# Function to add a song to the playlist
def add_song():
    song_name = document.querySelector("#song-name").value.strip()
    error_message = document.querySelector("#error-message")
    playlist = document.querySelector("#playlist")

    if song_name == "":
        error_message.innerText = "Please enter a song name!"
        return

    # Create a new list item
    new_song = document.createElement("li")
    new_song.classList.add("song-item")

    # Create a span for the song name
    song_text = document.createElement("span")
    song_text.innerText = song_name

    # Create delete button
    delete_btn = document.createElement("button")
    delete_btn.innerText = "X"
    delete_btn.classList.add("delete-btn")
    
    # Function to remove the song
    def delete_song(event):
        playlist.removeChild(new_song)

    # Bind the delete function
    delete_btn.addEventListener("click", delete_song)

    # Append elements
    new_song.appendChild(song_text)
    new_song.appendChild(delete_btn)
    playlist.appendChild(new_song)

    # Clear input field and error message
    document.querySelector("#song-name").value = ""
    error_message.innerText = ""