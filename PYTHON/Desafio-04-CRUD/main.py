while True:
    try:
        code = int(input(
            "\n=====================\n"
            "  GESTÃO DE TAREFAS\n"
            "=====================\n"
            "Digite uma das opções a seguir:\n"
            " 1. USUÁRIOS\n"
            " 2. TAREFAS\n"
            " 0. SAIR\n"
            "DIGITE AQUI: "))
        
    except ValueError:
        print("Erro: digite uma opção válida!")
        continue

    # ---------------------
    #       USUÁRIOS
    # ---------------------

    if code == 1:
        try:
            code_user = int(input(
                "\n=====================\n"
                "       USUÁRIOS\n"
                "=====================\n"
                "Digite uma das opções a seguir:\n"
                " 1. CRIAR\n"
                " 2. LER LISTA\n"
                " 3. ATUALIZAR\n"
                " 4. DELETAR\n"
                " 0. VOLTAR\n"
                "DIGITE AQUI: "))
            
        except ValueError:
                print("Erro: digite uma opção válida!")
                continue

        # CREATE USER
        if code_user == 1:
            while True:
                nome = input("NOME DE USUÁRIO: ").strip()

                if not nome:
                    print("Erro: o nome não pode ficar vazio!")
                else:
                    break

            while True:
                email = input("INSIRA O SEU E-MAIL: ").strip()

                if not email:
                    print("Erro: o e-mail não pode ficar vazio!")
                elif "@" not in email:
                    print("Erro: e-mail inválido! O e-mail deve conter @.")
                else:
                    break

            from usuarios import criar_usuario
            criar_usuario(nome, email)

        # LIST USER
        elif code_user == 2:
            from usuarios import listar_usuarios
            listar_usuarios()

        # UPDATE USER
        elif code_user == 3:
            while True:
                nome = input("NOVO NOME DE USUÁRIO: ").strip()

                if not nome:
                    print("Erro: o nome não pode ficar vazio!")
                else:
                    break

            while True:
                email = input("INSIRA O SEU NOVO E-MAIL: ").strip()

                if not email:
                    print("Erro: o e-mail não pode ficar vazio!")
                elif "@" not in email:
                    print("Erro: e-mail inválido! O e-mail deve conter @.")
                else:
                    break

            while True:
                try:
                    usuario_id = int(input("INSIRA O ID DO USUÁRIO: "))
                    break
                except ValueError:
                    print("Erro: o ID deve ser um número!")

            from usuarios import atualizar_usuario
            atualizar_usuario(usuario_id, nome, email)

        # DELETE USER
        elif code_user == 4:
            while True:
                try:
                    usuario_id = int(input("INSIRA O ID DO USUÁRIO PARA A EXCLUSÃO: "))
                    break
                except ValueError:
                    print("Erro: o ID deve ser um número!")

            from usuarios import excluir_usuario
            excluir_usuario(usuario_id)            

        # VOLTAR
        elif code_user == 0:
            continue

        else:
            print("Opção inválida!")

    # ---------------------
    #        TAREFAS
    # ---------------------
    elif code == 2:
        try:
            code_user = int(input(
                        "\n=====================\n"
                        "       TAREFAS\n"
                        "=====================\n"
                        "Digite uma das opções a seguir:\n"
                        " 1. CRIAR\n"
                        " 2. LER LISTA\n"
                        " 3. ATUALIZAR\n"
                        " 4. DELETAR\n"
                        " 0. VOLTAR\n"
                        "DIGITE AQUI: "))
        
        except ValueError:
                print("Erro: digite uma opção válida!")
                continue
        # CREATE TASK
        if code_user == 1:
            while True:
                titulo = input("TÍTULO: ").strip()
        
                if not titulo:
                    print("Erro: o título não pode ficar vazio!")
                else:
                    break

            while True:
                descricao = input("DESCRIÇÃO: ").strip()
        
                if not descricao:
                    print("Erro: a descrição não pode ficar vazia!")
                else:
                    break

            while True:
                try:
                    usuario_id = int(input("INSIRA O ID DO USUÁRIO: "))
                    break
                except ValueError:
                    print("Erro: o ID deve ser um número!")

            from tarefas import criar_tarefa
            criar_tarefa(titulo, descricao, usuario_id)

        # lIST TASK
        elif code_user == 2:
            from tarefas import listar_tarefas
            listar_tarefas()

        # UPDATE TAREFA
        elif code_user == 3:
            while True:
                try:
                    tarefa_id = int(input("INSIRA O ID DA TAREFA: "))
                    break
                except ValueError:
                    print("Erro: o ID deve ser um número!")

            while True:
                titulo = input("NOVO TÍTULO: ").strip()

                if not titulo:
                    print("Erro: o título não pode ficar vazio!")
                else:
                    break

            while True:
                descricao = input("NOVA DESCRIÇÃO: ").strip()

                if not descricao:
                    print("Erro: a descrição não pode ficar vazia!")
                else:
                    break

            data_conclusao = input("DATA DE CONCLUSÃO (AAAA-MM-DD HH:MM:SS): ").strip()

            from tarefas import atualizar_tarefa
            atualizar_tarefa(tarefa_id, titulo, descricao, data_conclusao)

        # DELETE TASK
        elif code_user == 4:
            while True:
                try:
                    tarefa_id = int(input("INSIRA O ID DA TAREFA PARA A EXCLUSÃO: "))
                    break
                except ValueError:
                    print("Erro: o ID deve ser um número!")

            from tarefas import excluir_tarefa
            excluir_tarefa(tarefa_id)
            
        # VOLTAR
        elif code_user == 0:
            continue
        
        else:
            print("Opção inválida!")

    # ---------------------
    #         SAIR
    # ---------------------

    elif code == 0:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")