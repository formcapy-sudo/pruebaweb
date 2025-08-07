from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configura tu conexión
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ee349145',
    'database': 'tienda'
}

@app.route('/')
def mostrar_productos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('tabla.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
