import ply.yacc as yacc
from analizadorLexico import tokens, lexer

# Reglas
def p_programa(p):
    '''programa : declaraciones DO instrucciones ENDDO WHILE PARENTESIS_IZQ condicion PARENTESIS_DER ENDWHILE'''
    if reservedWords.index('DO') >= reservedWords.index('ENDDO') or \
       reservedWords.index('ENDDO') >= reservedWords.index('WHILE') or \
       reservedWords.index('WHILE') >= reservedWords.index('ENDWHILE'):
        raise SyntaxError(f"Error de orden en las palabras reservadas: {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]} {p[8]} {p[9]}")
    pass

def p_declaraciones(p):
    '''declaraciones : declaracion
                     | declaracion declaraciones'''
    pass

def p_declaracion(p):
    '''declaracion : INT IDENTIFICADOR IGUAL NUMERO PUNTOYCOMA'''
    pass

def p_instrucciones(p):
    '''instrucciones : instruccion
                     | instruccion instrucciones'''
    pass

def p_instruccion(p):
    '''instruccion : IDENTIFICADOR IGUAL expresion PUNTOYCOMA'''
    pass

def p_expresion(p):
    '''expresion : termino
                 | termino MAS expresion'''
    pass

def p_termino(p):
    '''termino : factor
               | factor ASTERISCO termino'''
    pass

def p_factor(p):
    '''factor : NUMERO
              | IDENTIFICADOR'''
    pass

def p_condicion(p):
    '''condicion : INT IDENTIFICADOR IGUAL_IGUAL NUMERO'''
    pass

def p_error(p):
    raise SyntaxError(f"Syntax error '{p.value}', linea {p.lineno}")

# Construir el parser
parser = yacc.yacc()

# Función para analizar la sintaxis
def analizar_sintaxis(codigo):
    errores = []
    lexer.input(codigo)
    
    while True:
        tok = lexer.token()
        if not tok:
            break

    try:
        parser.parse(codigo, tracking=True)
    except Exception as e:
        errores.append(str(e))

    return errores if errores else ["Sintaxis correcta"]

# Lista de palabras reservadas en el orden requerido
reservedWords = ['INT', 'DO', 'ENDDO', 'WHILE', 'ENDWHILE']
