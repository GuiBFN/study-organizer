from src.manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n--- Study Organizer ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o nome da tarefa: ")
            try:
                manager.add_task(titulo)
                print("Tarefa adicionada com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            tarefas = manager.list_tasks()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i} - {tarefa.title}")

        elif opcao == "3":
            try:
                indice = int(input("Digite o índice da tarefa: "))
                manager.remove_task(indice)
                print("Tarefa removida com sucesso!")
            except (ValueError, IndexError):
                print("Índice inválido.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()