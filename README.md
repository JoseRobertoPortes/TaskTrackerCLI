# TaskTrackerCLI

Gerenciador de tarefas simples via linha de comando, feito em Python.

## Funcionalidades

- Listar tarefas (`view`)
- Adicionar tarefa com prioridade (`add`)
- Atualizar o status de uma tarefa (`priority`)
- Remover uma tarefa (`del`)

Cada tarefa tem: `Id`, `Nome`, `Prioridade` e `Status` (`To_do`, `In_progress`, `Done`).

## Como executar

Dentro da pasta do projeto:

```bash
python -m TaskTrackerCLI view
python -m TaskTrackerCLI add "lavar o carro" alta
python -m TaskTrackerCLI priority 1 Done
python -m TaskTrackerCLI del 1
```

## Estrutura

- `__main__.py` — ponto de entrada, interpreta os comandos passados por linha de comando
- `classes/classes.py` — lógica de manipulação das tarefas (adicionar, listar, atualizar status, remover)

## Tecnologias

- Python 3
