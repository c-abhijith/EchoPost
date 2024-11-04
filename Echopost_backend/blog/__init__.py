from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register the auth blueprint
    from .routes.auth import auth  # Ensure you're importing the correct blueprint
    app.register_blueprint(auth)  # This should register the blueprint correctly

    return app
