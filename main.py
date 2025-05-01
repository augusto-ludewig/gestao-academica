# main.py
from inclusao import *
from auxiliar import *
from alteracao import *
from exclusao import *
from persistencia import *

# Carregar dados ao iniciar
dados = carregar_dados()
lista_alunos = dados['alunos']
lista_disciplinas = dados['disciplinas']
lista_professores = dados['professores']
lista_turmas = dados['turmas']
lista_matriculas = dados['matriculas']

print('\n-----------------------------')
print('***** SISTEMA ACADÊMICO *****')
print('-----------------------------\n')

# Menu principal
while True:
    categoria = print_menu_principal()
    
    # Conversão da seleção em palavra para ser usado como variável
    if categoria == '1':
        categoria = 'estudantes'
    elif categoria == '2':
        categoria = 'disciplinas'
    elif categoria == '3':
        categoria = 'professores'
    elif categoria == '4':
        categoria = 'turmas'
    elif categoria == '5':
        categoria = 'matriculas'
    elif categoria == '0':
        print('Saindo do sistema...')
        break
    else:
        print('\nOpção inválida. Tente novamente.\n')
    
    while True:
        funcionalidade = print_menu_funcionalidades(categoria)

        if funcionalidade in ['1', '2', '3', '4', 'incluir', 'listar', 'excluir', 'alterar']:
            match funcionalidade:  

            #INCLUIR
                case '1':
                    print('\n===== INCLUSÃO =====')
                    if categoria == 'estudantes':
                        incluir_aluno(lista_alunos)
                    elif categoria == 'disciplinas':
                        incluir_disciplina(lista_disciplinas)
                    elif categoria == 'professores':
                        incluir_professor(lista_professores)
                    elif categoria == 'turmas':
                        incluir_turma(lista_turmas)
                    elif categoria == 'matriculas':
                        incluir_matricula(lista_matriculas, lista_alunos, lista_turmas)
                    else:
                        print("Opção inválida!")
            #LISTAR
                case '2': 
                    print('\n===== LISTAGEM =====')
                    if categoria == 'estudantes':
                        listar(categoria, lista_alunos)
                    elif categoria == 'disciplinas':
                        listar(categoria, lista_disciplinas)
                    elif categoria == 'professores':
                        listar(categoria, lista_professores)
                    elif categoria == 'turmas':
                        listar(categoria, lista_turmas)
                    elif categoria == 'matriculas':
                        listar(categoria, lista_matriculas)
                    else:
                        print("Opção inválida!")

            #EXCLUIR
                case '3':
                    print('\n===== EXCLUSÃO =====')
                    if categoria == 'estudantes':
                        excluir_registro(lista_alunos)
                    elif categoria == 'disciplinas':
                        excluir_disciplina(lista_disciplinas)
                    elif categoria == 'professores':
                        excluir_registro(lista_professores)
                    elif categoria == 'turmas':
                        excluir_registro(lista_turmas)
                    elif categoria == 'matriculas':
                        excluir_matricula(lista_matriculas)
                    
            #ALTERAR
                case '4':

                    print('\n===== ALTERAR =====')
                    if categoria == 'estudantes':
                        alterar_estudante(lista_alunos)
                    elif categoria == 'disciplinas':
                        alterar_disciplina(lista_disciplinas)
                    elif categoria == 'professores':
                        alterar_professor(lista_professores)
                    else: #turmas
                        alterar_turma(lista_turmas)



        # Volta ao menu principal
        elif funcionalidade == '0' or funcionalidade == 'Voltar ao menu principal':
            if salvar_dados(lista_alunos, lista_professores, lista_disciplinas,
                            lista_turmas, lista_matriculas):
                print('Dados salvos com sucesso!')
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.')
