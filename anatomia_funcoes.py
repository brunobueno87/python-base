"""\
Este modulo serve apenas de anotação.
"""

# definição ou atribuição
# assinatura + type hints
# documentação / docstring
# codigo
# valor de retorno

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

valor = nome_da_funcao(1, 2, 3)
print(valor)
