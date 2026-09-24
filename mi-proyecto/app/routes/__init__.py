from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def inicio():
    return render_template("clientes/index.html")


@main_bp.route("/nosotros")
def nosotros():
    return render_template("clientes/nosotros.html")


@main_bp.route("/conoce-matahuasi")
def conoce_matahuasi():
    return render_template("clientes/conoce.html")


@main_bp.route("/productos")
def productos():
    return render_template("clientes/productos.html")


@main_bp.route("/contactos")
def contactos():
    return render_template("clientes/contactos.html")


@main_bp.route("/compra")
def compra():
    return render_template("clientes/compra.html")

@main_bp.route("/usuarios")
def usuarios():
    from app.database import get_connection

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id, nombre, correo FROM usuarios ORDER BY id DESC")
    usuarios = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "conexion": "MySQL OK",
        "usuarios": usuarios
    }


@main_bp.route("/usuarios/registrar", methods=["POST"])
def registrar_usuario():
    from flask import request
    from app.database import get_connection

    datos = request.get_json()

    nombre = datos.get("nombre")
    correo = datos.get("correo")

    if not nombre or not correo:
        return {
            "error": "nombre y correo son obligatorios"
        }, 400

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)",
        (nombre, correo)
    )

    connection.commit()

    nuevo_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return {
        "mensaje": "Usuario registrado correctamente",
        "id": nuevo_id,
        "nombre": nombre,
        "correo": correo
    }, 201


@main_bp.route("/contactos/registrar", methods=["POST"])
def registrar_contacto():
    from flask import request
    from app.database import get_connection

    datos = request.get_json(silent=True) or {}

    nombre = str(datos.get("nombre") or "").strip()
    correo = str(datos.get("correo") or "").strip()
    telefono = str(datos.get("telefono") or "").strip()
    motivo = str(datos.get("motivo") or "").strip()
    mensaje = str(datos.get("mensaje") or "").strip()

    if not all([nombre, correo, motivo, mensaje]):
        return {"error": "Completa todos los campos obligatorios."}, 400

    if (len(nombre) > 100 or len(correo) > 150
            or len(telefono) > 30 or len(motivo) > 200):
        return {"error": "Uno de los campos supera el límite permitido."}, 400

    conexion = None
    cursor = None

    try:
        conexion = get_connection()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO contactos
                (nombre, correo, telefono, motivo, mensaje)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nombre, correo, telefono, motivo, mensaje)
        )

        conexion.commit()

        return {
            "mensaje": "Tu mensaje se registró correctamente.",
            "id": cursor.lastrowid
        }, 201

    except Exception:
        return {"error": "No se pudo guardar el mensaje."}, 500

    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()
