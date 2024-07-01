from usuario import Usuario
from conteudo import Conteudo

def cadastrar_usuario(usuarios, nome, email, senha, tipo_assinatura):
    if email in [user.email for user in usuarios.values()]:
        return False
    novo_id = obter_proximo_id(usuarios)
    novo_usuario = Usuario(novo_id, nome, email, senha, tipo_assinatura)
    usuarios[novo_id] = novo_usuario
    return True

def login_usuario(usuarios, email, senha):
    for user in usuarios.values():
        if user.email == email and user.senha == senha:
            return user
    return None

def excluir_usuario(usuarios, id_usuario):
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        return True
    return False

def alterar_senha(usuario, nova_senha):
    usuario.senha = nova_senha


def adicionar_historico(usuario, id_conteudo):
    if id_conteudo not in usuario.historico:
        usuario.historico.append(id_conteudo)
        
def adicionar_preferencia(usuario, genero):
    if genero not in usuario.preferencias:
        usuario.preferencias.append(genero)
        print(f"Preferência '{genero}' adicionada para o usuário '{usuario.nome}'.")

def remover_preferencia(usuario, genero):
    if genero in usuario.preferencias:
        usuario.preferencias.remove(genero)
        print(f"Preferência '{genero}' removida para o usuário '{usuario.nome}'.")

def recomendar_conteudos(usuario, conteudos):
    recomendados = []
    for conteudo in conteudos.values():
        for genero in conteudo.generos:
            if genero in usuario.preferencias:
                recomendados.append(conteudo)
                break
    return recomendados

def listar_conteudos(conteudos):
    return [f"ID: {conteudo.id}, Título: {conteudo.titulo}" for conteudo in conteudos.values()]


def buscar_usuario_por_email(usuarios, email):
    for user in usuarios.values():
        if user.email == email:
            return user
    return None

def alterar_dados_usuario(usuario, nome, email, senha, tipo_assinatura, tipo_user):
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

def adicionar_conteudo(conteudos, titulo, descricao, tipo, generos):
    novo_id = obter_proximo_id(conteudos)
    novo_conteudo = Conteudo(novo_id, titulo, descricao, tipo, generos)
    conteudos[novo_id] = novo_conteudo

def alterar_conteudo(conteudos, id_conteudo, titulo, descricao, tipo, generos):
    conteudo = conteudos.get(id_conteudo)
    if conteudo:
        if titulo:
            conteudo.titulo = titulo
        if descricao:
            conteudo.descricao = descricao
        if tipo:
            conteudo.tipo = tipo
        if generos:
            conteudo.generos = generos

def excluir_conteudo(conteudos, id_conteudo):
    if id_conteudo in conteudos:
        del conteudos[id_conteudo]
        return True
    return False

def obter_proximo_id(dicionario):
    if not dicionario:
        return 1
    else:
        return max(dicionario.keys()) + 1
