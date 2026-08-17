from classes.classes import *
import sys
import json


def main():

    if sys.argv[1] == "view":
        apresentar_lista()
    elif sys.argv[1] == "add":
        add_Tarefa(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "priority":
        select_status(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "del":
        del_tarefa(sys.argv[2])


if __name__ == "__main__":
    main()

