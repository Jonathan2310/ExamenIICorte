from flask import Flask, request, jsonify
from flask_cors import CORS
import analizadorLexico
import analizadorSintactico
import logging

app = Flask(__name__)
CORS(app)
app.secret_key = 'clavee22'
logging.basicConfig(level=logging.DEBUG)

@app.route('/lexico', methods=['POST'])
def analisis_lexico():
    data = request.json
    codigo = data.get('textarea_content', '')

    tokens = analizadorLexico.analizar_codigo(codigo)

    return jsonify({'tokens': tokens})

@app.route('/sintactico', methods=['POST'])
def analisis_sintactico():
    try:
        data = request.json
        codigo = data.get('textarea_content', '')

        errores = analizadorSintactico.analizar_sintaxis(codigo)

        return jsonify({'sintactico': errores})
    except Exception as e:
        logging.error(f"Error en el análisis sintáctico: {e}")
        return jsonify({'error': 'Ocurrió un error en el servidor'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)

