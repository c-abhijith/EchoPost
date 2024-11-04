from flask import Blueprint, jsonify

# Create a blueprint instance
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login endpoint"})

@auth.route('/register', methods=['POST'])
def register():
    return jsonify({"message": "Registration endpoint"})
