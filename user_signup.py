import json
import hashlib

with open("db.json") as db:
    users: dict = json.loads(db.read())


def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_input(input_string):
    return " " not in input_string

def register():
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty!")
        return

    if not is_valid_input(username):
        print("Username can't contain spaces!")
        return
    
    if not is_valid_input(password):
        print("Password can't contain spaces!")
        return
    
    if username in users:
        print("Username already exists! Try another.")
    else:
        users[username] = hash_password(password)
        print("User registered successfully!")
        with open("db.json", "w") as db:
            json.dump(users, db, indent=4)

def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if not is_valid_input(username):
        print("Invalid username: spaces are not allowed!")
        return
    
    if not is_valid_input(password):
        print("Invalid password: spaces are not allowed!")
        return

    if username in users and users[username] == hash_password(password):
        print("Login successful!")
    else:
        print("Invalid username or password!")
