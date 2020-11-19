from flask import Flask, render_template, request, jsonify
from hashlib import sha512
from Clases.Usuario import Usuario
from Database.Consultas import loginDb, getUserDataDb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.json['username']
    contrasena = request.json['password']
    #contrasena = sha512(str(request.json['password']).encode()).hexdigest()
    response_db = loginDb(usuario, contrasena)

    return jsonify(response_db)

@app.route('/usuario/<nombre_usuario>/')
def second(nombre_usuario):
    response_db = getUserDataDb(nombre_usuario)
    return jsonify(response_db)
    

if __name__ == "__main__":
    app.run(debug=True)