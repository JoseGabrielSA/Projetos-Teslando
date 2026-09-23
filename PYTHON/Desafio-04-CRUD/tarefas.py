from banco import conectar

conexao = conectar()
cursor = conexao.cursor()

# Criar tarefa
def criar_tarefa(titulo, descricao, usuario_id):
    comando = """
        INSERT INTO tarefas (titulo, descricao, usuario_id)
        VALUES (%s, %s, %s)
    """

    cursor.execute(comando, (titulo, descricao, usuario_id))
    conexao.commit()

    print("Tarefa criada com sucesso!")

# Listar tarefas
def listar_tarefas():
    comando = """
        SELECT
            tarefas.id,
            tarefas.titulo,
            tarefas.descricao,
            tarefas.data_criacao,
            tarefas.data_conclusao,
            usuarios.nome
        FROM tarefas
        INNER JOIN usuarios
            ON tarefas.usuario_id = usuarios.id
        ORDER BY tarefas.id
    """

    cursor.execute(comando)
    tarefas = cursor.fetchall()
    if not tarefas:
        print("NENHUMA TAREFA ENCONTRADA!")
        return

    for tarefa in tarefas:
        print(f"ID: {tarefa[0]}")
        print(f"Título: {tarefa[1]}")
        print(f"Descrição: {tarefa[2]}")
        print(f"Data de criação: {tarefa[3]}")
        print(f"Data de conclusão: {tarefa[4]}")
        print(f"Usuário: {tarefa[5]}")
        print("-" * 30)

# Atualizar tarefa
def atualizar_tarefa(tarefa_id, titulo, descricao, data_conclusao):
    comando = """
        UPDATE tarefas
        SET titulo = %s,
            descricao = %s,
            data_conclusao = %s
        WHERE id = %s;
    """

    cursor.execute(comando, (titulo, descricao, data_conclusao, tarefa_id))
    conexao.commit()

    if cursor.rowcount == 0:
        print("Tarefa não encontrada!")
    else:
        print("Tarefa atualizada com sucesso!")

# Excluir Tarefa
def excluir_tarefa(tarefa_id):
    comando = """
        DELETE FROM tarefas
        WHERE id = %s;
    """

    cursor.execute(comando, (tarefa_id,))
    conexao.commit()

    if cursor.rowcount == 0:
        print("Tarefa não encontrada!")
    else:
        print("Tarefa excluída com sucesso!")