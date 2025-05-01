# alteracao.py

def alterar_estudante(alunos):
    print("\n--- Alterar Estudante ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    while True:
        try:
            id = int(input("ID do aluno: "))
            if id not in alunos:
                print("Erro: ID não encontrado!")
                continue
            break
        except ValueError:
            print("Erro: ID deve ser um número!")

    nome_atual, cpf_atual = alunos[id]

    novo_nome = input(f"Nome atual: {nome_atual}"
                      f"\nNovo nome (vazio para manter): ").strip()
    nome = novo_nome if novo_nome else nome_atual

    while True:
        novo_cpf = input(f"CPF atual: {cpf_atual}"
                         f"\nNovo CPF (vazio para manter): ").strip()
        if not novo_cpf:
            cpf = cpf_atual
            break

        cpfs = [aluno[1] for aluno in alunos.values() if aluno[1] != cpf_atual]
        if novo_cpf in cpfs:
            print("Erro: CPF já cadastrado!")
            continue
        cpf = novo_cpf
        break

    alunos[id] = (nome, cpf)
    print("Dados atualizados com sucesso!")


def alterar_disciplina(disciplinas):
    print("\n--- Alterar Disciplina ---")
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    # Obter código válido
    codigo = input("Código da disciplina: ").strip()
    if codigo not in disciplinas:
        print("Erro: Código não encontrado!")
        return

    # Novo nome
    nome_atual = disciplinas[codigo]
    novo_nome = input(f"Nome atual: {nome_atual}"
                      f"\nNovo nome (vazio para manter): ").strip()
    if novo_nome:
        disciplinas[codigo] = novo_nome
        print("Disciplina atualizada com sucesso!")
    else:
        print("Nenhuma alteração realizada.")


def alterar_professor(professores):
    print("\n--- Alterar Professor ---")
    if not professores:
        print("Nenhum professor cadastrado.")
        return

    while True:
        try:
            id = int(input("ID do professor: "))
            if id not in professores:
                print("Erro: ID não encontrado!")
                continue
            break
        except ValueError:
            print("Erro: ID deve ser um número!")

    nome_atual, cpf_atual = professores[id]

    novo_nome = input(f"Nome atual: {nome_atual}"
                      f"\nNovo nome (vazio para manter): ").strip()
    nome = novo_nome if novo_nome else nome_atual

    while True:
        novo_cpf = input(f"CPF atual: {cpf_atual}"
                         f"\nNovo CPF (vazio para manter): ").strip()
        if not novo_cpf:
            cpf = cpf_atual
            break

        cpfs = [prof[1] for prof in professores.values() if prof[1] != cpf_atual]
        if novo_cpf in cpfs:
            print("Erro: CPF já cadastrado!")
            continue
        cpf = novo_cpf
        break

    professores[id] = (nome, cpf)
    print("Dados atualizados com sucesso!")


def alterar_turma(turmas):
    print("\n--- Alterar Turma ---")
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    # Obter ID válido
    while True:
        try:
            id = int(input("Código da turma: "))
            if id not in turmas:
                print("Erro: Código não encontrado!")
                continue
            break
        except ValueError:
            print("Erro: Código inválido!")

    nome_atual = turmas[id]
    novo_nome = input(f"Nome atual: {nome_atual}"
                      f"\nNovo nome (vazio para manter): ").strip()
    if novo_nome:
        turmas[id] = novo_nome
        print("Turma atualizada com sucesso!")
    else:
        print("Nenhuma alteração realizada.")