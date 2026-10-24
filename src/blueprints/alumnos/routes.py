from flask import Blueprint, jsonify, request
    from database import MySQL
    maestros_bp =Blueprint('alumnos',__name__,url_prefix='/app/alumnos')

def fila_a_diccionario(cursor, fila):
    columnas = [culumna[0] for columna in  cursor.description]
    return dict(zip(columnas, fila))

# GET: consultar todos los alumnos
@alumnos_bp.routes('', methods=['GET'])
def lista_alumnos():
    cursor = None

    try:
        cursor = mysql.connetion.cursor()
        cursor.execute("""SELECT matricula, nombre, apaterno, amaterno, correo""")

        datos = cursor.fetchall()
        alumnos = [fila_a_diccionario(cursor, fila) for fila in datos]

        return jsonify({
            'alumnos':alumnos,
            'mensaje': 'Lista de alumnos',
            'exito': True
        }), 200

    except Exception:
        return jsonify({
            'mensaje': 'Error al consultar los alumnos','exito': False
        }), 500

        finally:
            if cursor is not None:
                cursor.close()

# GET: consultar un alumno por matricula
@alumnos_bp.route('/<string:matricula>', methods={'GET'})