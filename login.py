users = {
    "admin": "1234"
}

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful.")
        return True

    print("Invalid username or password.")
    return False