import json


def carregar_tarefas():
    try:
        with open('lista_tarefas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        lista_vazia = []
        with open('lista_tarefas.json', 'w', encoding='utf-8') as arquivo:
            json.dump(lista_vazia, arquivo)
        return lista_vazia
    except json.JSONDecodeError:
        print("Erro: o arquivo lista_tarefas.json existe, mas o conteúdo dele está corrompido ou inválido.")
        return []


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
    with open('lista_tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
    return True


def update_nome(id, novo_nome):
    try:
        idint = int(id)
    except ValueError:
        print(f"Erro: '{id}' não é um id válido. Use um número inteiro.")
        return False

    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            tarefa['nome'] = novo_nome
            with open('lista_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
            return True

    print(f"Erro: nenhuma tarefa encontrada com id {idint}.")
    return False


def update_prioridade(id, nova_prioridade):
    try:
        idint = int(id)
    except ValueError:
        print(f"Erro: '{id}' não é um id válido. Use um número inteiro.")
        return False

    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            tarefa['prioridade'] = nova_prioridade
            with open('lista_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
            return True

    print(f"Erro: nenhuma tarefa encontrada com id {idint}.")
    return False


def update_status(id, novo_status):
    try:
        idint = int(id)
    except ValueError:
        print(f"Erro: '{id}' não é um id válido. Use um número inteiro.")
        return False

    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            tarefa['status'] = novo_status
            with open('lista_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
            return True

    print(f"Erro: nenhuma tarefa encontrada com id {idint}.")
    return False


def del_task(id):
    try:
        idint = int(id)
    except ValueError:
        print(f"Erro: '{id}' não é um id válido. Use um número inteiro.")
        return False

    for tarefa in lista_tarefas:
        if tarefa['id'] == idint:
            lista_tarefas.remove(tarefa)
            with open('lista_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
            return True

    print(f"Erro: nenhuma tarefa encontrada com id {idint}.")
    return False


def all_tasks():
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada ainda.")
        return

    for tarefa in lista_tarefas:
        print(
            f"Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}")


def done_tasks():
    encontrou = False
    for tarefa in lista_tarefas:
        if tarefa['status'] == 'done':
            encontrou = True
            print(
                f"Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}")
    if not encontrou:
        print("Nenhuma tarefa concluída.")


def undone_tasks():
    encontrou = False
    for tarefa in lista_tarefas:
        if tarefa['status'] != 'done':
            encontrou = True
            print(
                f"Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}")
    if not encontrou:
        print("Nenhuma tarefa pendente.")


def inprogress_tasks():
    encontrou = False
    for tarefa in lista_tarefas:
        if tarefa['status'] == 'in progress':
            encontrou = True
            print(
                f"Id: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}")
    if not encontrou:
        print("Nenhuma tarefa em andamento.")
