import bcrypt

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password using bcrypt."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """Verifies a password against a stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
