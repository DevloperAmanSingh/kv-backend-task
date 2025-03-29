users_db = {
    "user1": {"username": "user1", "password": "password123"},
    "admin": {"username": "admin", "password": "adminpass"}
}

def authenticate(username: str, password: str) -> bool:
    user = users_db.get(username)
    return user and user["password"] == password
