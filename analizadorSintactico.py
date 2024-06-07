import re

def analizar_sintaxis(codigo):
    lineas = codigo.split("\n")
    errores = []
    pila_llaves = []

    # Lista de palabras reservadas y componentes clave en Go
    palabras_reservadas = ["package", "import", "func", "main", "fmt", "Println"]
    operadores = ["+", "=", "*", "/", "-", "."]
    simbolos = ["(", ")", "{", "}", "\""]

    for num_linea, linea in enumerate(lineas, start=1):
        stripped_linea = linea.strip()

        # Verificar saltos de línea y espacios en blanco
        if not stripped_linea:
            continue

        # Verificar comillas dobles balanceadas
        if stripped_linea.count('"') % 2 != 0:
            errores.append((num_linea, stripped_linea, "Error: comillas desbalanceadas"))
            continue

        # Verificar paréntesis balanceados
        if stripped_linea.count('(') != stripped_linea.count(')'):
            errores.append((num_linea, stripped_linea, "Error: paréntesis desbalanceados"))
            continue

        # Verificar llaves balanceadas
        for char in stripped_linea:
            if char == '{':
                pila_llaves.append('{')
            elif char == '}':
                if pila_llaves and pila_llaves[-1] == '{':
                    pila_llaves.pop()
                else:
                    errores.append((num_linea, stripped_linea, "Error sintáctico: llave de cierre '}' sin llave de apertura correspondiente"))

        # Extraer y omitir cadenas literales para análisis de palabras reservadas
        stripped_linea_sin_cadenas = stripped_linea
        cadenas = re.findall(r'"[^"]*"', stripped_linea)
        for cadena in cadenas:
            stripped_linea_sin_cadenas = stripped_linea_sin_cadenas.replace(cadena, '""')

        # Verificar palabra por palabra
        palabras = re.findall(r'\b\w+\b', stripped_linea_sin_cadenas)
        for palabra in palabras:
            if palabra not in palabras_reservadas and not any(op in palabra for op in operadores) and palabra not in simbolos:
                errores.append((num_linea, stripped_linea, f"Error sintáctico: '{palabra}' mal escrita o inesperada"))

        # Verificar la estructura completa de la línea
        if re.match(r'^package\s+main$', stripped_linea):
            continue
        elif re.match(r'^import\s+"fmt"$', stripped_linea):
            continue
        elif re.match(r'^func\s+main\(\)\s+\{', stripped_linea):
            continue
        elif re.match(r'^fmt\.Println\(".*"\)$', stripped_linea):
            continue
        elif re.match(r'^\}$', stripped_linea):
            continue
        else:
            errores.append((num_linea, stripped_linea, "Error sintáctico: estructura de línea incorrecta"))

    if pila_llaves:
        errores.append((num_linea, "", "Error sintáctico: llave de apertura '{' sin llave de cierre correspondiente"))

    if errores:
        return errores
    else:
        return "Sintaxis correcta"
