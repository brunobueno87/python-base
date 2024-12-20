"""\
Este modulo serve apenas de anotação.
"""

# definição ou atribuição
# assinatura + type hints
# documentação / docstring
# codigo
# valor de retorno

# - parametros
# posicional - passados em ordem

def nome_da_funcao(a: int, b: int, c: int) -> int:
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    qunado o parametro a tiver o valor 10
    vai acontecer x.

    >>> nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

# passagem de argumentos posicionais
valor = nome_da_funcao(1, 2, 3)

# passagem de argumentos nomeados
valor = nome_da_funcao(a=1, b=2, c=3)
valor = nome_da_funcao(c=1, b=2, a=3)
valor = nome_da_funcao(b=1, a=2, c=3)

# passagem de argumentos mista
# argumentos posicionais antes dos nomeados
valor = nome_da_funcao(1, 2, c=3)
valor = nome_da_funcao(1, c=2, b=3)

#valor com muitos argumentos
valor = nome_da_funcao(
    a=1, 
    c=2, 
    b=3
)

print(valor)


###################################################

def outra_funcao(a, b, c):
    """Explica o que ela faz"""
    return a * 2, b * 2, c * 2

outro_valor = outra_funcao(1, 2, 3)
print(outro_valor)

valor1, *resto = outra_funcao(1, 2, 3)
print(valor1)
print(resto)

###################################################

# Passagem de argumentos com desempacotamento

def soma(n1, n2):
    """Faz a soma de 2 numeros"""
    return n1 + n2

print(soma(10, 20))

args = (20, 30)
print(soma(args[0], args[1]))

###################################################

