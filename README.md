# TaskTracker — Bootcamp II, Fase 3

O TaskTracker é um gerenciador de tarefas executado no terminal. Ele permite cadastrar atividades, consultar o que está pendente ou concluído e marcar tarefas como concluídas. Esta implementação transforma em Python o [planejamento lógico da Fase 1](docs/planejamento_logico.pdf) e, na Fase 3, empacota a aplicação em um container Docker para que ela rode de forma idêntica em qualquer ambiente.

## Funcionalidades

- Cadastro com título, descrição, prioridade e data limite. Cada tarefa recebe um ID numérico crescente e começa com status **Pendente**.
- Título obrigatório: entradas vazias ou formadas apenas por espaços são recusadas.
- Prioridade limitada a **Alta**, **Média** (também aceita `Media`) e **Baixa**.
- Data limite no formato `DD/MM/AAAA`, com verificação de data válida e de prazo não anterior ao dia do cadastro.
- Listagem com todas as propriedades da tarefa, pendentes antes das concluídas. As pendentes aparecem por prioridade e, em caso de empate, por prazo. Ao final são mostrados os totais de pendentes e concluídas.
- Conclusão por ID, com aviso para ID inexistente ou tarefa já concluída.

## Tecnologias

- Python 3.11 e sua biblioteca padrão.
- Git para o histórico de desenvolvimento.
- Docker e Docker Compose para empacotar e executar a aplicação.

## Estrutura

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf      # Planejamento da Fase 1
├── src/
│   └── main.py                      # Código Python da Fase 2
├── Dockerfile                       # Receita da imagem (Fase 3)
└── docker-compose.yml               # Execução interativa (Fase 3)
```

## Como executar com Docker (recomendado)

É necessário ter o [Docker](https://docs.docker.com/get-docker/) instalado e em execução. Todos os comandos abaixo devem ser executados na raiz do repositório, onde estão o `Dockerfile` e o `docker-compose.yml`.

### 1. Construir a imagem

```bash
docker build -t tasktracker .
```

### 2. Rodar o container em modo isolado

```bash
docker run -it --rm tasktracker
```

O `-it` liga o teclado ao container e cria um terminal virtual, o que é necessário porque o menu usa `input()`. O `--rm` remove o container ao sair.

### 3. Rodar via orquestração (recomendado)

```bash
docker compose run --rm tasktracker
```

O `docker compose run` constrói a imagem caso ela ainda não exista. No `docker-compose.yml`, as opções `stdin_open: true` e `tty: true` fazem o mesmo papel do `-it`. Para reconstruir a imagem depois de alterar o código, use `docker compose build`.

### O que o Dockerfile faz

| Instrução | Função |
| --- | --- |
| `FROM python:3.11-slim` | Usa uma imagem base leve com Python. |
| `WORKDIR /app` | Define a pasta de trabalho dentro do container. |
| `ENV PYTHONUNBUFFERED=1` | Mostra a saída do Python no terminal sem atraso. |
| `ENV TZ=America/Sao_Paulo` | Usa o horário de Brasília na validação da data limite. |
| `COPY src/ /app/src/` | Copia apenas o código da aplicação para a imagem. |
| `CMD ["python", "src/main.py"]` | Inicia o menu do TaskTracker. |

## Como executar sem Docker

Também é possível rodar direto com Python 3, sem dependências externas:

```bash
python src/main.py
```

No Windows, se o comando `python` não apontar para Python 3, use `py -3 src/main.py`.

## Como usar

O menu é exibido continuamente até a escolha de saída:

1. **Cadastrar nova tarefa:** informe título, descrição, prioridade e data limite. O programa repete as perguntas de campos obrigatórios enquanto o valor for inválido.
2. **Visualizar tarefas cadastradas:** consulte os dados de cada tarefa e a contagem por status. Se a lista estiver vazia, o programa informa isso.
3. **Sair da aplicação:** encerre o programa.
4. **Concluir tarefa:** informe o ID de uma tarefa existente e pendente para alterar seu status para **Concluída**.

A opção **3. Sair** segue o menu exigido na Fase 2. A opção **4. Concluir tarefa** preserva a funcionalidade prevista no planejamento da Fase 1.

Exemplo de cadastro: título `Entregar atividade`, descrição `Revisar o PDF`, prioridade `Alta` e data limite `20/12/2026`.

## Apresentação em vídeo

- Fase 3 (Docker): _link a ser adicionado_
- [Fase 2 (Python e Git)](https://youtu.be/DomRQztjaBw)

## Limitações

As tarefas ficam somente na memória do programa. Ao sair, os cadastros e as alterações de status são perdidos. Esta versão funciona no terminal, localmente ou em container, e não possui banco de dados nem interface gráfica.
