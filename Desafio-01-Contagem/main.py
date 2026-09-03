# 🚀 [Desafio 01] Desenvolvimento de um Script em Python para Contagem com IncrementoO objetivo deste desafio é 
# construir um script em Python que permita ao usuário realizar uma contagem a partir de um número inicial até um número final, 
# somando um valor de incremento a cada iteração. Siga as especificações abaixo para completar o desafio:

# 1. Especificações Gerais:
#     - O script deve ser executado via linha de comando e não requer interface gráfica.
#     - O usuário deverá fornecer três números como entrada: número inicial, número final e incremento.
#     - O script realizará uma contagem a partir do número inicial até o número final, somando o valor do incremento.

while True: # --> While True loop para garantir que o usuário digite valores válidos
    try: # --> oq o usuário escreveu e tente treansformar em um número inteiro: 
        # Declarando as variáveis de entrada do usuário:
        inicio = int(input("Digite o valor inicial: "))
        fim = int(input("Digite o valor final: "))
        passos = int(input("Digite o valor do passo: "))
#       -------------------------
#         Validação das entradas 
#       -------------------------        
        # Validação do passo se for 0:
        if passos == 0:
            print("O valor do passo não pode ser zero.")
            continue
        # Validação do passo se for descrescente e o valor do passo for positivo:
        elif inicio > fim and passos > 0:
            print("Para contagem decrescente, o valor do passo deve ser negativo.")
            continue
        # Validação do passo se for crescente e o valor do passo for negativo:
        elif inicio < fim and passos < 0:
            print("Para contagem crescente, o valor do passo deve ser positivo.")
            continue
        # Limite entre os intervalos de contagem:
        elif abs(inicio - fim)>1000:
            print("O intervalo entre o valor inicial e final é muito grande. Por favor, digite valores mais próximos.")
            continue
        break

# Exceção para caso o usuário digite um valor que não seja inteiro:
    except ValueError:
        print("Digite apenas números inteiros.")

#-----------------------
#   SAIDA DO TERMINAL
#-----------------------
# Calculo da contagem com base nas entradas do usuário:
#--> decrescente:
if inicio > fim and passos < 0: #--> se obedecer a condição de contagem decrescente, o loop será executado

    for i in range(inicio, fim-1, passos):
        print(i)
#--> crescente:
elif inicio < fim and passos > 0: # --> se obedecer a condição de contagem crescente, o loop será executado

    for i in range(inicio, fim+1, passos):
        print(i)
#--> igualdade:
elif inicio == fim:

    print("O valor inicial e final são iguais. Não há contagem a ser feita.")