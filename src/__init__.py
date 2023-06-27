from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "randomshit"

    from .views import views
    app.register_blueprint(views)

    return app