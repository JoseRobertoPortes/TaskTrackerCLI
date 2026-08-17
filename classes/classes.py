import json

def carregar_tarefas():
    with open('lista_tarefas.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo, ensure_ascii=False)

lista_tarefas = carregar_tarefas()


def add_Tarefa(tarefa, prioridade):
    novo_id = lista_tarefas[-1]["Id"] + 1 if lista_tarefas else 1
    tarefa_atual = {
        "Id": novo_id,
        "Nome": tarefa,
        "Prioridade": prioridade,
        "Status": "To_do"
    }
    lista_tarefas.append(tarefa_atual)
    with open('lista_tarefas.json', "w", encoding='utf-8') as arquivo:
        json.dump(lista_tarefas,arquivo, ensure_ascii=False)
    return tarefa


def apresentar_lista():
    for c in range(len(lista_tarefas)):
        print(lista_tarefas[c])


def select_status(id_tarefa, status):
    conversor = int(id_tarefa)
    for tarefa in lista_tarefas:
        if tarefa["Id"] == conversor:
            tarefa["Status"] = status
            with open('lista_tarefas.json', "w", encoding='utf-8') as arquivo:
                json.dump(lista_tarefas, arquivo, ensure_ascii=False)
            return True
    return False

def del_tarefa(id_tarefa):
    conversor = int(id_tarefa)
    for tarefa in lista_tarefas:

        if tarefa["Id"] == conversor:
            lista_tarefas.remove(tarefa)
            with open('lista_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_tarefas,arquivo, ensure_ascii=False)

            return True
    return False


