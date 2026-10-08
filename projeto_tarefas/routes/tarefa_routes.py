from flask import Blueprint, render_template, request, redirect, url_for
from controllers.tarefa_controller import TarefaController

tarefa_bp = Blueprint('tarefa_bp', __name__)
controller = TarefaController()

@tarefa_bp.route('/')
def index():
    todas_tarefas = controller.listar_tarefas()
    pendentes = [t for t in todas_tarefas if not t.concluida]
    concluidas = [t for t in todas_tarefas if t.concluida]
    
    return render_template('index.html', pendentes=pendentes, concluidas=concluidas)

@tarefa_bp.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form.get('descricao')
    controller.adicionar_tarefa(descricao)
    return redirect(url_for('tarefa_bp.index'))

@tarefa_bp.route('/concluir/<int:id>')
def concluir(id):
    controller.concluir_tarefa(id)
    return redirect(url_for('tarefa_bp.index'))

@tarefa_bp.route('/remover/<int:id>')
def remover(id):
    controller.remover_tarefa(id)
    return redirect(url_for('tarefa_bp.index'))
