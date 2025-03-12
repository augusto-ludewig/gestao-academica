#Código desenvolvido por Augusto Ludewig, estudante de Análise e Desenvolvimento de Sistemas da PUCPR - Curitiba, 11/03/2025

#listas para armazenar os dados
listaAlunos  = []

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
    print('(0) Sair')

    categoria = str(input('\nInforme a opção desejada: ')) #Entrada de dados para seleção
    
    # Conversão da seleção em palavra para ser usado como variável
    if (categoria == '1'):
        categoria = 'ESTUDANTES'
    elif (categoria in ['2', '3' ,'4' , '5']):
        print('\nEM DESENVOLVIMENTO!\n')
    elif (categoria == '0'):
        print('Saindo do sistema...')
        break
    else:
        print('\nOpção inválida. Tente novamente.\n')
    
    while True and categoria == 'ESTUDANTES':
        # Sub menu - Funcionalidades
        print('\n***** [' + categoria + '] MENU DE OPERAÇÕES *****')
        print('(1) Incluir')
        print('(2) Listar')
        print('(3) Excluir')
        print('(4) Alterar')
        print('(0) Voltar ao menu principal')
        funcionalidade = input('\nInforma a ação desejada: ').lower()
        if funcionalidade in ['1', '2', '3', '4', 'incluir', 'listar', 'excluir', 'alterar']:
            match funcionalidade:  

            #INCLUIR
                case '1':
                    print('\n===== INCLUSÃO =====')
                    if(categoria == 'ESTUDANTES'):
                        listaAlunos.append(input('\nNome do aluno: '))
                    else:
                        print('EM DESENVOLVIMENTO')

                #LISTAR
                case '2': 
                    print('\n===== LISTAGEM =====')
                    if(categoria == 'ESTUDANTES'):
                        print('\nAlunos: ')
                        for nome in listaAlunos:
                            print('- ' + nome)
                    else:
                        print('EM DESENVOLVIMENTO')

                #EXCLUIR
                case '3':
                    print('\n===== EXCLUSÃO =====')
                    try:
                        if(categoria == 'ESTUDANTES'):
                            listaAlunos.remove(input('Digite o nome do aluno para ser removido: '))
                        else:
                            print('EM DESENVOLVIMENTO')
                    except:
                        print('Erro ao excluir! ' + categoria + ' não registrado.')
                    
                #ALTERAR
                case '4':

                    print('\n===== ALTERAR =====')

                    print('EM DESENVOLVIMENTO!')
        elif(funcionalidade == '0' or funcionalidade == 'Voltar ao menu principal'):
            break
        else:
            print('Opção inválida. Tente novamente.')