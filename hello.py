#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Tenha a variável LANG devidamente configurada ex:

    export LANG=en_US.UTF-8

Execução:

    python3 hello.py
    ou
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Bruno Bueno"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)

