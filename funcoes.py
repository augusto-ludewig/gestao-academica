# Menu principal
def printMenuPrincipal():
    print('****** MENU PRINCIPAL ******\n')
    print('(1) Gerenciar estudantes')
    print('(2) Gerenciar disciplinas')
    print('(3) Gerenciar professores')
    print('(4) Gerenciar turmas')
    print('(5) Gerenciar matriculas')
    print('(0) Sair')
    categoria = str(input('\nInforme a opção desejada: '))  # Entrada de dados para seleção
    return categoria

# Sub menu - Funcionalidades
def printMenuFuncionalidades(categoria):
    print('\n***** [' + categoria.upper() + '] MENU DE OPERAÇÕES *****')
    print('(1) Incluir')
    print('(2) Listar')
    print('(3) Excluir')
    print('(4) Alterar')
    print('(0) Voltar ao menu principal')
    funcionalidade = input('\nInforma a ação desejada: ').lower()
    return funcionalidade

# Inclusões
def incluirAluno(lista):
    idAluno = int(len(lista) + 1)
    while idAluno in lista: #evita ID repetido
        idAluno += 1
    nomeAluno = input('\nNome do aluno: ')
    cpfAluno = input('CPF do aluno: ')
    while cpfAluno in lista:
        print("CPF já cadastrado!")
        cpfAluno = input('Digite o CPF do aluno: ')
    lista[idAluno] = nomeAluno, cpfAluno

def incluirDisciplina(lista):
    idDisciplina = input('\nCódigo da disciplina: ')
    while idDisciplina in lista:
        print("Código já cadastrado!")
        idDisciplina = input('Por favor, digite um código diferente: ')
    nomeDisciplina = input('\nNome da disciplina: ')
    lista[idDisciplina] = nomeDisciplina

def incluirProfessor(lista):
    idProfessor = int(len(lista) + 1)
    while idProfessor in lista:  # evita ID repetido
        idProfessor += 1
    nomeProfessor = input('\nNome do professor: ')
    cpfProfessor = input('CPF do professor: ')
    while cpfProfessor in lista:
        print("CPF já cadastrado!")
        cpfAluno = input('Digite o CPF do professor: ')
    lista[idProfessor] = nomeProfessor, cpfProfessor

def incluirTurma(lista):
    idTurma = int(input('\nCódigo da turma: '))
    while idTurma in lista:
        print("Código já cadastrado!")
        idTurma = input('Por favor, digite um código diferente: ')
    nomeTurma = input('\nNome da turma: ')
    lista[idTurma] = nomeTurma


def incluirMatricula(listaMatriculas, listaAlunos, listaTurmas):
    print("\n--- Incluir Matrícula ---")
    idTurma = int(input('Código da turma: '))
    idAluno = int(input('Código do aluno: '))

    if idTurma not in listaTurmas:
        print(f"Erro: Turma {idTurma} não encontrada!")
        return

    if idAluno not in listaAlunos:
        print(f"Erro: Aluno {idAluno} não encontrado!")
        return

    for matricula in listaMatriculas:
        if matricula[0] == idTurma and matricula[1] == idAluno:
            print("Erro: Matrícula já existente!")
            return

    listaMatriculas.append((idTurma, idAluno))
    print("Matrícula cadastrada com sucesso!")

# Listagem
def listar(categoria, lista):
    print('\n' + categoria + ':')
    for key, item in lista.items():
        print(key, item)

# Exclusão
def excluir(lista):
    try:
        lista.pop(int(input('Digite o ID para ser removido: ')))
    except:
        print('Erro ao excluir! ID não registrado.')


def alterarEstudante(lista):
    try:
        alunoAlterar = int(input('Digite o ID do aluno a ser alterado: '))
        if alunoAlterar in lista:
            idAluno = alunoAlterar
            nomeAluno = input('Nome do aluno: ')
            cpfAluno = input('CPF do aluno: ')
            lista[idAluno] = nomeAluno, cpfAluno
        else:
            print("Não foi possível localizar o ID informado.")
    except:
        print('Erro ao alterar! ID não registrado.')

def alterarProfessor(lista):
    try:
        professorAlterar = int(input('Digite o ID do professor a ser alterado: '))
        if professorAlterar in lista:
            idProfessor = professorAlterar
            nomeProfessor = input('Nome do professor: ')
            cpfProfessor = input('CPF do professor: ')
            lista[idProfessor] = nomeProfessor, cpfProfessor
        else:
            print("Não foi possível localizar o ID informado.")
    except:
        print('Erro ao alterar! ID não registrado.')