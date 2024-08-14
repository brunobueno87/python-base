#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Tenha a variável LANG devidamente configurada ex:

    export LANG=en_US.UTF-8

Ou informe atraves do CLI arguments `--lang`

Ou o usuario tera que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Bruno Bueno"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Optiond {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input ("Choose a language:")

current_language = current_language[:5]

msg = {
   "en_US": "Hello, World!",
   "pt_BR": "Olá, Mundo!",
   "it_IT": "Ciao, Mondo!",
   "es_ES": "Hola, Mundo!",
   "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))
