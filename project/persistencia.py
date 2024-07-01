import json
import os
from usuario import Usuario
from conteudo import Conteudo

def salvar_dados(usuarios, conteudos, conteudos_2):
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, 'data')

    print("Salvando dados dos usuários...")
    with open(os.path.join(data_dir, 'usuarios.json'), 'w', encoding='utf-8') as f:
        json.dump([usuario.__dict__ for usuario in usuarios.values()], f, ensure_ascii=False, indent=4)
    print("Dados dos usuários salvos.")

    print("Salvando dados dos conteúdos...")
    with open(os.path.join(data_dir, 'conteudos.json'), 'w', encoding='utf-8') as f:
        json.dump([conteudo.__dict__ for conteudo in conteudos.values()], f, ensure_ascii=False, indent=4)
    print("Dados dos conteúdos salvos.")

    print("Salvando dados dos conteúdos 2...")
    with open(os.path.join(data_dir, 'conteudos_2.json'), 'w', encoding='utf-8') as f:
        json.dump([conteudo.__dict__ for conteudo in conteudos_2.values()], f, ensure_ascii=False, indent=4)
    print("Dados dos conteúdos 2 salvos.")

def carregar_dados():
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, 'data')
    
    if not os.path.exists(data_dir):
        print(f"Criando diretório: {data_dir}")
        os.makedirs(data_dir)

    usuarios = {}
    conteudos = {}
    conteudos_2 = {}

    try:
        print("Carregando dados de 'usuarios.json'...")
        with open(os.path.join(data_dir, 'usuarios.json'), 'r', encoding='utf-8') as f:
            usuarios_data = json.load(f)
            for data in usuarios_data:
                usuarios[data['id']] = Usuario(**data)
        print("Usuários carregados.")
    except FileNotFoundError:
        print(f"Arquivo 'usuarios.json' não encontrado. Criando um arquivo vazio.")
        with open(os.path.join(data_dir, 'usuarios.json'), 'w', encoding='utf-8') as f:
            json.dump([], f)
    except Exception as e:
        print(f"Erro ao carregar 'usuarios.json': {e}")

    try:
        print("Carregando dados de 'conteudos.json'...")
        with open(os.path.join(data_dir, 'conteudos.json'), 'r', encoding='utf-8') as f:
            conteudos_data = json.load(f)
            for data in conteudos_data:
                conteudos[data['id']] = Conteudo(**data)
        print("Conteúdos carregados.")
    except FileNotFoundError:
        print(f"Arquivo 'conteudos.json' não encontrado. Criando um arquivo vazio.")
        with open(os.path.join(data_dir, 'conteudos.json'), 'w', encoding='utf-8') as f:
            json.dump([], f)
    except Exception as e:
        print(f"Erro ao carregar 'conteudos.json': {e}")

    try:
        print("Carregando dados de 'conteudos_2.json'...")
        with open(os.path.join(data_dir, 'conteudos_2.json'), 'r', encoding='utf-8') as f:
            conteudos_2_data = json.load(f)
            for data in conteudos_2_data:
                conteudos_2[data['id']] = Conteudo(**data)
        print("Conteúdos 2 carregados.")
    except FileNotFoundError:
        print(f"Arquivo 'conteudos_2.json' não encontrado. Criando um arquivo vazio.")
        with open(os.path.join(data_dir, 'conteudos_2.json'), 'w', encoding='utf-8') as f:
            json.dump([], f)
    except Exception as e:
        print(f"Erro ao carregar 'conteudos_2.json': {e}")

    return usuarios, conteudos, conteudos_2
