import json



def carregar_tarefas():
    try:
        with open('lista_tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        lista_vazia = []
        with open('lista_tarefas.json', 'w') as arquivo:
            json.dump(lista_vazia, arquivo)
    return lista_vazia


lista_tarefas = carregar_tarefas()


def add(nome, prioridade):
    novo_id = lista_tarefas[-1]['id'] + 1 if lista_tarefas else 1
    nova_tarefa = {
        'id': novo_id,
        'nome': nome,
        'prioridade': prioridade,
        'status': 'to do'
    }
    lista_tarefas.append(nova_tarefa)
    with open('lista_tarefas.json', 'w') as arquivo:
        json.dump(lista_tarefas, arquivo)


def update_nome(id, novo_nome):
    idint = int(id)
    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            tarefa['nome'] = novo_nome
            with open('lista_tarefas.json', 'w') as arquivo:
                json.dump(lista_tarefas, arquivo)
            return True



def update_prioridade(id, nova_prioridade):
    idint = int(id)
    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            tarefa['prioridade'] = nova_prioridade
            with open('lista_tarefas.json', 'w') as arquivo:
                json.dump(lista_tarefas, arquivo)
            return True


def update_status(id, novo_status):
    idint = int(id)
    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            tarefa['status'] = novo_status
            with open('lista_tarefas.json', 'w') as arquivo:
                json.dump(lista_tarefas, arquivo)
            return True

def del_task(id):
    idint = int(id)
    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            lista_tarefas.remove(tarefa)
            with open('lista_tarefas.json', 'w') as arquivo:
                json.dump(lista_tarefas, arquivo)
            return True



def all_tasks():
    for tarefa in lista_tarefas:
        print(
            f'Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}')


def done_tasks():
    for tarefa in lista_tarefas:
        if tarefa['status'] == 'done':
            print(
                f'Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}')



def undone_tasks():
    for tarefa in lista_tarefas:
        if tarefa['status'] != 'done':
            print(
                f'Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}')


def inprogress_tasks():
    for tarefa in lista_tarefas:
        if tarefa['status'] == 'in progress':
            print(
                f'Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}')