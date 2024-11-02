import connexion
from flask import jsonify, request, abort

# Datos simulados para películas
PELICULAS = {
    1: {
        "id": 1,
        "titulo": "Toy Story 4",
        "director": "Josh Cooley",
        "descripcion": "Woody, Buzz Lightyear y el resto de los juguetes viven felices con su nueva dueña Bonnie, hasta que un nuevo juguete, Forky, se une al grupo y comienzan una nueva aventura.",
        "estreno": True,
        "genero": "Animación",
        "esAnimada": True,
        "fechaEstreno": "2019-06-21",
        "urlVideo": "https://www.youtube.com/watch?v=wmiIUN-7qhE"
    }
}
NEXT_PELICULA_ID = max(PELICULAS.keys()) + 1 if PELICULAS else 1

def get_all_peliculas():
    """Obtener todas las películas."""
    return jsonify(list(PELICULAS.values())), 200

def get_pelicula(id):
    """Obtener una película por ID."""
    pelicula = PELICULAS.get(id)
    if pelicula:
        return jsonify(pelicula), 200
    else:
        abort(404, description=f"Película con ID {id} no encontrada")

def add_pelicula():
    """Agregar una nueva película."""
    global NEXT_PELICULA_ID
    data = request.get_json()
    
    # Validar campos obligatorios
    if not all(key in data for key in ["titulo", "director", "descripcion", "genero", "fechaEstreno"]):
        abort(400, description="Faltan datos necesarios para crear la película")

    nueva_pelicula = {
        "id": NEXT_PELICULA_ID,
        "titulo": data["titulo"],
        "director": data["director"],
        "descripcion": data["descripcion"],
        "estreno": data.get("estreno", False),
        "genero": data["genero"],
        "esAnimada": data.get("esAnimada", False),
        "fechaEstreno": data["fechaEstreno"],
        "urlVideo": data.get("urlVideo", "")
    }

    PELICULAS[NEXT_PELICULA_ID] = nueva_pelicula
    NEXT_PELICULA_ID += 1

    return jsonify(nueva_pelicula), 201

def delete_pelicula(id):
    """Eliminar una película por ID."""
    if id in PELICULAS:
        del PELICULAS[id]
        return jsonify({"mensaje": f"Película con ID {id} eliminada"}), 200
    else:
        abort(404, description=f"Película con ID {id} no encontrada")

def update_pelicula(id):
    """Actualizar los datos de una película por ID."""
    if id not in PELICULAS:
        abort(404, description=f"Película con ID {id} no encontrada")

    data = request.get_json()

    # Validar que los campos necesarios están presentes
    if not all(key in data for key in ["titulo", "director", "descripcion", "genero", "fechaEstreno"]):
        abort(400, description="Faltan datos necesarios para actualizar la película")

    # Actualizar los datos de la película
    pelicula = PELICULAS[id]
    pelicula["titulo"] = data.get("titulo", pelicula["titulo"])
    pelicula["director"] = data.get("director", pelicula["director"])
    pelicula["descripcion"] = data.get("descripcion", pelicula["descripcion"])
    pelicula["estreno"] = data.get("estreno", pelicula["estreno"])
    pelicula["genero"] = data.get("genero", pelicula["genero"])
    pelicula["esAnimada"] = data.get("esAnimada", pelicula["esAnimada"])
    pelicula["fechaEstreno"] = data.get("fechaEstreno", pelicula["fechaEstreno"])
    pelicula["urlVideo"] = data.get("urlVideo", pelicula["urlVideo"])

    return jsonify(pelicula), 200

# Crear la aplicación Flask + Connexion
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
