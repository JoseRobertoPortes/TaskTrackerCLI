# TaskTrackerCLI

Gerenciador de tarefas simples via linha de comando, feito em Python.

## Funcionalidades

- Listar tarefas (`view`)
- Adicionar tarefa com prioridade (`add`)
- Atualizar o status de uma tarefa (`priority`)
- Remover uma tarefa (`del`)

Cada tarefa tem: `Id`, `Nome`, `Prioridade` e `Status` (`To_do`, `In_progress`, `Done`).

## Como executar

O programa lê e escreve o arquivo `lista_tarefas.json` usando um caminho relativo à pasta atual do terminal — por isso é necessário estar **dentro** da pasta `TaskTrackerCLI` ao rodar os comandos.

```bash
cd TaskTrackerCLI

python __main__.py view
python __main__.py add "lavar o carro" alta
python __main__.py priority 1 Done
python __main__.py del 1
```

## Estrutura

- `__main__.py` — ponto de entrada, interpreta os comandos passados por linha de comando
- `classes/classes.py` — lógica de manipulação das tarefas (adicionar, listar, atualizar status, remover)
- `lista_tarefas.json` — arquivo onde as tarefas são persistidas entre execuções

## Tecnologias

- Python 3
