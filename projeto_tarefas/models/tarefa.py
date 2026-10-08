
class Tarefa:
    def __init__(self, id_tarefa, descricao):
        self.id = id_tarefa
        self.descricao = descricao
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True

    def atualizar_descricao(self, nova_descricao):
        self.descricao = nova_descricao
