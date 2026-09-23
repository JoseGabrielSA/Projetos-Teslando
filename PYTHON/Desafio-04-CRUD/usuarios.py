from banco import conectar

conexao = conectar()  # -> abrir conexão

cursor = conexao.cursor()  # -> enviar comandos SQL para o DB

# Criar user
def criar_usuario(nome, email):
    comando = """
        INSERT INTO usuarios (nome, email)
        VALUES (%s, %s)
    """

    cursor.execute(comando, (nome, email))
    conexao.commit()

    print("Usuário criado com sucesso!")

# ler a lista de usuários
def listar_usuarios():
    comando = """
        SELECT id, nome, email
        FROM usuarios
        ORDER BY id
    """

    cursor.execute(comando)
    usuarios = cursor.fetchall()

    if not usuarios:
        print("NENHUM USUÁRIO CADASTRADO!")
        return

    for usuario in usuarios:
        print(f"ID: {usuario[0]}")
        print(f"Nome: {usuario[1]}")
        print(f"E-mail: {usuario[2]}")
        print("-" * 30)

# Atualizar um usuário
def atualizar_usuario(usuario_id, nome, email):
    comando = """
        UPDATE usuarios
        SET nome = %s, email = %s
        WHERE id = %s;
    """

    cursor.execute(comando, (nome, email, usuario_id))
    conexao.commit()

    if cursor.rowcount == 0:
        print("Usuário não encontrado!")
    else:
        print("Usuário atualizado com sucesso!")

# Excluir usuário
def excluir_usuario(usuario_id):
    comando = """
        DELETE FROM usuarios
        WHERE id = %s;
    """

    cursor.execute(comando, (usuario_id,))
    conexao.commit()

    if cursor.rowcount == 0:
        print("Usuário não encontrado!")
    else:
        print("Usuário excluída com sucesso!")