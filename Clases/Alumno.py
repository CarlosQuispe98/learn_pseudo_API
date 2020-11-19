import json
from Usuario import Usuario

class Alumno(Usuario):

    def __init__(self, nombre, apellido, nombre_usuario, correo_electronico, contrasena, sexo, fecha_nacimiento, pais, foto):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo_electronico = correo_electronico
        Usuario.__init__(self, nombre, apellido, sexo, fecha_nacimiento, pais, foto)
        
    def __init__(self):
        pass

    def login(self):
        pass

    def getDatos(self):
        self.nombre = "Carlos"
        self.apellido = "Quispe León"
        self.nombre_usuario = "carlosql2598"
        self.sexo = "Masculino"
        self.fecha_nacimiento = "25/10/1998"
        self.pais = "Perú"
        self.foto = "https://i.blogs.es/91af5b/incog/1366_2000.jpg"

    def getJson(self):
        return json.dumps({
            "nombre": self.nombre,
            "apellido": self.apellido,
            "nombreDeUsuario": self.nombre_usuario,
            "sexo": self.sexo,
            "fechaDeNacimiento": self.fecha_nacimiento,
            "pais": self.pais,
            "foto": self.foto
        })