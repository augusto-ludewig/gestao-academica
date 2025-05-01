# funções de inclusão

def incluir_aluno(lista):
    id_aluno = len(lista) + 1
    while id_aluno in lista:
        id_aluno += 1

    nome = input('\nNome do aluno: ').strip()

    # Verificar CPF único
    cpf = input('CPF do aluno: ').strip()
    cpfs_existentes = [aluno[1] for aluno in lista.values()]
    while cpf in cpfs_existentes:
        print("Erro: CPF já cadastrado!")
        cpf = input('Digite novo CPF: ').strip()
        cpfs_existentes = [aluno[1] for aluno in lista.values()]

    lista[id_aluno] = (nome, cpf)
    print("Aluno cadastrado com sucesso!")


def incluir_disciplina(lista):
    while True:
        codigo = input('\nCódigo da disciplina: ').strip()
        if codigo in lista:
            print("Erro: Código já existe!")
            continue
        break

    nome = input('Nome da disciplina: ').strip()
    lista[codigo] = nome
    print("Disciplina cadastrada com sucesso!")


def incluir_professor(lista):
    id_professor = len(lista) + 1
    while id_professor in lista:
        id_professor += 1

    nome = input('\nNome do professor: ').strip()

    cpf = input('CPF do professor: ').strip()
    cpfs_existentes = [prof[1] for prof in lista.values()]
    while cpf in cpfs_existentes:
        print("Erro: CPF já cadastrado!")
        cpf = input('Digite novo CPF: ').strip()
        cpfs_existentes = [prof[1] for prof in lista.values()]

    lista[id_professor] = (nome, cpf)
    print("Professor cadastrado com sucesso!")

def incluir_turma(lista):
    while True:
        try:
            codigo = int(input('\nCódigo da turma: '))
            if codigo in lista:
                print("Erro: Código já existe!")
                continue
            break
        except ValueError:
            print("Erro: Insira um número inteiro!")

    nome = input('Nome da turma: ').strip()
    lista[codigo] = nome
    print("Turma cadastrada com sucesso!")

def incluir_matricula(matriculas, alunos, turmas):
    print("\n--- Nova Matrícula ---")

    # Verificar turma
    while True:
        try:
            cod_turma = int(input('Código da turma: '))
            if cod_turma not in turmas:
                print("Erro: Turma não encontrada!")
                continue
            break
        except ValueError:
            print("Erro: Código inválido!")

    while True:
        try:
            cod_aluno = int(input('Código do aluno: '))
            if cod_aluno not in alunos:
                print("Erro: Aluno não encontrado!")
                continue
            break
        except ValueError:
            print("Erro: Código inválido!")

    nova_matricula = (cod_turma, cod_aluno)
    if nova_matricula in matriculas:
        print("Erro: Matrícula já existe!")
        return

    matriculas.append(nova_matricula)
    print("Matrícula realizada com sucesso!")