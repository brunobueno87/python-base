#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "brunobueno87@gmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Pyton"
TEXT = """\
Este é meu e-mail enviado pelo Python
"""

mensage = f"""\
From: {FROM}
To: {", ".join(TO)}
subject: {SUBJECT}

{TEXT} 
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, mensage.encode("utf-8"))
