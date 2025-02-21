from flask import request, jsonify
from functools import wraps
from services.jwt import JWTService

def token_required(f):
    """Decorator to protect routes with JWT authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        token = token.split(" ")[1] if " " in token else token  # Handle 'Bearer <token>' format

        decoded = JWTService.decode_token(token)
        if "error" in decoded:
            return jsonify(decoded), 401

        return f(*args, **kwargs)

    return decorated_function
