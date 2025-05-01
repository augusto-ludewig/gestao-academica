# persistencia.py
import json
import os

# Nomes dos arquivos
ARQUIVOS = {
    'alunos': 'alunos.json',
    'professores': 'professores.json',
    'disciplinas': 'disciplinas.json',
    'turmas': 'turmas.json',
    'matriculas': 'matriculas.json'
}


def salvar_dados(alunos, professores, disciplinas, turmas, matriculas):
    """Salva todos os dados em arquivos JSON"""
    try:
        # Salvar alunos (converte chaves int para str)
        with open(ARQUIVOS['alunos'], 'w') as f:
            json.dump({str(k): v for k, v in alunos.items()}, f)

        # Salvar professores (converte chaves int para str)
        with open(ARQUIVOS['professores'], 'w') as f:
            json.dump({str(k): v for k, v in professores.items()}, f)

        # Salvar disciplinas (mantém chaves str)
        with open(ARQUIVOS['disciplinas'], 'w') as f:
            json.dump(disciplinas, f)

        # Salvar turmas (converte chaves int para str)
        with open(ARQUIVOS['turmas'], 'w') as f:
            json.dump({str(k): v for k, v in turmas.items()}, f)

        # Salvar matrículas (converte tuplas para listas)
        with open(ARQUIVOS['matriculas'], 'w') as f:
            json.dump([list(m) for m in matriculas], f)

        return True
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        return False


def carregar_dados():
    """Carrega todos os dados dos arquivos JSON"""
    dados = {
        'alunos': {},
        'professores': {},
        'disciplinas': {},
        'turmas': {},
        'matriculas': []
    }

    try:
        # Carregar alunos (converte chaves str para int)
        if os.path.exists(ARQUIVOS['alunos']):
            with open(ARQUIVOS['alunos'], 'r') as f:
                dados['alunos'] = {int(k): tuple(v) for k, v in json.load(f).items()}

        # Carregar professores (converte chaves str para int)
        if os.path.exists(ARQUIVOS['professores']):
            with open(ARQUIVOS['professores'], 'r') as f:
                dados['professores'] = {int(k): tuple(v) for k, v in json.load(f).items()}

        # Carregar disciplinas
        if os.path.exists(ARQUIVOS['disciplinas']):
            with open(ARQUIVOS['disciplinas'], 'r') as f:
                dados['disciplinas'] = json.load(f)

        # Carregar turmas (converte chaves str para int)
        if os.path.exists(ARQUIVOS['turmas']):
            with open(ARQUIVOS['turmas'], 'r') as f:
                dados['turmas'] = {int(k): v for k, v in json.load(f).items()}

        # Carregar matrículas (converte listas para tuplas)
        if os.path.exists(ARQUIVOS['matriculas']):
            with open(ARQUIVOS['matriculas'], 'r') as f:
                dados['matriculas'] = [tuple(m) for m in json.load(f)]

    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

    return dados