#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.1"

sala1 = {
    "aluno1": "Erik", 
    "aluno2": "Maia",
    "aluno3": "Gustavo",
    "aluno4": "Manuel",
    "aluno5": "Sofia",
    "aluno6": "Joana",
}

sala2 = {
    "aluno1": "Joao",
    "aluno2": "Antonio",
    "aluno3": "Carlos", 
    "aluno4": "Maria",
    "aluno5": "Isolda",
}

aula_ingles = {
    "Erik", "Maria", "Joana", "Carlos", "Antonio"],
    "aula_musica": ["Erik", "Carlos", "Maria"],
    "aula_danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}


atividades = [("Inglês", {aulas['aula_ingles'][0]}), 
              ("Música", {aulas['aula_musica'][0]}), 
              ("Dança", {aulas['aula_danca'][0]}),
              ]


#for nome_atividade, atividade in atividades:

#    print(f"Alunos da atividade {nome_atividade}\n")
#    print("-" * 50)

#    atividade_sala1 = set(sala1) & set(atividade)
#    atividade_sala2 = set(sala2) & set(atividade)

#    print(f" sala1 ", atividade_sala1)
#    print(f" sala2 ", atividade_sala2)
#    print()
#    print("#" * 50)
