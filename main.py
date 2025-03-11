categoria = ''
listaAlunos  = []
listaDisciplinas  = []
listaProfessores  = []
listaTurmas  = []
listaMatricula = []

print('\n-----------------------------')
print('***** SISTEMA ACADÊMICO *****')
print('-----------------------------\n')

v1 = False
while v1 == False:
    print('****** MENU PRINCIPAL ******\n')
    print('(1) Gerenciar estudantes')
    print('(2) Gerenciar disciplinas')
    print('(3) Gerenciar professores')
    print('(4) Gerenciar turmas')
    print('(5) Gerenciar matriculas')
    print('(9) Sair')
    categoria = str(input('Informe a opção desejada: ').lower())
    if categoria in ['1', '2', '3', '4', '5', '9']:
        v1 = True
    else:
        print('Opção inválida. Tente novamente.')
    
    if (categoria == '1'):
        categoria = 'ESTUDANTES'
    elif (categoria == '2'):
        categoria = 'DISCIPLINAS'
    elif (categoria == '3'):
        categoria = 'PROFESSORES'
    elif (categoria == '4'):
        categoria = 'TURMAS'
    elif (categoria == '5'):
        categoria = 'MATRICULAS'
    else:
        print('Saindo do sistema...')
        categoria = 'SAIR'

funcionalidade = 0
while funcionalidade != '9':
    v2 = False
    while v2 == False:
        print('\n***** [' + categoria + '] MENU DE OPERAÇÕES *****')
        print('(1) Incluir')
        print('(2) Listar')
        print('(3) Excluir')
        print('(4) Alterar')
        print('(9) Voltar')
        funcionalidade = input('Informa a ação desejada: ').lower()
        if funcionalidade in ['1', '2', '3', '4', 'incluir', 'listar', 'excluir', 'alterar']:
            v2 = True
        elif(funcionalidade == '9'):
            v1 = False
            v2 = True
        else:
            print('Opção inválida. Tente novamente.')



    match funcionalidade:
        
        #INCLUIR
        case '1':
            if(categoria == 'ESTUDANTES'):
                listaAlunos.append(input('Nome do aluno: '))
            elif(categoria == 'DISCIPLINAS'):
                listaDisciplinas.append(input('Nome da disciplina: '))
            elif(categoria == 'PROFESSORES'):
                listaProfessores.append(input('Nome do professor: '))
            elif(categoria == 'TURMAS'):
                listaTurmas.append(input('Nome da turma: '))
            elif(categoria == 'MATRICULAS'):
                listaMatricula.append(input('Numero da matrícula: '))
        
        #LISTAR
        case '2': 
            if(categoria == 'ESTUDANTES'):
                print('\nAlunos: ')
                for nome in listaAlunos:
                    print('- ' + nome)
            elif(categoria == 'DISCIPLINAS'):
                print('\nDisciplinas: ')
                for nome in listaDisciplinas:
                    print('- ' + nome)
            elif(categoria == 'PROFESSORES'):
                print('\nProfessores: ')
                for nome in listaProfessores:
                    print('- ' + nome)
            elif(categoria == 'TURMAS'):
                print('\nTurmas: ')
                for nome in listaTurmas:
                    print('- ' + nome)
            elif(categoria == 'MATRICULAS'):
                print('\nMatrículas: ')
                for nome in listaMatricula:
                    print('- ' + nome)

        #EXCLUIR
        case '3':
            print('Selecionou c')

        #ALTERAR
        case '4':
            print('Selecionou d')