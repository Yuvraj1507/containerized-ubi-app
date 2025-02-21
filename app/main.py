from flask import Flask, jsonify
from routes.user import user_blueprint
from routes.health import health_blueprint
from config import Config
from models.base import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Register Blueprints (API Routes)
app.register_blueprint(user_blueprint, url_prefix="/api/users")
app.register_blueprint(health_blueprint, url_prefix="/api/health")

# Root Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Containerized App with Red Hat UBI!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
