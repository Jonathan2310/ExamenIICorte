import ply.yacc as yacc
from analizadorLexico import tokens, lexer

# Manejamos una lista de variables declaradas
declaraciones = {}

def p_programa(p):
    '''programa : declaraciones DO instrucciones ENDDO WHILE PARENTESIS_IZQ condicion PARENTESIS_DER ENDWHILE'''
    pass

def p_declaraciones(p):
    '''declaraciones : declaracion
                     | declaracion declaraciones'''
    pass

def p_declaracion(p):
    '''declaracion : tipo IDENTIFICADOR IGUAL NUMERO PUNTOYCOMA'''
    declaraciones[p[2]] = p[1]  # Assuming p[1] is the type
    pass

def p_instrucciones(p):
    '''instrucciones : instruccion
                     | instruccion instrucciones'''
    pass

def p_instruccion(p):
    '''instruccion : IDENTIFICADOR IGUAL expresion PUNTOYCOMA'''
    if p[1] not in declaraciones:
        errores.append(f"Error: Variable '{p[1]}' no declarada en la línea {p.lineno(1)}")
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
    if isinstance(p[1], str) and p[1] not in declaraciones:
        errores.append(f"Error: Variable '{p[1]}' no declarada en la línea {p.lineno(1)}")
    pass

def p_condicion(p):
    '''condicion : tipo IDENTIFICADOR IGUAL_IGUAL NUMERO'''
    if p[2] not in declaraciones:
        errores.append(f"Error: Variable '{p[2]}' no declarada en la línea {p.lineno(2)}")
    if p[1] != 'int':
        errores.append(f"Error: Tipo '{p[1]}' no válido para variable '{p[2]}' en la línea {p.lineno(2)}")
    pass

def p_tipo(p):
    '''tipo : INT'''
    p[0] = p[1]

def p_error(p):
    if p:
        errores.append(f"Syntax error '{p.value}', linea {p.lineno}")
    else:
        errores.append("Syntax error at EOF")

# Construir el parser
parser = yacc.yacc()

# Función para analizar la semántica
def analizar_semantica(codigo):
    global declaraciones, errores
    declaraciones = {}
    errores = []
    lexer.input(codigo)
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type not in tokens:
            errores.append(f"Error: Palabra reservada mal escrita '{tok.value}' en la línea {tok.lineno}")

    try:
        parser.parse(codigo, tracking=True)
    except Exception as e:
        errores.append(str(e))

    if not errores:
        errores.append("Análisis semántico correcto")

    return errores
