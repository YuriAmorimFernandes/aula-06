from models.tarefa import Tarefa

class TarefaController:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, descricao):
        if descricao and descricao.strip():
            nova_tarefa = Tarefa(self.proximo_id, descricao.strip())
            self.tarefas.append(nova_tarefa)
            self.proximo_id += 1

    def listar_tarefas(self):
        return self.tarefas

    def remover_tarefa(self, id_tarefa):
        self.tarefas = [t for t in self.tarefas if t.id != id_tarefa]

    def concluir_tarefa(self, id_tarefa):
        for t in self.tarefas:
            if t.id == id_tarefa:
                t.marcar_como_concluida()
                break
