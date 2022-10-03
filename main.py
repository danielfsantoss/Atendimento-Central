class Atendimento:
    def __init__(self, nome, empresa, contato, resumo):
        self.nome = nome_cliente
        self.empresa = nome_empresa
        self.contato = contato_cliente
        self.resumo = resumo_atendimento
    

def confirma_escolha():
    continua_menu = input("Deseja continuar? [Y/N]: ").upper()
    while True:
        if(continua_menu == "Y"):
            menu_repeticao = 1
            break
        elif(continua_menu == "N"):
            print("ROTINA ENCERRADA!")
            arquivo.close() 
            break
        else:
            continua_menu = input("Digite 'Y' ou 'N': ").upper()


menu_repeticao = 1
escolha_menu = ""
continua_menu = "Y"
quebra_linha = "="*30

while True:
    escolha_menu = int(input("1. Incluir Registros\n2. Consultar Atendimentos\n3. Sair\nEscolha: "))
    if(escolha_menu == 1):
        while menu_repeticao == 1:
            arquivo = open("Atendimentos.py", "a")
            nome_cliente = input("NOME DO CLIENTE: ").title()
            nome_empresa = input("NOME DA EMPRESA: ").title()
            contato_cliente = int(input("NUMERO DO CLIENTE: "))
            resumo_atendimento = input("RESUMO DO ATENDIMENTO: ").title()
            atendimento = Atendimento(nome_cliente, nome_empresa, contato_cliente, resumo_atendimento)
            arquivo.writelines(f"NOME: {atendimento.nome}\nEMPRESA: {atendimento.empresa}\nCONTATO: {atendimento.contato}\nRESUMO: {atendimento.resumo}\n{quebra_linha}\n")
            arquivo.close()
            print("REGISTRO INCLUIDO!")
            confirma_escolha()
    elif(escolha_menu==2):
        arquivo = open("Atendimentos.py", "r")
        print(arquivo.readlines())
        confirma_escolha()
    elif(escolha_menu==3):
        break
# Segue
