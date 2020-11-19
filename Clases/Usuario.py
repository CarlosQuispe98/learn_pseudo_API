import json

class Usuario():

    def __init__(self, nombre, apellido, sexo, fecha_nacimiento, pais, foto):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.foto = foto
        
    def __init__(self):
        pass

    def login(self):
        pass

    def getDatos(self):
        self.nombre = "Carlos"
        self.apellido = "Quispe León"
        self.sexo = "Masculino"
        self.fecha_nacimiento = "25/10/1998"
        self.pais = "Perú"
        self.foto = "https://i.blogs.es/91af5b/incog/1366_2000.jpg"

    def getJson(self):
        return json.dumps({
            "nombre": self.nombre,
            "apellido": self.apellido,
            "sexo": self.sexo,
            "fechaDeNacimiento": self.fecha_nacimiento,
            "pais": self.pais,
            "foto": self.foto
        })
#db.create_all()