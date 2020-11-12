#from Database import DataBaseLearnCode
import json

class Usuario():
    def __init__(self, nombre, apellido, nombre_usuario, contrasena, sexo, fecha_nacimiento, pais, foto):
        self._nombre = nombre
        self._apellido = apellido
        self._nombre_usuario = nombre_usuario
        self._contrasena = contrasena
        self._sexo = sexo
        self._fecha_nacimiento = fecha_nacimiento
        self._pais = pais
        self._foto = foto
        
    def __init__(self):
        pass

    def login(self):
        pass

    def getDatos(self):
        self._nombre = "Carlos"
        self._apellido = "Quispe León"
        self._nombre_usuario = "carlosql2598"
        self._sexo = "Masculino"
        self._fecha_nacimiento = "25/10/1998"
        self._pais = "Perú"
        self._foto = "https://i.blogs.es/91af5b/incog/1366_2000.jpg"

    def getJson(self):
        return json.dumps({
            "nombre": self._nombre,
            "apellido": self._apellido,
            "nombreDeUsuario": self._nombre_usuario,
            "sexo": self._sexo,
            "fechaDeNacimiento": self._fecha_nacimiento,
            "pais": self._pais,
            "foto": self._foto
        })