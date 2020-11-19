from Database.Conexion import run_query

def loginDb(username, password):
    query = """SELECT COUNT(IDALUMNO) AS CANTIDAD FROM ALUMNOS
        WHERE NOMBRE_USUARIO = '%s' 
        AND CONTRASEÑA = '%s';""" % (username, password)
    
    result = run_query(query) 
    
    if result[0][0] > 0:
        response = {
            "exito": True,
            "resultado": ""
        }
    else:
        response = {
            "exito": False,
            "resultado": ""
        }
    
    return response

def getUserDataDb(username):
    query = """SELECT A.NOMBRE_USUARIO, A.CORREO_ELECTRONICO, U.NOMBRE, U.APELLIDO, U.FECHA_NACIMIENTO, U.SEXO, U.PAIS  FROM ALUMNOS A
        INNER JOIN USUARIOS U
        ON A.IDALUMNO = U.IDUSUARIO
        WHERE A.NOMBRE_USUARIO = '%s';""" % (username)
    
    result = run_query(query)
    
    if len(result) > 0:
        result = run_query(query)[0]
        response = {
            "exito": True,
            "resultado": {
                "nombre_usuario": result[0],
                "correo": result[1],
                "nombre": result[2],
                "apellido": result[3],
                "fecha_nacimiento": result[4],
                "sexo": result[5],
                "pais": result[6],
            }
        }
    else:
        response = {
            "exito": False,
            "resultado": []
        }
    return response