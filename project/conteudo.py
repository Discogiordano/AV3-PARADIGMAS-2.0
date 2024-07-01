class Conteudo:
    def __init__(self, id, titulo, descricao, tipo, generos):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.tipo = tipo
        self.generos = [genero.lower() for genero in generos]
