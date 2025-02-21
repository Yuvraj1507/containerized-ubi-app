from flask import Blueprint, jsonify
from models.base import db
from models.health import HealthCheck

health_blueprint = Blueprint("health", __name__)

# Health Check Endpoint
@health_blueprint.route("/", methods=["GET"])
def check_health():
    health_entry = HealthCheck(status="healthy")
    db.session.add(health_entry)
    db.session.commit()
    
    return jsonify({
        "status": "healthy",
        "checked_at": health_entry.checked_at.strftime("%Y-%m-%d %H:%M:%S")
    }), 200
