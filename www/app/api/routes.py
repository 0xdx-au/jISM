from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/controls', methods=['GET'])
def get_controls():
    # Placeholder for fetching controls
    return jsonify({"message": "List of controls"})
