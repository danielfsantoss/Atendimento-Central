menu_repeticao = 1
escolha_menu = ""
continua_menu = "Y"
quebra_linha = "="*30

class Atendimento:
    def __init__(self, nome, empresa, contato, resumo):
        self.nome = nome_cliente
        self.empresa = nome_empresa
        self.contato = contato_cliente
        self.resumo = resumo_atendimento
    

def confirma_escolha(): # Erro semântico
    continua_menu = input("Deseja continuar? [Y/N]: ").upper()
    if(continua_menu == "N"):
        print("ROTINA ENCERRADA!")
        global menu_repeticao
        menu_repeticao = 0
    return 0


def gerar_txt():
    arquivo = open("Atendimentos.txt", "a")
    arquivo.writelines(f"NOME: {atendimento.nome}\nEMPRESA: {atendimento.empresa}\nCONTATO: {atendimento.contato}\nRESUMO: {atendimento.resumo}\n{quebra_linha}\n")
    arquivo.close()
    return 0


def gerar_csv():
    return 0


while True:
    escolha_menu = int(input("1. Incluir Registros\n2. Consultar Atendimentos\n3. Sair\nEscolha: "))
    if(escolha_menu == 1):
        while menu_repeticao == 1:
            nome_cliente = input("NOME DO CLIENTE: ").title()
            nome_empresa = input("NOME DA EMPRESA: ").title()
            contato_cliente = int(input("NUMERO DO CLIENTE: "))
            resumo_atendimento = input("RESUMO DO ATENDIMENTO: ").title()
            atendimento = Atendimento(nome_cliente, nome_empresa, contato_cliente, resumo_atendimento)
            print("REGISTRO INCLUIDO!")
            confirma_escolha()
    elif(escolha_menu==2):
        formato_arquivo = int(input(""))
        """
        arquivo = open("Atendimentos.txt", "r")
        print(arquivo.readlines())
        confirma_escolha()
        """ # GERAR TXT DIRETO
    elif(escolha_menu==3):
        break
# Segue