from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
# 🔹 Función para conectar con la base de datos
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          
        password="",          
        database="hotel_reservas"
    )
    return conn

# 🔹 Ruta principal
@app.route('/')
def index():
    return "<h2>Bienvenido al sistema de reservas del hotel</h2><ul>" \
           "<li><a href='/habitaciones'>Ver Habitaciones</a></li>" \
           "<li><a href='/clientes'>Ver Clientes</a></li>" \
           "<li><a href='/reservas'>Ver Reservas</a></li></ul>"

# 🔹 Mostrar habitaciones
@app.route('/habitaciones')
def mostrar_habitaciones():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM habitaciones")
    habitaciones = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("habitaciones.html", habitaciones=habitaciones)

# 🔹 Mostrar clientes
@app.route('/clientes')
def mostrar_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("clientes.html", clientes=clientes)

# 🔹 Mostrar reservas
@app.route('/reservas')
def mostrar_reservas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.id_reserva, c.nombre, c.apellido, h.numero_habitacion, 
               r.fecha_ingreso, r.fecha_salida, r.estado
        FROM reservas r
        JOIN clientes c ON r.id_cliente = c.id_cliente
        JOIN habitaciones h ON r.id_habitacion = h.id_habitacion
    """)
    reservas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("reservas.html", reservas=reservas)

if __name__ == "_main_":
    app.run(debug=True)

