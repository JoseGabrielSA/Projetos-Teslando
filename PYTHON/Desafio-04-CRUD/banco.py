import psycopg # -> biblioteca que conversa com meu banco
import os
from dotenv import load_dotenv

load_dotenv()

SENHA_BANCO = os.getenv("SENHA")


def conectar():

    conexao = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="gestao_tarefas",
        user="postgres",
        password=SENHA_BANCO
    )

    return conexao