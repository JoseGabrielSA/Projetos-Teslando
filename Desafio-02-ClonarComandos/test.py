#print("teste em python com comando cat")
# 1. Começamos com um dicionário vazio
comandos_usuario = {}

print("--- Cadastro de Comandos do Terminal ---")

# 2. Criamos um loop que roda até o usuário decidir parar
while True:
    # Pergunta qual será o nome do atalho (a chave)
    apelido = input("\nDigite um apelido para o comando (ou 'sair' para encerrar): ")
    
    # Se o usuário digitar 'sair', o programa encerra o loop
    if apelido.lower() == 'sair':
        break
        
    # Pergunta qual é o comando real do terminal (o valor)
    comando_real = input(f"Digite o comando real para '{apelido}': ")
    
    # 3. Salva os dados dentro do dicionário: dicionario[chave] = valor
    comandos_usuario[apelido] = comando_real
    print(f" Atalho '{apelido}' salvo com sucesso!")

# 4. Exibe o dicionário final na tela
print("\n--- Seu Dicionário de Comandos Final ---")
print(comandos_usuario)
