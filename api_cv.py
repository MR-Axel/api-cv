#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvenido a la API del curriculum vitae de Axel Rosso.",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)


@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/FotoAxel.jpg"
    cv = {
        "nombre" : "Axel",
        "apellido" : "Rosso",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "< describe tu posición>",
            "empresa" : "< nombre de tu empresa >",
            "desde" : "< cuándo empezaste a trabajar >",
            "hasta" : "< si ya no trabajas más, cuándo >",
            "descripcion" : "< detalles >"
        }],
        "educación" : {
            "nivel" : "< nivel de tus estudios >",
            "titulo" : "< nombre de tu carrera >",
            "institucion" : "< dónde estudiaste >",
            "facultad" : "< más detalles >"
        },
        "intereses" : ["python", "apis", "enseñar"],
        "redes" : {
            "github" : "https://github.com/MR-Axel",
            "linkedin" : "https://www.linkedin.com/in/axelrosso/"
        },
        "foto" : url_imagen
    }
    return jsonify(cv)


@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()

    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")

    print("MENSAJE DE CONTACTO: " + str(mensaje))
    return "Gracias por su mensaje."


if __name__ == "__main__":
    app.run()