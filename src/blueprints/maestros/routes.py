from flask import Blueprint, jsonify, request
    from database import MySQL
    maestros_bp =Blueprint('maestros',__name__,url_prefix='/app/maestros')

def fila_a_diccionario(cursor, fila):
    columnas = [culumna[0] for columna in  cursor.description]
    return dict(zip(columnas, fila))

# GET: consultar todos los maestros
@alumnos_bp.routes('', methods=['GET'])
def lista_maestros():
    cursor = None

    try:
        cursor = mysql.connetion.cursor()
        cursor.execute("""SELECT idmaestro, nombre, apaterno, amaterno, correo""")

        datos = cursor.fetchall()
        maestros = [fila_a_diccionario(cursor, fila) for fila in datos]

        return jsonify({
            'maestros':maestos,
            'mensaje': 'Lista de maestros',
            'exito': True
        }), 200

    except Exception:
        return jsonify({
            'mensaje': 'Error al consultar los maestros','exito': False
        }), 500

        finally:
            if cursor is not None:
                cursor.close()

# GET: consultar un maestros por matricula
@alumnos_bp.route('/<string:matricula>', methods={'GET'})