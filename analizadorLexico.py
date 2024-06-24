import ply.lex as lex

# Definir las palabras reservadas
reserved = {
    'int': 'INT',
    'DO': 'DO',
    'ENDDO': 'ENDDO',
    'WHILE': 'WHILE',
    'ENDWHILE': 'ENDWHILE'
}

# Lista de tokens
tokens = [
    'NUMERO', 'IDENTIFICADOR',
    'IGUAL', 'MAS', 'PUNTOYCOMA',
    'PARENTESIS_IZQ', 'PARENTESIS_DER',
    'ASTERISCO', 'IGUAL_IGUAL'
] + list(reserved.values())

# Expresiones regulares para tokens simples
t_IGUAL = r'='
t_MAS = r'\+'
t_PUNTOYCOMA = r';'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_ASTERISCO = r'\*'
t_IGUAL_IGUAL = r'=='

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definir reglas para tokens complejos
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejar nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función para analizar el código
def analizar_codigo(codigo):
    lexer.input(codigo)
    tokens = []
    counts = {
        'tokens': 0,
        'palabras_reservadas': 0,
        'ids': 0,
        'simbolos': 0
    }
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.lineno, tok.value, tok.type))
        counts['tokens'] += 1
        if tok.type in reserved.values():
            counts['palabras_reservadas'] += 1
        elif tok.type == 'IDENTIFICADOR':
            counts['ids'] += 1
        else:
            counts['simbolos'] += 1
    return tokens, counts

# Ejemplo de uso
if __name__ == "__main__":
    codigo = """
    int a=0;
    int b=10;
    int c=0;
    DO 
        a=3*b;
        c=2+a;
    ENDDO
    WHILE (int x==2)
    ENDWHILE
    """

    tokens, counts = analizar_codigo(codigo)
    for token in tokens:
        print(token)
    print(f"Counts: {counts}")
