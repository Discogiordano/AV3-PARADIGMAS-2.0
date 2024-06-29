from usuario import Usuario

def cadastrar_usuario(usuarios, nome, email, senha, tipo_assinatura):
    if tipo_assinatura in ['b', 'p']:
        tipo_assinatura = 'básica' if tipo_assinatura == 'b' else 'premium'
        id_usuario = max(usuarios.keys(), default=0) + 1
        usuario = Usuario(id_usuario, nome, email, senha, tipo_assinatura)
        usuarios[id_usuario] = usuario
        return True
    else:
        return False

def login_usuario(usuarios, email, senha):
    email = email.lower()
    print(f"Tentativa de login: {email}, {senha}")
    for usuario in usuarios.values():
        print(f"Verificando usuário: {usuario.email}, {usuario.senha}")
        if usuario.email == email and usuario.senha == senha:
            print("Login bem-sucedido para o usuário:", usuario.nome)
            return usuario
    return None

def excluir_usuario(usuarios, usuario):
    if usuario:
        del usuarios[usuario.id]
        return True
    return False

def alterar_senha(usuario, nova_senha):
    usuario.senha = nova_senha

def adicionar_preferencia(usuario, genero):
    if genero not in usuario.preferencias:
        usuario.preferencias.append(genero)

def remover_preferencia(usuario, genero):
    if genero in usuario.preferencias:
        usuario.preferencias.remove(genero)

def adicionar_historico(usuario, id_conteudo):
    usuario.historico.append(id_conteudo)
    usuario.historico = usuario.historico[-3:]

def listar_conteudos(conteudos):
    conteudo_info = []
    for conteudo in conteudos.values():
        conteudo_info.append(f"ID: {conteudo.id}, Título: {conteudo.titulo}, Tipo: {conteudo.tipo}, Descrição: {conteudo.descricao}")
    return conteudo_info

def recomendar_conteudos(usuario, conteudos):
    if not usuario.preferencias:
        return []

    recomendados = []
    for conteudo in conteudos.values():
        if any(genero in conteudo.generos for genero in usuario.preferencias):
            recomendados.append(f"ID: {conteudo.id}, Título: {conteudo.titulo}, Tipo: {conteudo.tipo}, Descrição: {conteudo.descricao}")

    return recomendados

