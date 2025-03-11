#listas para armazenar os dados
listaAlunos  = []
listaDisciplinas  = []
listaProfessores  = []
listaTurmas  = []
listaMatricula = []

print('\n-----------------------------')
print('***** SISTEMA ACADÊMICO *****')
print('-----------------------------\n')

# Menu principal
while True:
    print('****** MENU PRINCIPAL ******\n')
    print('(1) Gerenciar estudantes')
    print('(2) Gerenciar disciplinas')
    print('(3) Gerenciar professores')
    print('(4) Gerenciar turmas')
    print('(5) Gerenciar matriculas')
    print('(9) Sair')

    categoria = str(input('\nInforme a opção desejada: ')) #Entrada de dados para seleção
    
    # Conversão da seleção em palavra para ser usado como variável
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
    elif (categoria == '9'):
        print('Saindo do sistema...')
        break
    else:
        print('\nOpção inválida. Tente novamente.\n')
    
    while True and categoria in ['ESTUDANTES', 'DISCIPLINAS', 'PROFESSORES', 'TURMAS', 'MATRICULAS']:
        # Sub menu - Funcionalidades
        print('\n***** [' + categoria + '] MENU DE OPERAÇÕES *****')
        print('(1) Incluir')
        print('(2) Listar')
        print('(3) Excluir')
        print('(4) Alterar')
        print('(9) Voltar ao menu principal')
        funcionalidade = input('\nInforma a ação desejada: ').lower()
        if funcionalidade in ['1', '2', '3', '4', 'incluir', 'listar', 'excluir', 'alterar']:
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
                    try:
                        if(categoria == 'ESTUDANTES'):
                            listaAlunos.remove(input('Digite o nome do aluno para ser removido: '))
                        elif(categoria == 'DISCIPLINAS'):
                            listaDisciplinas.remove(input('Digite o nome do aluno para ser removido: '))
                        elif(categoria == 'PROFESSORES'):
                            listaProfessores.remove(input('Digite o nome do aluno para ser removido: '))
                        elif(categoria == 'TURMAS'):
                            listaTurmas.remove(input('Digite o nome do aluno para ser removido: '))
                        elif(categoria == 'MATRICULAS'):
                            listaMatricula.remove(input('Digite o nome do aluno para ser removido: '))
                    except:
                        print('Erro ao excluir! ' + categoria + ' não registrado.')
                #ALTERAR
                case '4':
                    print('Selecionou d')
        elif(funcionalidade == '9' or funcionalidade == 'Voltar ao menu principal'):
            break
        else:
            print('Opção inválida. Tente novamente.')