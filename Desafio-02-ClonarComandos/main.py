"""
🚀 [Desafio 02] Aplicacao pratica - Clone de Comandos SimplesObjetivo: 
utilizar funcoes basicas da linguagem python para clonar simples comandos do terminal (ls, cat, echo, tee), tais comandos focados em loops e manipulacao de arquivos ou diretorios.

2. Pontuação Final:
    - Baseado no quao proximo o script implementa a funcionalidade padrao do comando, + robustes ou opcoes adicionais.
"""
# Bibliotecas utilizadas:
import os
import shutil

while True: 

    entrada = input("Digite um comando: ").strip() # --> remover espaços em branco

    if not entrada: # --> se a entrada estiver vazia, repita a pergunta
        continue

    partes = entrada.split()
    comando = partes[0]
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
# comando para imprimir uma mensagem na tela
    elif comando == "echo":
        # texto
        mensagem = " ".join(partes[1:])
        print(mensagem)

        continue
# comando para criar um arquivo e escrever conteudo nele
    elif comando == "tee":

        nome_arquivo_tee = input("Digite o nome do arquivo: ")
        conteudo = input("Digite o conteúdo a ser escrito no arquivo: ")

        with open(nome_arquivo_tee, 'w') as file:
            file.write(conteudo)

        print(conteudo)

        continue
#   -----------------------------
#       COMANDOS ADICIONAIS
#   -----------------------------
# comando para criar um diretório
    elif comando == "mkdir":

        nome_diretorio = input("Digite o nome do diretório: ")

        if not os.path.exists(nome_diretorio): # se o diretório não existir, cria um diretório
            os.makedirs(nome_diretorio)
            print(f"Diretório '{nome_diretorio}' criado com sucesso.")
        else:
            print("Diretório já existe.")

        continue
# comando para criar um arquivo vazio
    elif comando == "touch":

        nome_arquivo_touch = input("Digite o nome do arquivo: ")

        if not os.path.isfile(nome_arquivo_touch): # se o arquivo não existir, cria um arquivo vazio
            with open(nome_arquivo_touch, 'w') as file:
                pass

        else:
            print("Arquivo já existe.")

        continue
# comando para excluir um arquivo
    elif comando == "rm":

        nome_arquivo_rm = input("Digite o nome do arquivo para excluir: ")

        if os.path.isfile(nome_arquivo_rm):
            os.remove(nome_arquivo_rm) 
            print(f"Arquivo '{nome_arquivo_rm}' excluído com sucesso.")
        else:
            print("Arquivo não encontrado.")

        continue
# comando para excluir um diretório VAZIO
    elif comando == "rmdir":

        nome_diretorio_rmdir = input("Digite o nome do diretório para excluir: ")
        if os.path.isdir(nome_diretorio_rmdir): # se o diretório existir, exclui o diretório
            try: # tente excluir o diretório, se não estiver vazio, exibe uma mensagem de erro
                os.rmdir(nome_diretorio_rmdir)
                print(f"Diretório '{nome_diretorio_rmdir}' excluído com sucesso.")
            except OSError: # exceção caso o diretório não esteja vazio
                print("Diretório não está vazio.")
        else:
            print("Diretório não encontrado.")

        continue
# comando para mover ou renomear um arquivo ou diretório
    elif comando == "mv":

        origem = input("Digite o nome do arquivo ou diretório de origem: ")
        destino = input("Digite o caminho ou nome de destino: ")
        if os.path.exists(origem):
            try:
                shutil.move(origem, destino)
                print(f"Arquivo ou diretório '{origem}' movido para '{destino}'.")

            except OSError as erro: # exceção caso não seja possível mover o arquivo ou diretório
                print(f"Não foi possível mover: {erro}") 
        else:
            print("Arquivo ou diretório de origem não encontrado.")

        continue
# comando para encerrar o programa
    elif comando == "exit":

        break

    else:

        print("Comando não reconhecido.")