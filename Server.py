from flask import Flask, render_template, request, jsonify
from hashlib import sha512
from UsuarioClase import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    datos = {
        "nombres": "Carlos Alberto",
        "apellidos": "Quispe Leon",
        "edad": 22,
        "sexo": "Masculino"
    }

    return jsonify(datos)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.json['username']
    contrasena = request.json['password']
    #contrasena = sha512(str(request.json['password']).encode()).hexdigest()

    if usuario == 'carlosql2598' and contrasena == '12345678':
        usuario = Usuario()
        usuario.getDatos()
        
        server_response = {
            "exito": True,
            "resultado": usuario.getJson()
        }
    else:
        server_response = {
            "exito": False,
            "resultado": ""
        }

    return jsonify(server_response)

#@app.route('/second/<nombre>/')
#def second(nombre):
#    return render_template("second.html", nombre=nombre)
    

if __name__ == "__main__":
    app.run(debug=True)