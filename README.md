# TaskTrackerCLI

Gerenciador de tarefas simples via linha de comando, feito em Python.

## Funcionalidades

- Listar todas as tarefas (`list`)
- Adicionar tarefa com prioridade (`add`)
- Atualizar o nome de uma tarefa (`upnome`)
- Atualizar a prioridade de uma tarefa (`uppriority`)
- Atualizar o status de uma tarefa (`upstatus`)
- Remover uma tarefa (`del`)
- Listar tarefas concluídas (`done`)
- Listar tarefas não concluídas (`undone`)
- Listar tarefas em andamento (`inprogress`)

Cada tarefa tem: `id`, `nome`, `prioridade` (`alta`, `media`, `baixa`) e `status` (`to do`, `in progress`, `done`).

## Como executar

O programa lê e escreve o arquivo `lista_tarefas.json` usando um caminho relativo à pasta atual do terminal — por isso é necessário estar **dentro** da pasta do projeto ao rodar os comandos. Se o arquivo ainda não existir, ele é criado automaticamente na primeira execução.

```bash
cd TaskTrackerCLI

python __main__.py list
python __main__.py add "lavar o carro" alta
python __main__.py upnome 1 "lavar o carro e a moto"
python __main__.py uppriority 1 baixa
python __main__.py upstatus 1 done
python __main__.py del 1
python __main__.py done
python __main__.py undone
python __main__.py inprogress
```

## Estrutura

- `__main__.py` — ponto de entrada, interpreta os comandos passados por linha de comando
- `classes/classes.py` — lógica de manipulação das tarefas (adicionar, listar, filtrar por status, atualizar, remover)
- `lista_tarefas.json` — arquivo onde as tarefas são persistidas entre execuções

## Tecnologias

- Python 3
