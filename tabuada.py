#!/usr/bin/env python3
"""Programinha de tabuada"""
__version__ = "0.1.1"
__author__ = "Bruno Bueno"
__license__ = "Unlicense"

template = """
---Tabuada do ---

{bloco:^18}

##################   
"""

numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))

    print("#" * 18)
