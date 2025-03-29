users_db = {
    "user1": {"username": "user1", "password": "password123"},
    "admin": {"username": "admin", "password": "adminpass"}
    
}

def authenticate(username, password):
    user = users_db.get(username)
    if user and user["password"] == password:
        return True
    return False
