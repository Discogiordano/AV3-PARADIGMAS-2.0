import json
import os

# Novos 20 filmes
conteudos_2 = [
    {"id": 7, "titulo": "Inception", "descricao": "Sonhos dentro de sonhos", "tipo": "filme", "generos": ["ficção científica", "ação"]},
    {"id": 8, "titulo": "The Matrix", "descricao": "A realidade simulada", "tipo": "filme", "generos": ["ficção científica", "ação"]},
    {"id": 9, "titulo": "Interstellar", "descricao": "Viagem no espaço-tempo", "tipo": "filme", "generos": ["ficção científica", "drama"]},
    {"id": 10, "titulo": "The Shawshank Redemption", "descricao": "Liberdade através da perseverança", "tipo": "filme", "generos": ["drama"]},
    {"id": 11, "titulo": "The Dark Knight", "descricao": "O cavaleiro das trevas luta contra o crime", "tipo": "filme", "generos": ["ação", "drama"]},
    {"id": 12, "titulo": "Pulp Fiction", "descricao": "Histórias interligadas de crime", "tipo": "filme", "generos": ["crime", "drama"]},
    {"id": 13, "titulo": "Fight Club", "descricao": "Clube de luta clandestino", "tipo": "filme", "generos": ["drama"]},
    {"id": 14, "titulo": "Forrest Gump", "descricao": "A vida de Forrest Gump", "tipo": "filme", "generos": ["drama", "comédia"]},
    {"id": 15, "titulo": "Gladiator", "descricao": "O gladiador em busca de vingança", "tipo": "filme", "generos": ["ação", "drama"]},
    {"id": 16, "titulo": "Saving Private Ryan", "descricao": "Resgate na Segunda Guerra Mundial", "tipo": "filme", "generos": ["ação", "drama", "guerra"]},
    {"id": 17, "titulo": "Schindler's List", "descricao": "A história de Oskar Schindler", "tipo": "filme", "generos": ["drama", "histórico"]},
    {"id": 18, "titulo": "Braveheart", "descricao": "A luta pela liberdade da Escócia", "tipo": "filme", "generos": ["ação", "drama", "histórico"]},
    {"id": 19, "titulo": "The Lion King", "descricao": "O rei leão em busca de seu destino", "tipo": "animação", "generos": ["animação", "drama"]},
    {"id": 20, "titulo": "Titanic", "descricao": "Romance no trágico naufrágio", "tipo": "filme", "generos": ["drama", "romance"]},
    {"id": 21, "titulo": "Avatar", "descricao": "A luta por Pandora", "tipo": "filme", "generos": ["ficção científica", "ação"]},
    {"id": 22, "titulo": "The Godfather", "descricao": "A saga da família Corleone", "tipo": "filme", "generos": ["crime", "drama"]},
    {"id": 23, "titulo": "The Godfather: Part II", "descricao": "A continuação da saga Corleone", "tipo": "filme", "generos": ["crime", "drama"]},
    {"id": 24, "titulo": "The Lord of the Rings: The Fellowship of the Ring", "descricao": "A jornada para destruir o anel", "tipo": "filme", "generos": ["aventura", "fantasia"]},
    {"id": 25, "titulo": "The Lord of the Rings: The Two Towers", "descricao": "A continuação da jornada", "tipo": "filme", "generos": ["aventura", "fantasia"]},
    {"id": 26, "titulo": "The Lord of the Rings: The Return of the King", "descricao": "A conclusão da jornada", "tipo": "filme", "generos": ["aventura", "fantasia"]}
]

# Definir o caminho da pasta data dentro do diretório project
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Criar o diretório data se não existir
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Salvando os dados em arquivos JSON com codificação UTF-8
with open(os.path.join(DATA_DIR, 'conteudos_2.json'), 'w', encoding='utf-8') as f:
    json.dump(conteudos_2, f, ensure_ascii=False, indent=4)

print("Dados iniciais salvos com sucesso.")
