from app import create_app

# Crear la aplicación utilizando la fábrica
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
