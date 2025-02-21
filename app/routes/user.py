from flask import Blueprint, request, jsonify
from models.base import db
from models.user import User

user_blueprint = Blueprint("user", __name__)

# Get all users
@user_blueprint.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Create a new user
@user_blueprint.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "username" not in data or "email" not in data or "password" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_user = User(username=data["username"], email=data["email"], password_hash=data["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201
