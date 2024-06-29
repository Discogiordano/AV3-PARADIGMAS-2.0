import json
import os
from usuario import Usuario
from conteudo import Conteudo

# Definir o caminho da pasta data dentro do diretório project
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'data')

def salvar_dados(usuarios, conteudos, conteudos_2):
    # Criar o diretório data se não existir
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Converter objetos Usuario para dicionários e salvar no arquivo JSON
    usuarios_data = [usuario.__dict__ for usuario in usuarios.values()]
    with open(os.path.join(DATA_DIR, 'usuarios.json'), 'w', encoding='utf-8') as f:
        json.dump(usuarios_data, f, ensure_ascii=False, indent=4)

    # Converter objetos Conteudo para dicionários e salvar no arquivo JSON
    conteudos_data = [conteudo.__dict__ for conteudo in conteudos.values()]
    with open(os.path.join(DATA_DIR, 'conteudos.json'), 'w', encoding='utf-8') as f:
        json.dump(conteudos_data, f, ensure_ascii=False, indent=4)

    # Converter objetos Conteudo_2 para dicionários e salvar no arquivo JSON
    conteudos_2_data = [conteudo.__dict__ for conteudo in conteudos_2.values()]
    with open(os.path.join(DATA_DIR, 'conteudos_2.json'), 'w', encoding='utf-8') as f:
        json.dump(conteudos_2_data, f, ensure_ascii=False, indent=4)

def carregar_dados():
    print("Carregando dados de 'usuarios.json'...")
    try:
        with open(os.path.join(DATA_DIR, 'usuarios.json'), 'r', encoding='utf-8') as f:
            usuarios_data = json.load(f)
            usuarios = {u['id']: Usuario(**u) for u in usuarios_data}
    except FileNotFoundError:
        print("'usuarios.json' não encontrado.")
        usuarios = {}
    except Exception as e:
        print(f"Erro ao carregar 'usuarios.json': {e}")
        usuarios = {}

    print("Usuários carregados:", usuarios)

    print("Carregando dados de 'conteudos.json'...")
    try:
        with open(os.path.join(DATA_DIR, 'conteudos.json'), 'r', encoding='utf-8') as f:
            conteudos_data = json.load(f)
            conteudos = {c['id']: Conteudo(**c) for c in conteudos_data}
    except FileNotFoundError:
        print("'conteudos.json' não encontrado.")
        conteudos = {}
    except Exception as e:
        print(f"Erro ao carregar 'conteudos.json': {e}")
        conteudos = {}

    print("Conteúdos carregados:", conteudos)

    print("Carregando dados de 'conteudos_2.json'...")
    try:
        with open(os.path.join(DATA_DIR, 'conteudos_2.json'), 'r', encoding='utf-8') as f:
            conteudos_2_data = json.load(f)
            conteudos_2 = {c['id']: Conteudo(**c) for c in conteudos_2_data}
    except FileNotFoundError:
        print("'conteudos_2.json' não encontrado.")
        conteudos_2 = {}
    except Exception as e:
        print(f"Erro ao carregar 'conteudos_2.json': {e}")
        conteudos_2 = {}

    print("Conteúdos 2 carregados:", conteudos_2)
    
    return usuarios, conteudos, conteudos_2
