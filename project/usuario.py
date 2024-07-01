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

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha

    def adicionar_preferencia(self, genero):
        if genero not in self.preferencias:
            self.preferencias.append(genero)

    def remover_preferencia(self, genero):
        if genero in self.preferencias:
            self.preferencias.remove(genero)

    def adicionar_historico(self, id_conteudo):
        self.historico.append(id_conteudo)
        self.historico = self.historico[-3:]  # Manter apenas os três últimos itens
