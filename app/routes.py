from flask import Blueprint, render_template

# Crear un Blueprint para las rutas principales
main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("home.html", title="Hola Mundo")

# Registrar el Blueprint
from flask import current_app as app
app.register_blueprint(main)
