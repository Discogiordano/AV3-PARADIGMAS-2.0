from usuario import Usuario

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
