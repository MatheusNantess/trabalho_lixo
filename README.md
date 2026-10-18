# TaskTracker — Bootcamp II, Fase 2

O TaskTracker é um gerenciador de tarefas executado no terminal. Ele permite cadastrar atividades, consultar o que está pendente ou concluído e marcar tarefas como concluídas. Esta implementação transforma em Python o [planejamento lógico da Fase 1](docs/planejamento_logico.pdf).

## Funcionalidades

- Cadastro com título, descrição, prioridade e data limite. Cada tarefa recebe um ID numérico crescente e começa com status **Pendente**.
- Título obrigatório: entradas vazias ou formadas apenas por espaços são recusadas.
- Prioridade limitada a **Alta**, **Média** (também aceita `Media`) e **Baixa**.
- Data limite no formato `DD/MM/AAAA`, com verificação de data válida e de prazo não anterior ao dia do cadastro.
- Listagem com todas as propriedades da tarefa, pendentes antes das concluídas. As pendentes aparecem por prioridade e, em caso de empate, por prazo. Ao final são mostrados os totais de pendentes e concluídas.
- Conclusão por ID, com aviso para ID inexistente ou tarefa já concluída.

## Tecnologias

- Python 3 e sua biblioteca padrão.
- Git para o histórico de desenvolvimento.

## Estrutura

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Como executar

É necessário ter Python 3 instalado. Não há dependências externas nem etapa de instalação de pacotes. No terminal, entre na pasta `tasktracker-projeto` e execute:

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

Exemplo de cadastro: título `Entregar atividade`, descrição `Revisar o PDF`, prioridade `Alta` e data limite `20/12/2026`.

## Limitações desta fase

As tarefas ficam somente na memória do programa. Ao sair, os cadastros e as alterações de status são perdidos. Esta versão funciona localmente no terminal e não possui banco de dados nem interface gráfica.
