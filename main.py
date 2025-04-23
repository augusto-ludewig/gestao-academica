#Código desenvolvido por Augusto Ludewig, estudante de Análise e Desenvolvimento de Sistemas da PUCPR - Curitiba, 11/03/2025
from funcoes import *

#listas para armazenar os dados
listaAlunos  = {}
listaDisciplinas  = {}
listaProfessores  = {}
listaTurmas  = {}
listaMatriculas  = {}

print('\n-----------------------------')
print('***** SISTEMA ACADÊMICO *****')
print('-----------------------------\n')

# Menu principal
while True:
    categoria = printMenuPrincipal()
    
    # Conversão da seleção em palavra para ser usado como variável
    if (categoria == '1'):
        categoria = 'estudantes'
    elif (categoria in ['2', '3' ,'4' , '5']):
        print('\nEM DESENVOLVIMENTO!\n')
    elif (categoria == '0'):
        print('Saindo do sistema...')
        break
    else:
        print('\nOpção inválida. Tente novamente.\n')
    
    while True and categoria == 'estudantes':
        funcionalidade = printMenuFuncionalidades(categoria)

        if funcionalidade in ['1', '2', '3', '4', 'incluir', 'listar', 'excluir', 'alterar']:
            match funcionalidade:  

            #INCLUIR
                case '1':
                    print('\n===== INCLUSÃO =====')
                    if categoria == 'estudantes':
                        incluirAluno(listaAlunos)
                    elif categoria == 'disciplinas':
                        incluirDisciplina(listaDisciplinas)
                    elif categoria == 'professores':
                        incluirProfessor(listaProfessores)
                    elif categoria == 'turmas':
                        incluirTurma(listaTurmas)
                    else:
                        incluirMatricula(listaMatriculas)

                #LISTAR
                case '2': 
                    print('\n===== LISTAGEM =====')
                    if categoria == 'estudantes':
                        listar(categoria, listaAlunos)
                    elif categoria == 'disciplinas':
                        listar(categoria, listaDisciplinas)
                    elif categoria == 'professores':
                        listar(categoria, listaProfessores)
                    elif categoria == 'turmas':
                        listar(categoria, listaTurmas)
                    else:
                        listar(categoria, listaMatriculas)

                #EXCLUIR
                case '3':
                    print('\n===== EXCLUSÃO =====')
                    if categoria == 'estudantes':
                        excluir(listaAlunos)
                    elif categoria == 'disciplinas':
                        excluir(listaDisciplinas)
                    elif categoria == 'professores':
                        excluir(listaProfessores)
                    elif categoria == 'turmas':
                        excluir(listaTurmas)
                    else:
                        excluir(listaMatriculas)
                    
                #ALTERAR
                case '4':

                    print('\n===== ALTERAR =====')
                    if categoria == 'estudantes':
                        alterarEstudante(listaAlunos)
                    elif categoria == 'disciplinas':
                        print()
                    elif categoria == 'professores':
                        print()
                    elif categoria == 'turmas':
                        print()
                    else:
                        print()

        # Volta ao menu principal
        elif funcionalidade == '0' or funcionalidade == 'Voltar ao menu principal':
            break
        else:
            print('Opção inválida. Tente novamente.')