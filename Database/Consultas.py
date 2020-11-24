from Database.Conexion import run_query

def login_db(username, password):
    query = """SELECT COUNT(IDALUMNO) AS CANTIDAD FROM ALUMNOS
        WHERE NOMBRE_USUARIO = '%s' 
        AND CONTRASEÑA = '%s';""" % (username, password)
    
    try:
        result = run_query(query) 
        
        if result[0][0] > 0:
            response = {
                "exito": True,
                "mensaje": "Solicitud ejecutada con éxito.",
                "resultado": ""
            }
        else:
            response = {
                "exito": False,
                "mensaje": "Nombre de usuario o contraseña incorrectos.",
                "resultado": ""
            }
    except:
        response = {
            "exito": False,
            "mensaje": "Ocurrió un problema al ejecutar la solicitud. Intente de nuevo",
            "resultado": ""
        }
    
    return response

def obtener_datos_de_usuario_db(username):
    query = """SELECT A.NOMBRE_USUARIO, A.CORREO_ELECTRONICO, U.NOMBRE, U.APELLIDO, U.FECHA_NACIMIENTO, U.SEXO, U.PAIS  FROM ALUMNOS A
        INNER JOIN USUARIOS U
        ON A.IDALUMNO = U.IDUSUARIO
        WHERE A.NOMBRE_USUARIO = '%s';""" % (username)
    
    try:
        result = run_query(query)
    
        if len(result) > 0:
            result = result[0]
            response = {
                "exito": True,
                "mensaje": "Solicitud ejecutada con éxito.",
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
                "mensaje": "No se encontró el nombre de usuario buscado.",
                "resultado": []
            }
    except:
        response = {
            "exito": False,
            "mensaje": "Ocurrió un problema al ejecutar la solicitud. Intente de nuevo",
            "resultado": ""
        }

    return response

def obtener_calificaciones_db(username):
    lista_calificaciones = []
    query = """SELECT C.NOMBRE, AC.PUNTOS, A.NOMBRE_USUARIO FROM ALUMNOS A
        INNER JOIN ALUMNOSCURSOS AC
        ON AC.IDALUMNO = A.IDALUMNO
        INNER JOIN CURSOS C
        ON C.IDCURSO = AC.IDCURSO
        WHERE A.NOMBRE_USUARIO = '%s';""" % (username)
    
    try:
        result = run_query(query)
        lista_calificaciones = [{"nombre_curso": r[0], "puntos": r[1], "nombre_usuario": r[2]} for r in result]

        if len(result) > 0:
            response = {
                "exito": True,
                "mensaje": "Solicitud ejecutada con éxito.",
                "resultado": lista_calificaciones
            }
        else:
            response = {
                "exito": False,
                "mensaje": "No se encontró el nombre de usuario buscado.",
                "resultado": []
            }
    except:
        response = {
            "exito": False,
            "mensaje": "Ocurrió un problema al ejecutar la solicitud. Intente de nuevo",
            "resultado": ""
        }

    return response

def obtener_calificaciones_por_curso_db(username, nombre_curso):
    query = """SELECT C.NOMBRE, AC.PUNTOS, A.NOMBRE_USUARIO FROM ALUMNOS A
        INNER JOIN ALUMNOSCURSOS AC
        ON AC.IDALUMNO = A.IDALUMNO
        INNER JOIN CURSOS C
        ON C.IDCURSO = AC.IDCURSO
        WHERE A.NOMBRE_USUARIO = '%s' AND C.NOMBRE = '%s';""" % (username, nombre_curso)
    
    try:
        result = run_query(query)
        
        if len(result) > 0:
            result = result[0]
            response = {
                "exito": True,
                "mensaje": "Solicitud ejecutada con éxito.",
                "resultado": {
                    "nombre_curso": result[0], 
                    "puntos": result[1], 
                    "nombre_usuario": result[2]
                }
            }
        else:
            response = {
                "exito": False,
                "mensaje": "No se encontró el nombre de usuario o curso buscado.",
                "resultado": []
            }
    except:
        response = {
            "exito": False,
            "mensaje": "Ocurrió un problema al ejecutar la solicitud. Intente de nuevo",
            "resultado": ""
        }

    return response

def actualizar_puntaje_curso_db(username, nombre_curso, puntaje):
    if puntaje.isnumeric():
        puntaje = int(puntaje)
    else:
        return {
            "exito": False,
            "mensaje": "El puntaje debe ser un número entero positivo",
            "resultado": ""
        }

    query = """UPDATE ALUMNOSCURSOS AC
            INNER JOIN ALUMNOS A
            ON AC.IDALUMNO = A.IDALUMNO
            INNER JOIN CURSOS C
            ON C.IDCURSO = AC.IDCURSO
            SET AC.PUNTOS = AC.PUNTOS + %i
            WHERE A.NOMBRE_USUARIO = '%s' AND C.NOMBRE = '%s';""" % (puntaje, username, nombre_curso)
    
    query_usuario = """SELECT * FROM ALUMNOS
            WHERE NOMBRE_USUARIO = '%s'""" % (username)
    
    query_curso = """SELECT * FROM CURSOS
            WHERE NOMBRE = '%s'""" % (nombre_curso)
    
    try:
        result_usuario = run_query(query_usuario)
        result_curso = run_query(query_curso)


        if len(result_usuario) > 0 and len(result_curso) > 0:
            result = run_query(query)
            
            response = {
                "exito": True,
                "mensaje": "Solicitud ejecutada con éxito.",
                "resultado": ""
            }
        else:
            response = {
                "exito": False,
                "mensaje": "No se encontró el nombre de usuario o curso buscado.",
                "resultado": ""
            }
    except:
        response = {
            "exito": False,
            "mensaje": "Ocurrió un problema al ejecutar la solicitud. Intente de nuevo",
            "resultado": ""
        }

    return response

def obtener_pruebas_por_curso_db(nombre_curso):
    lista_pruebas = []
    query = """SELECT P.PREGUNTA, P.RESPUESTA_CORRECTA, P.RESPUESTA_INCORRECTA, C.NOMBRE FROM PRUEBAS P
        INNER JOIN CURSOS C
        ON C.IDCURSO = P.IDCURSO
        WHERE C.NOMBRE = '%s';""" % (nombre_curso)
    
    try:
        result = run_query(query)
        lista_pruebas = [{"pregunta": r[0], "respuesta_correcta": r[1], "respuesta_incorrecta": r[2], "nombre_curso": r[2]} for r in result]

        if len(result) > 0:
            response = {
                "exito": True,
                "mensaje": "Solicitud ejecutada con éxito.",
                "resultado": lista_pruebas
            }
        else:
            response = {
                "exito": False,
                "mensaje": "No se encontró el curso buscado.",
                "resultado": []
            }
    except:
        response = {
            "exito": False,
            "mensaje": "Ocurrió un problema al ejecutar la solicitud. Intente de nuevo",
            "resultado": ""
        }

    return response

