from pyscript import Element
import hashlib
import sqlite3
import js  # Required for proper redirects in PyScript

def encrypt_password(password):
    """Encrypts the password using SHA256 hashing."""
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    """Handles user login process with proper validation and error handling."""
    # Get input values
    username = Element("login-username").value.strip()
    password = Element("login-password").value.strip()
    
    # Clear previous messages
    Element("login-error").write("")
    Element("login-success").write("")

    # Basic client-side validation
    if not username or not password:
        Element("login-error").write("Please fill in all fields!", color="red")
        return

    try:
        # Database connection
        with sqlite3.connect('project.db') as db:
            cursor = db.cursor()
            
            # Parameterized query to prevent SQL injection
            cursor.execute(
                "SELECT password FROM users WHERE username = ?", 
                (username,)
            )
            result = cursor.fetchone()

            if result:
                stored_hash = result[0]
                if stored_hash == encrypt_password(password):
                    # Successful login
                    Element("login-success").write(
                        "Login successful! Redirecting...", 
                        color="green"
                    )
                    # Redirect after short delay
                    js.setTimeout(lambda: js.window.location.replace("index.htm"), 1500)
                else:
                    Element("login-error").write(
                        "Incorrect password! Try again.", 
                        color="red"
                    )
            else:
                Element("login-error").write(
                    "Username not found! Please sign up first.", 
                    color="red"
                )
                
    except sqlite3.Error as err:
        Element("login-error").write(
            f"Database error: {err}", 
            color="red"
        )
    except Exception as e:
        Element("login-error").write(
            f"Unexpected error: {str(e)}", 
            color="red"
        )