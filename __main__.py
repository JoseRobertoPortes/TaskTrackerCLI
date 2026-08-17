from classes.classes import *
import sys

COMANDOS = ["list", "add", "upnome", "uppriority", "upstatus", "del", "undone", "done", "inprogress"]

ARGUMENTOS_NECESSARIOS = {
    "add": 2,
    "upnome": 2,
    "uppriority": 2,
    "upstatus": 2,
    "del": 1,
}


def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum comando informado.")
        print(f"Comandos disponíveis: {', '.join(COMANDOS)}")
        return

    comando = sys.argv[1]

    if comando not in COMANDOS:
        print(f"Erro: comando '{comando}' não existe.")
        print(f"Comandos disponíveis: {', '.join(COMANDOS)}")
        return

    esperado = ARGUMENTOS_NECESSARIOS.get(comando, 0)
    recebido = len(sys.argv) - 2
    if recebido < esperado:
        print(f"Erro: o comando '{comando}' precisa de {esperado} argumento(s), mas recebeu {recebido}.")
        return

    if comando == "list":
        all_tasks()
    elif comando == "add":
        add(sys.argv[2], sys.argv[3])
    elif comando == "upnome":
        update_nome(sys.argv[2], sys.argv[3])
    elif comando == "uppriority":
        update_prioridade(sys.argv[2], sys.argv[3])
    elif comando == "upstatus":
        update_status(sys.argv[2], sys.argv[3])
    elif comando == "del":
        del_task(sys.argv[2])
    elif comando == "undone":
        undone_tasks()
    elif comando == "done":
        done_tasks()
    elif comando == "inprogress":
        inprogress_tasks()


if __name__ == '__main__':
    main()
