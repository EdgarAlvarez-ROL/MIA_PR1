import ply.lex as lex

# Lista de tokens
tokens = (
    'ASSIGNMENT',
    'IDENTIFIER',
    'STRING',
)

# Regla para el operador de asignación "="
def t_ASSIGNMENT(t):
    r'-[a-zA-Z]+=[a-zA-Z0-9_]+'
    return t

# Regla para identificadores (cualquier secuencia de letras y números)
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

# Regla para cadenas de texto (encerradas entre comillas)
def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]  # Eliminar las comillas alrededor de la cadena
    return t

# Regla para manejar espacios en blanco y nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para ignorar espacios y tabulaciones
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)



# Construir el lexer
lexer = lex.lex()

# Ejemplo de uso
data = "-name=ejemplo -city=Nueva_York -age=30 -country=\"Estados Unidos\""

lexer.input(data)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
