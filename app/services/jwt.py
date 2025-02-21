import jwt
import datetime
import os

SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")

class JWTService:
    @staticmethod
    def generate_token(user_id: int, expires_in: int = 3600) -> str:
        """Generates a JWT token for a user."""
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in),
            "iat": datetime.datetime.utcnow()
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    @staticmethod
    def decode_token(token: str):
        """Decodes a JWT token and returns the payload."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}
