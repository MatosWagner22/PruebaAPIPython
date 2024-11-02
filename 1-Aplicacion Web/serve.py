from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'VinlandSagaDB'

mysql = MySQL(app)

# Ruta principal para mostrar solo el formulario
@app.route('/')
def index():
    return render_template('create.html')

# Ruta para manejar la solicitud POST del formulario y responder en JSON
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            # Obtén los datos del formulario
            personaje = request.form.get('personaje')
            tierra_favorita = request.form.get('tierra')
            aliado = request.form.get('compañero')
            armas = ','.join(request.form.getlist('tecnicas'))
            actividades = ','.join(request.form.getlist('actividades'))
            aventura = request.form.get('aventura')
            fecha_inicio = request.form.get('fecha')
            
            # Conecta a la base de datos y ejecuta la inserción
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO VinlandSagaFormulario (personaje, tierra_favorita, aliado, armas, actividades, aventura, fecha_inicio) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (personaje, tierra_favorita, aliado, armas, actividades, aventura, fecha_inicio))
            
            mysql.connection.commit()
            cursor.close()
            
            # Responder con éxito en formato JSON
            return jsonify(success=True, message="Datos guardados exitosamente.")
        
        except Exception as e:
            print(f"Error: {e}")
            # Responder con un error en formato JSON
            return jsonify(success=False, message="Error al guardar los datos.")

# Nueva ruta para mostrar los datos registrados en una tabla
@app.route('/datos')
def datos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM VinlandSagaFormulario")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', vinland_data=data)

if __name__ == "__main__":
    app.run(debug=True)
