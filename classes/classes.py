tarefas = [
    {"Id": 1, "Nome": "lavar o carro", "Prioridade": "alta", "Status": "To_do"},
    {"Id": 2, "Nome": "estudar POO", "Prioridade": "alta", "Status": "In_progress"},
    {"Id": 3, "Nome": "ir dormir", "Prioridade": "baixa", "Status": "To_do"},
    {"Id": 4, "Nome": "comprar pão", "Prioridade": "media", "Status": "Done"},
    {"Id": 5, "Nome": "responder email", "Prioridade": "media", "Status": "To_do"},
]

def add_Tarefa(tarefa, prioridade):
        novo_id = tarefas[-1]["Id"] + 1 if tarefas else 1

        lista_tarefas = {
              "Id" : novo_id,
              "Nome" : tarefa,
              "Prioridade" : prioridade,
              "Status" : "To_do"
        }
        tarefas.append(lista_tarefas)
        return tarefa

def apresentar_lista():
    for c in range(len(tarefas)):
         print(tarefas[c])

def select_status(id_tarefa, status):
    conversor = int(id_tarefa)
    for tarefa in tarefas:
        if tarefa["Id"] == conversor:
            tarefa["Status"] = status
            return True
    return False

def conluida(id_tarefa):
    conversor = int(id_tarefa)
    for tarefa in tarefas:
        if tarefa["Id"] == conversor:
            tarefa["Status"] = "Done"
            return True
    return False

def del_tarefa(id_tarefa):
    conversor = int(id_tarefa)
    for tarefa in tarefas:
        if tarefa["Id"] == conversor:
            tarefas.remove(tarefa)
            return True
    return False