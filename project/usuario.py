class Usuario:
    def __init__(self, id, nome, email, senha, tipo_assinatura, preferencias=None, historico=None, tipo_user='usuário'):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura
        self.preferencias = preferencias if preferencias is not None else []
        self.historico = historico if historico is not None else []
        self.tipo_user = tipo_user
