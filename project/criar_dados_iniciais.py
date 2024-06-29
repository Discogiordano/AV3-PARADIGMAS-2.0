import json
import os

# Dados dos usuários e conteúdos
usuarios = [
    {
        "id": 1,
        "nome": "Malena",
        "email": "malena@blade.com",
        "senha": "senha123",
        "tipo_assinatura": "premium",
        "preferencias": ["drama", "ação", "comédia"],
        "historico": [1, 2, 3]
    },
    {
        "id": 2,
        "nome": "Miquella",
        "email": "miquella@sacra.com",
        "senha": "senha321",
        "tipo_assinatura": "básica",
        "preferencias": ["ação", "ficção científica", "terror"],
        "historico": [1, 3]
    }
]

conteudos = [
    {
        "id": 1,
        "titulo": "Harry Potter",
        "descricao": "Mundo Mágico de fantasias",
        "tipo": "filme",
        "generos": ["aventura", "fantasia"]
    },
    {
        "id": 2,
        "titulo": "Dexter",
        "descricao": "Uma intrigante série de investigação",
        "tipo": "série",
        "generos": ["drama", "suspense"]
    },
    {
        "id": 3,
        "titulo": "Naruto",
        "descricao": "Ação no mundo ninja",
        "tipo": "animação",
        "generos": ["animação", "ação", "drama"]
    },
    {
        "id": 4,
        "titulo": "Game of Thrones",
        "descricao": "Aventura em fantasia medieval",
        "tipo": "série",
        "generos": ["aventura", "ação", "fantasia"]
    },
    {
        "id": 5,
        "titulo": "Alien",
        "descricao": "Terror de ficção científica no espaço sideral",
        "tipo": "filme",
        "generos": ["ficção científica", "mistério", "terror"]
    },
    {
        "id": 6,
        "titulo": "As Branquelas",
        "descricao": "Comédia besteirol",
        "tipo": "filme",
        "generos": ["comédia"]
    }
]

# Criando o diretório data se não existir
if not os.path.exists('data'):
    os.makedirs('data')

# Salvando os dados em arquivos JSON
with open('data/usuarios.json', 'w') as f:
    json.dump(usuarios, f, indent=4)

with open('data/conteudos.json', 'w') as f:
    json.dump(conteudos, f, indent=4)
