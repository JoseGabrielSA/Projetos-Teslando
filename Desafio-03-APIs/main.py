# Bibliotecas
import requests
import csv
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
email_remetente = os.getenv("EMAIL_REMETENTE")
email_senha_app = os.getenv("EMAIL_SENHA")
email_destinatario = os.getenv("EMAIL_DESTINATARIO")

API_URL = "https://reqres.in/api/users" 
# Função para buscar os usuários da API
def get_users():

    pagina = 1 # -> variavel de controle das paginas
    usuarios = []

    while True:
        resposta_api = requests.get(API_URL, params={"page": pagina})
        dados = resposta_api.json()
        # adicionando dentro da lista
        usuarios.extend(dados["data"])
        # verifica se existe mais uma pagina
        if pagina >= dados["total_pages"]:
            break

        pagina += 1

    print("\nUsuários Obtidos com Sucesso!\n")

    return usuarios, resposta_api
'''
200 -> SUCESSO
300 -> REDIRECIONAMENTO
400 -> ERRO DO CLIENTE
500 -> ERRO NO SERVIDOR
'''
# Função para salvar os usuários em um arquivo CSV
def save_users_csv(usuarios):
    with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        campos = ["id", "email", "first_name", "last_name", "avatar"]

        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

        escritor.writeheader() # -> Escreve o nome das colunas
        escritor.writerows(usuarios) # -> Escreve várias linhas onde os usuários vão preenchê-las
        print("\nArquivo usuarios.csv criado com sucesso!\n")
# Função enviar e-mail
def send_email():
    mensagem = EmailMessage() # -> cria o objeto que representa o e-mail
    # remetente
    mensagem["From"] = email_remetente
    # destinatário
    mensagem["To"] = email_destinatario
    # título
    mensagem["Subject"] = "Usuários da API ReqRes"
    # mensagem
    mensagem.set_content("Olá! Segue em anexo o arquivo com os usuários obtidos da API ReqRes.")

    with open("usuarios.csv", "rb") as arquivo:
        dados_arquivo = arquivo.read()
    # anexo no e-mail:
    mensagem.add_attachment(
    dados_arquivo,
    maintype="text",
    subtype="csv",
    filename="usuarios.csv"
)
    # add no servidor SMTP do Gmail:
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls() # iniciando uma comunicação segura com o servidor
        servidor.login(email_remetente, email_senha_app)
        servidor.send_message(mensagem)
        print("\nE-mail enviado com sucesso!\n")

usuarios, resposta_api = get_users()
save_users_csv(usuarios)
send_email()