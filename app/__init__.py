from flask import Flask

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Registrar rutas
    with app.app_context():
        from app import routes
        return app
