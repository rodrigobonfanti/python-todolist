import json

def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    try: 
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

tarefas = carregar_tarefas()

while True:
    print("\n1 - Adicionar Tarefas")
    print("2 - Ver Tarefas")
    print("3 - Remover Tarefas")
    print("4 - Sair")
    print("5 - Editar tarefa")
    print("6 - Marcar como conclusa")

    opcao = input("Escolha uma opção:")
    
    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append({
            "texto": tarefa, 
            "concluida": False
            })
        salvar_tarefas()
        print("Tarefa adicionada!")

    elif opcao == "2":
        print("\nLista de tarefas: ")
        for i, tarefa in enumerate(tarefas):
            if tarefa["concluida"]:
                status = "[x]"
            else:
                status = "[ ]"
            
            print(i, status, tarefa["texto"])
        
    elif opcao == "3":
        indice = int(input("Numero da tarefa para remover: "))
        tarefas.pop(indice)
        salvar_tarefas()

    elif opcao == "5":
        print("\nLista de tarefas:")

        for i, tarefa in enumerate(tarefas):
            status = "[x]" if tarefa["concluida"] else "[ ]"
            print(i, status, tarefa["texto"])

        indice = int(input("Numero da tarefa que deseja editar: "))

        nova_tarefa = input("Digite a nova tarefa: ")

        tarefas[indice]["texto"] = nova_tarefa
        
        salvar_tarefas()

        print("Tarefa atualizada!")


    elif opcao == "6":
        print("\nLista de tarefas:")

        for i, tarefa in enumerate(tarefas):
            status = "[x]" if tarefa["concluida"] else "[ ]"
            print(i, status, tarefa["texto"])

        indice = int(input("Número da tarefa conclusa: "))

        tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]
        salvar_tarefas()
        print("Tarefa conclusa com sucesso!")        
        

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")