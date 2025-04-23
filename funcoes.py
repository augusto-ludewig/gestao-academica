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
    print("Em desenvolvimento")

def incluirProfessor(lista):
    print("Em desenvolvimento")

def incluirTurma(lista):
    print("Em desenvolvimento")

def incluirMatricula(lista):
    print("Em desenvolvimento")

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
            print('EM DESENVOLVIMENTO')
    except:
        print('Erro ao alterar! ID não registrado.')