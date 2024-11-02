from flask import Flask, render_template
from flask_cors import CORS  # Importar CORS
import connexion  # Importar Connexion para integrar Swagger

# Crear la aplicación Connexion
app = connexion.App(__name__, specification_dir="./")

# Obtener la aplicación Flask subyacente
flask_app = app.app

# Habilitar CORS en todas las rutas y orígenes
CORS(flask_app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Agregar la API Swagger desde el archivo swagger.yml
app.add_api("swagger.yml")

# Definir la ruta para el home
@flask_app.route("/")
def home():
    return render_template("home.html")  # Asegúrate de tener este archivo en la carpeta templates/

# Ejecutar el servidor con Uvicorn
if __name__ == "__main__":
    import uvicorn
    # Escuchar solo en localhost
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
