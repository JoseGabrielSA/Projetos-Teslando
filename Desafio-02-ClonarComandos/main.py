"""
🚀 [Desafio 02] Aplicacao pratica - Clone de Comandos SimplesObjetivo: 
utilizar funcoes basicas da linguagem python para clonar simples comandos do terminal (ls, cat, echo, tee), tais comandos focados em loops e manipulacao de arquivos ou diretorios.

2. Pontuação Final:
    - Baseado no quao proximo o script implementa a funcionalidade padrao do comando, + robustes ou opcoes adicionais.
"""
import os

while True:

    entrada = input("Digite um comando: ").strip() # --> remover espaços em branco

    if not entrada: # --> se a entrada estiver vazia, repetir a pergunta
        continue

    partes = entrada.split()
    comando = partes[0]
    # dicionario para armazenar variaveis do usuario
    variaveis = {}
    # se o comando estiver vazio, repetir a pergunta
#   -----------------------------
#       COMANDOS DO DESAFIO
#   -----------------------------
# comando para listar arquivos e diretorios    
    if comando == "ls":

        for arquivo in os.listdir():
            print(arquivo)

        continue
# comando para exibir o conteudo de um arquivo
    elif comando == "cat":

        nome_arquivo = input("Digite o nome do arquivo: ")

        if os.path.isfile(nome_arquivo):

            with open(nome_arquivo, 'r') as file:
                print(file.read())

        else:
            print("Arquivo não encontrado.")

        continue
# comando para imprimir uma mensagem na tela ou declarar variaveis
    elif comando == "echo":
        # texto
        mensagem = " ".join(partes[1:])
        print(mensagem)
        # variaveis
#   -----------------------------
#       COMANDOS ADICIONAIS
#   -----------------------------
# comando para criar um arquivo vazio
    elif comando == "touch":

        nome_arquivo = input("Digite o nome do arquivo: ")

        if not os.path.isfile(nome_arquivo):

            with open(nome_arquivo, 'w') as file:
                pass

        else:
            print("Arquivo já existe.")

        continue
# comando parar o programa
    elif comando == "exit":

        break

    else:

        print("Comando não reconhecido.")