from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'static/uploads'

    from .routes import main
    app.register_blueprint(main)

    return app
