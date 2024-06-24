from flask import Flask, request, jsonify
from flask_cors import CORS
import analizadorLexico
import analizadorSintactico
import analizadorSemantico

app = Flask(__name__)
CORS(app)

@app.route('/lexico', methods=['POST'])
def lexico():
    data = request.get_json()
    codigo = data.get('textarea_content', '')
    tokens, counts = analizadorLexico.analizar_codigo(codigo)
    return jsonify({'tokens': tokens, 'counts': counts})

@app.route('/sintactico', methods=['POST'])
def sintactico():
    data = request.get_json()
    codigo = data.get('textarea_content', '')
    errores = analizadorSintactico.analizar_sintaxis(codigo)
    return jsonify({'errores': errores})

@app.route('/semantico', methods=['POST'])
def semantico():
    data = request.get_json()
    codigo = data.get('textarea_content', '')
    errores = analizadorSemantico.analizar_semantica(codigo)
    return jsonify({'errores': errores})

if __name__ == '__main__':
    app.run(debug=True)
