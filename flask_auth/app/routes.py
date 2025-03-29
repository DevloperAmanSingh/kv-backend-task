from flask import Blueprint, request, jsonify
from app.models import authenticate

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    if authenticate(username, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
