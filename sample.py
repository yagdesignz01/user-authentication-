import json
import hashlib
import os

try:
    with open("db.json") as db:
        users : dict = json.loads(db.read())
except (FileNotFoundError, json.JSONDecodeError):
    users = {}

def hash_password(password):
    #hashing the password for security using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_input(input_string):
    #Validates that input contains no spaces
    return " " not in input_string

def save_users():
    #saves the users dictioonary to the JSON file
    if users:
        with open("db.json", "w") as db:
            json.dump(users, db, indent=4)

def register():
    username = input("Enter a username (no spaces allowed): ").strip()
    password = input("Enter a password (no spaces allowed): ").strip()

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
        save_users()
    
#login form for users
def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if not is_valid_input(username):
        print("Invalid username: spaces are not allowed!")
        return
    
    if not is_valid_input(password):
        print("Invalid password: spaces are not allowed!")
        return
    
    if username in users:
        if users[username] == hash_password(password):
            print("Login successful!")
        else:
            print("Incorrect password!")
    else:
        print("Username does not exist!")
