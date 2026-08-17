from classes.classes import *
import sys

def main():
    if sys.argv[1] == "list":
        all_tasks()
    elif sys.argv[1] == "add":
        add(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "upnome":
        update_nome(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "uppriority":
        update_prioridade(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "upstatus":
        update_status(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "del":
            del_task(sys.argv[2])


    elif sys.argv[1] == "undone":
            undone_tasks()


    elif sys.argv[1] == "done":
            done_tasks()

    elif sys.argv[1] == "inprogress":
            inprogress_tasks()


if __name__ == '__main__':
    main()
