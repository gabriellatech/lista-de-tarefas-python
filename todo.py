import os

TAREFAS_ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    if not os.path.exists(TAREFAS_ARQUIVO):
        return []
    with open(TAREFAS_ARQUIVO, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

def salvar_tarefas(tarefas):
    with open(TAREFAS_ARQUIVO, "w", encoding="utf-8") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

def exibir_menu():
    print("\n=== LISTA DE TAREFAS ===")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")

def adicionar_tarefa(tarefas):
    nova = input("\nDigite a nova tarefa: ").strip()
    if nova:
        tarefas.append(f"[ ] {nova}")
        print("Tarefa adicionada!")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("\nN° da tarefa para marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            if tarefas[indice].startswith("[ ]"):
                tarefas[indice] = tarefas[indice].replace("[ ]", "[x]", 1)
                print("Tarefa marcada como concluída!")
            else:
                print("Essa tarefa já está concluída.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("\nN° da tarefa para remover: ")) - 1
        if 0 <= indice < len(tarefas):
            confirm = input(f"Deseja remover '{tarefas[indice]}'? (s/n): ").lower()
            if confirm == 's':
                tarefas.pop(indice)
                print("Tarefa removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def main():
    tarefas = carregar_tarefas()

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("\nTarefas salvas. Até a próxima!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
