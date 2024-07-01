from usuario import Usuario
from conteudo import Conteudo

def cadastrar_usuario(usuarios, nome, email, senha, tipo_assinatura, tipo_user='usuário'):
    if tipo_assinatura not in ['b', 'p']:
        return None
    tipo_assinatura = 'básica' if tipo_assinatura == 'b' else 'premium'
    id_usuario = max(usuarios.keys(), default=0) + 1
    usuarios[id_usuario] = Usuario(id_usuario, nome, email, senha, tipo_assinatura, tipo_user=tipo_user)
    return id_usuario

def login_usuario(usuarios, email, senha):
    for id, usuario in usuarios.items():
        if usuario.email == email and usuario.senha == senha:
            return usuario
    return None

def excluir_usuario(usuarios, id_usuario):
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        return True
    return False

def alterar_senha(usuario, nova_senha):
    usuario.alterar_senha(nova_senha)

def adicionar_preferencia(usuario, genero):
    usuario.adicionar_preferencia(genero)

def remover_preferencia(usuario, genero):
    usuario.remover_preferencia(genero)

def adicionar_historico(usuario, id_conteudo):
    usuario.adicionar_historico(id_conteudo)

def listar_conteudos(conteudos):
    conteudo_info = []
    for id, conteudo in conteudos.items():
        conteudo_info.append(f"ID: {id}, Título: {conteudo.titulo}, Tipo: {conteudo.tipo}, Descrição: {conteudo.descricao}")
    return conteudo_info

def recomendar_conteudos(usuario, conteudos):
    preferencias = usuario.preferencias
    recomendados = []
    for id_conteudo, conteudo in conteudos.items():
        if any(genero in conteudo.generos for genero in preferencias):
            recomendados.append(f"ID: {id_conteudo}, Título: {conteudo.titulo}, Tipo: {conteudo.tipo}, Descrição: {conteudo.descricao}")
    return recomendados

# Funções para gerenciamento de usuários pelo administrador
def buscar_usuario_por_email(usuarios, email):
    for usuario in usuarios.values():
        if usuario.email == email:
            return usuario
    return None

def alterar_dados_usuario(usuario, nome=None, email=None, senha=None, tipo_assinatura=None, tipo_user=None):
    if nome:
        usuario.nome = nome
    if email:
        usuario.email = email
    if senha:
        usuario.senha = senha
    if tipo_assinatura:
        usuario.tipo_assinatura = tipo_assinatura
    if tipo_user:
        usuario.tipo_user = tipo_user

# Função para obter o próximo ID disponível em um dicionário de conteúdos
def obter_proximo_id(conteudos):
    return max(conteudos.keys(), default=0) + 1

# Funções para gerenciamento de conteúdos pelo administrador
def adicionar_conteudo(conteudos, titulo, descricao, tipo, generos):
    id_conteudo = obter_proximo_id(conteudos)
    conteudos[id_conteudo] = Conteudo(id_conteudo, titulo, descricao, tipo, generos)

def alterar_conteudo(conteudos, id, titulo=None, descricao=None, tipo=None, generos=None):
    if id in conteudos:
        if titulo:
            conteudos[id].titulo = titulo
        if descricao:
            conteudos[id].descricao = descricao
        if tipo:
            conteudos[id].tipo = tipo
        if generos:
            conteudos[id].generos = generos

def excluir_conteudo(conteudos, id):
    if id in conteudos:
        del conteudos[id]
        return True
    return False
