"""Gerenciador de tarefas de linha de comando do projeto TaskTracker."""

from datetime import date, datetime
import re


def ler_titulo():
    """Solicita um título até receber um texto não vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("O título é obrigatório. Digite um título válido.")


def ler_prioridade():
    """Aceita apenas as prioridades previstas no projeto."""
    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip()
        if prioridade in ("Alta", "Média", "Media", "Baixa"):
            return "Média" if prioridade == "Media" else prioridade
        print("Prioridade inválida. Digite Alta, Média (ou Media) ou Baixa.")


def ler_data_limite():
    """Solicita uma data válida no formato DD/MM/AAAA a partir de hoje."""
    while True:
        texto = input("Data limite (DD/MM/AAAA): ").strip()
        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", texto):
            print("Data inválida. Use o formato DD/MM/AAAA.")
            continue

        try:
            prazo = datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Informe uma data existente.")
            continue

        if prazo < date.today():
            print("A data limite não pode ser anterior à data de hoje.")
            continue
        return texto


def cadastrar_tarefa(tarefas, proximo_id):
    """Lê os dados, cadastra a tarefa e devolve o próximo ID disponível."""
    print("\n--- Cadastrar nova tarefa ---")
    tarefa = {
        "id": proximo_id,
        "titulo": ler_titulo(),
        "descricao": input("Descrição: "),
        "prioridade": ler_prioridade(),
        "data_limite": ler_data_limite(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"Tarefa cadastrada com sucesso! ID: {proximo_id}")
    return proximo_id + 1


def ordem_da_tarefa(tarefa):
    """Coloca pendências primeiro, por prioridade e prazo mais próximo."""
    prioridades = {"Alta": 0, "Média": 1, "Baixa": 2}
    prazo = datetime.strptime(tarefa["data_limite"], "%d/%m/%Y").date()
    return (tarefa["status"] != "Pendente", prioridades[tarefa["prioridade"]], prazo)


def listar_tarefas(tarefas):
    """Mostra todas as propriedades das tarefas cadastradas."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for tarefa in sorted(tarefas, key=ordem_da_tarefa):
        print(f"\nTarefa ID {tarefa['id']}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")

    pendentes = sum(tarefa["status"] == "Pendente" for tarefa in tarefas)
    concluidas = len(tarefas) - pendentes
    print(f"\nTotal: {pendentes} pendente(s) e {concluidas} concluída(s).")


def concluir_tarefa(tarefas):
    """Marca como concluída uma tarefa identificada pelo ID."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    listar_tarefas(tarefas)
    texto = input("ID da tarefa a concluir: ").strip()
    try:
        id_escolhido = int(texto)
    except ValueError:
        print("ID inválido. Informe um número existente.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_escolhido:
            if tarefa["status"] == "Concluída":
                print("Essa tarefa já foi concluída.")
            else:
                tarefa["status"] = "Concluída"
                print(f"Tarefa '{tarefa['titulo']}' concluída com sucesso!")
            return

    print("ID não encontrado. Nenhuma tarefa foi alterada.")


def main():
    tarefas = []
    proximo_id = 1

    while True:
        print("\n=== TaskTracker ===")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        print("4. Concluir tarefa")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = cadastrar_tarefa(tarefas, proximo_id)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Até logo!")
            break
        elif opcao == "4":
            concluir_tarefa(tarefas)
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()
