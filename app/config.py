import os

class Config:
    # Flask App Config
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("DEBUG", False)

    # Database Config (PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydatabase")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security & Authentication
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_jwt_secret")

    # Monitoring & Logging
    PROMETHEUS_METRICS = os.getenv("PROMETHEUS_METRICS", True)

    # Other Configs
    CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "*")
