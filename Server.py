from flask import Flask, render_template, request, jsonify
#from Clases.Usuario import Usuario
from Database.Consultas import *
from hashlib import sha256

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.json['username']
    contrasena = request.json['password']
    contrasena = sha256(str(contrasena).encode()).hexdigest()
    response_db = login_db(usuario, contrasena)

    return jsonify(response_db)

@app.route('/usuario/<nombre_usuario>/')
def datos_usuario(nombre_usuario):
    response_db = obtener_datos_de_usuario_db(nombre_usuario)
    return jsonify(response_db)

@app.route('/calificaciones/<nombre_usuario>/')
def todas_calificaciones(nombre_usuario):
    response_db = obtener_calificaciones_db(nombre_usuario)
    return jsonify(response_db)

@app.route('/calificaciones_por_curso/<nombre_usuario>/<nombre_curso>')
def calificaciones_por_curso(nombre_usuario, nombre_curso):
    response_db = obtener_calificaciones_por_curso_db(nombre_usuario, nombre_curso)
    return jsonify(response_db)

@app.route('/actualizar_puntos_curso/<nombre_usuario>/<nombre_curso>/<puntaje>', methods=['PUT'])
def actualizar_puntos_curso(nombre_usuario, nombre_curso, puntaje):
    response_db = actualizar_puntaje_curso_db(nombre_usuario, nombre_curso, puntaje)
    return jsonify(response_db)

@app.route('/pruebas_curso/<nombre_curso>')
def pruebas_por_curso(nombre_curso):
    response_db = obtener_pruebas_por_curso_db(nombre_curso)
    return jsonify(response_db)
    

if __name__ == "__main__":
    app.run(debug=True)