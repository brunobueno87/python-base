import sys
import time

"""Exemplo de Backoff exponencial, util para retentativas de erro.
   Para testar crie (ou não) um arquivo no mesmo path com uma lista de nomes.
"""

max_retries = 5  # Máximo de tentativas
attempt = 0  # Contador de tentativas
while attempt < max_retries:
    try:
        names = open("names.txt").readlines()
    except FileNotFoundError:
        print(f"Nova tentativa, aguarde uns segundos")
        attempt += 1
        wait_time = 2 ** attempt  # Backoff exponencial
        time.sleep(wait_time)
        print("Error tratado")
    else:
        attempt += 1
        wait_time = 2 ** attempt  # Backoff exponencial
        time.sleep(wait_time)
        print(names)
