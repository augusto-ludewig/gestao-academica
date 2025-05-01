# Exclusão

# Função genérica para exclusão em dicionários (alunos, professores, turmas)
def excluir_registro(dicionario):
    try:
        id = int(input('Digite o ID para remover: '))
        dicionario.pop(id)
        print("Registro removido com sucesso!")
    except (KeyError, ValueError):
        print("Erro: ID inválido ou não encontrado!")

# Função específica para disciplinas (código string)
def excluir_disciplina(dicionario):
    try:
        codigo = input('Digite o código da disciplina: ')
        dicionario.pop(codigo)
        print("Disciplina removida com sucesso!")
    except KeyError:
        print("Erro: Código não encontrado!")

# Função específica para matrículas
def excluir_matricula(lista_matriculas):
    try:
        turma = int(input('Código da turma: '))
        aluno = int(input('Código do aluno: '))
        lista_matriculas.remove((turma, aluno))
        print("Matrícula removida com sucesso!")
    except (ValueError, TypeError):
        print("Erro: Matrícula não encontrada ou IDs inválidos!")