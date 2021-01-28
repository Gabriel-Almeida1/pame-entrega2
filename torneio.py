# Gabriel Almeida Avila e Silva
# Entrega 2 PAME 2020.2 - Python
# Sistema torneios de artes marciais

def validar_opt(opt, maiorOpt):
    n = 0
    ok = False

    if(len(opt) != 1):
        print_invalido()
        return False
    
    while(n < (maiorOpt + 1) and ok == False):
        if(opt == str(n)):
            ok = True
            return True
        n += 1
    return False


def print_invalido():
    print()
    print("Opção Inválida, tente novamente")
    print("-------------------------------")
    print()
    print()


def start_menu(): # primeiro menu exibido para o usuario
    
    print("Bem vindo ao Torneio de artes marciais!")
    print()
    print("Para acessar o Menu de Torneio digite 1")
    print("Para acessar o Menu de Lutador digite 2")
    print("Para criar um torneio aleatório digite 3")
    print("Para sair do programa, digite 4")
    print()

    maiorOpt = 4
    
    opt = input("Entre com sua escolha: ")

    ok = validar_opt(opt, maiorOpt)
        
    if(ok == True): # seleção dos menus secundários
        if(opt == '4'):
            return
        elif(opt == '1'):
            print()
            menu_torneio()
        elif(opt == '2'):
            print()
            menu_lutador()
        else:
            print()
            torneio_random()
            
    else:
        print_invalido()
        start_menu()

            

def menu_torneio(): # menu secundário de torneio
    print("--- Menu de Torneio ---")
    print()
    print("Para criar um torneio digite 1")
    print("Para inscrever um lutador digite 2")
    print("Para ver os torneios existentes digite 3")
    print("Para ver o ranking de um torneio digite 4")
    print("Para ver os lutadores inscritos em um torneio digite 5")
    print("Para realizar uma luta digite 6")
    print("Para retornar ao menu anterior digite 7")
    print("Para sair do programa, digite 8")
    print()

    maiorOpt = 8

    opt = input("Entre com sua escolha: ")
    
    ok = validar_opt(opt, maiorOpt)
        
    if(ok == True):
        if(opt == '8'):
            return
        elif(opt == '7'):
            print()
            start_menu()
        elif(opt == '1'):
            print()
            criar_torneio()
        elif(opt == '2'):
            print()
            inscrever_lutador_torneio()
        elif(opt == '3'):
            print()
            ver_torneios()
        elif(opt == '4'):
            print()
            ver_ranking()
        elif(opt == '5'):
            print()
            ver_inscritos_torneio()
        else:
            print()
            fazer_luta()
            
            
    else:
        print_invalido()
        menu_torneio()
        
    

def menu_lutador(): # menu secundário de lutador
    print("--- Menu de Lutador ---")
    print()
    print("Para cadastrar um lutador digite 1")
    print("Para ver os lutadores cadastrados digite 2")
    print("Para ver detalhes de um lutador digite 3")
    print("Para retornar ao menu anterior digite 4")
    print("Para sair do programa, digite 5")
    print()

    maiorOpt = 5

    opt = input("Entre com sua escolha: ")
    
    ok = validar_opt(opt, maiorOpt)
        
    if(ok == True):
        if(opt == '5'):
            return
        elif(opt == '4'):
            print()
            start_menu()
        elif(opt == '1'):
            print()
            cadastrar_lutador()
        elif(opt == '2'):
            print()
            ver_lutadores_cadastrados()
        else:
            print()
            ver_detalhes()
            
    else:
        print_invalido()
        menu_lutador()



def menu_random(): # menu secundário de torneio random
    print("menu_random")

# Funções do menu Torneio abaixo

def criar_torneio():
    print("criar_torneio()")

def inscrever_lutador_torneio():
    print("inscrever_lutador_torneio()")

def ver_torneios():
    print("ver_torneios()")
    
def ver_ranking():
    print("ver_ranking()")

def ver_inscritos_torneio():
    print("ver_inscritos_torneio()")

def fazer_luta():
    print("fazer_luta()")

# Funções do menu Lutador abaixo

def cadastrar_lutador():
    print("cadastrar_lutador()")

def ver_lutadores_cadastrados():
    print("ver_lutadores_cadastrados")

def ver_detalhes():
    print("ver_detalhes()")

    
# Funções Torneio Random
def torneio_random():
    print("torneio_random()")




def main():
    
    start_menu()
    
    
main()
