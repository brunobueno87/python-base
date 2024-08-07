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

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])

