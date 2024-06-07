import re

def analizar_codigo(codigo):
    reservadas = ["package", "import", "func"]
    operadores = ["+", "=", "*", "/", "-", "."]
    parentesis_abre = ["("]
    parentesis_cierra = [")"]
    llaves_abre = ["{"]
    llaves_cierra = ["}"]
    comillas_dobles = ["\""]
    punto_y_coma = [";"]
    identificadores = []
    numeros = re.compile(r'\b\d+\b')

    tokens_totales = []
    lineas = codigo.split("\n")

    for num_linea, linea in enumerate(lineas, start=1):
        tokens_linea = []

        # Buscar palabras reservadas
        for token in reservadas:
            matches = re.findall(r"\b{}\b".format(token), linea)
            for match in matches:
                tokens_linea.append((num_linea, match, "Palabra reservada"))

        # Buscar operadores
        for token in operadores:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Operador"))

        # Buscar paréntesis izquierdos
        for token in parentesis_abre:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Paréntesis izquierdo"))

        # Buscar paréntesis derechos
        for token in parentesis_cierra:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Paréntesis derecho"))

        # Buscar llaves izquierdas
        for token in llaves_abre:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Llave izquierda"))

        # Buscar llaves derechas
        for token in llaves_cierra:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Llave derecha"))

        # Buscar comillas dobles
        for token in comillas_dobles:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Comillas dobles"))

        # Buscar punto y coma
        for token in punto_y_coma:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Punto y coma"))

        # Buscar números
        matches = numeros.findall(linea)
        for match in matches:
            tokens_linea.append((num_linea, match, "Número"))

        # Buscar identificadores y clasificarlos correctamente
        identificadores_en_linea = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", linea)
        for identificador in identificadores_en_linea:
            if identificador in reservadas:
                tokens_linea.append((num_linea, identificador, "Palabra reservada"))
            else:
                tokens_linea.append((num_linea, identificador, "Identificador"))

        tokens_totales.extend(tokens_linea)
    
    return tokens_totales

codigo_go = '''
package main

import "fmt"

func main() {
    fmt.Println("Hola Mundo")
}
'''

tokens = analizar_codigo(codigo_go)
for token in tokens:
    print(token)
