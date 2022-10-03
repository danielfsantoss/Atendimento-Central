class Atendimento:
    def guardar_cliente_atendido():
        cliente_atendido = [{'nome': nome_cliente, 'contato': contato_cliente}]
    


menu_repeticao = 1
escolha_menu = "Y"

while menu_repeticao == 1:
    print("Incluir mais um atendimento? [Y/N]")
    escolha_menu = input("").upper()
    if(escolha_menu == "Y"):
        nome_cliente = input("Digite o nome do cliente: ")
        contato_cliente = int(input("Digite o número do cliente: "))
        print("CADASTRO INCLUIDO!")
    elif(escolha_menu == "N"):
        print("ROTINA ENCERRADA!")
        menu_repeticao-=1
