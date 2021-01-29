# Gabriel Almeida Avila e Silva
# Entrega 2 PAME 2020.2 - Python
# Sistema torneios de artes marciais

import sys
import random

def validar_opt(opt, maiorOpt):
    n = 0
    ok = False

    if(len(opt) != 1):
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


def start_menu(lutadores, torneios): # primeiro menu exibido para o usuario
    
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
            sys.exit()
        elif(opt == '1'):
            print()
            menu_torneio(lutadores, torneios)
        elif(opt == '2'):
            print()
            menu_lutador(lutadores, torneios)
        else:
            print()
            torneio_random(lutadores, torneios)
            
    else:
        print_invalido()
        start_menu()
            

def menu_torneio(lutadores, torneios): # menu secundário de torneio
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
            sys.exit()
        elif(opt == '7'):
            print()
            start_menu(lutadores, torneios)
        elif(opt == '1'):
            print()
            criar_torneio(lutadores, torneios)
        elif(opt == '2'):
            print()
            inscrever_lutador_torneio(lutadores, torneios)
        elif(opt == '3'):
            print()
            ver_torneios(lutadores, torneios)
        elif(opt == '4'):
            print()
            ver_ranking(lutadores, torneios)
        elif(opt == '5'):
            print()
            ver_inscritos_torneio(lutadores, torneios)
        else:
            print()
            fazer_luta(lutadores, torneios)
            
            
    else:
        print_invalido()
        menu_torneio(lutadores, torneios)
        
    

def menu_lutador(lutadores, torneios): # menu secundário de lutador
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
            sys.exit() 
        elif(opt == '4'):
            print()
            start_menu(lutadores, torneios)
        elif(opt == '1'):
            print()
            cadastrar_lutador(lutadores, torneios)
        elif(opt == '2'):
            print()
            ver_lutadores_cadastrados(lutadores, torneios)
        else:
            print()
            ver_detalhes(lutadores, torneios)
            
    else:
        print_invalido()
        menu_lutador(lutadores, torneios)


def menu_random(): # menu secundário de torneio random
    print("menu_random")

# Funções do menu Torneio abaixo

def criar_torneio(lutadores, torneios):
    ok = False

    torneios.append(torneio())
    
    nome = input("Nome do torneio: ")
    while(ok == False):
        if(nome != ''):
            ok = True
        else:
            print("\nNome inválido\n")
            nome = input("Nome do torneio: ")
    ok = False
    torneios[-1].nome = nome


    estiloLuta = input("Arte marcial do torneio: ")
    while(ok == False):
        if(estiloLuta != ''):
            ok = True
        else:
            print("\nArte Marcial inválida\n")
            estiloLuta = input("Arte Marcial do torneio: ")
    ok = False
    torneios[-1].estiloLuta = estiloLuta

 
    print("Diga as faixas de peso permitidas no torneio:")
    print("Exemplo:\n\nDe: 80\nAté: 90\n")
    controle = False
    while(controle == False):
        
        while(ok == False):
            peso_inicial = input("De: ")
            peso_final = input("Até: ")
            try:
                peso_inicial = float(peso_inicial)
                peso_final = float(peso_final)
                if(peso_inicial < peso_final):
                    ok = True
                else:
                    print("Faixa Inválida. O primeiro peso inserido deve ser menor do que o segundo\n")
            except:
                print("\nPeso inválido. Lembre-se, o primeiro peso deve ser menor do que o segundo inserido\n")
        ok = False
        torneios[-1].pesos.append([peso_inicial,peso_final])
        
        resp = input("Deseja adicionar mais faixas de peso?(s/n) ")
        if(resp == 'n'):
            controle = True
    
    print("Diga as faixas permitidas no torneio: ")
    controle = False
    while(controle == False):
        faixa = input("Faixa: ")
        while(ok == False):
            if(faixa != ''):
                ok = True
            else:
                print("\nFaixa inválida\n")
                faixa = input("Faixa: ")
        ok = False
        torneios[-1].faixas.append(faixa)
        
        resp = input("Deseja adicionar mais faixas?(s/n) ")
        if(resp == 'n'):
            controle = True
            
    print("\nTorneio Criado!\n")
    menu_torneio(lutadores, torneios)

def inscrever_lutador_torneio(lutadores, torneios):

    lutador = input("Entre com o nome do lutador que você quer inscrever: ")
    ok = False
    while(ok == False):
        if(lutador != ''):
            ok = True
        else:
            print("\nNome inválido\n")
            lutador = input("Nome do lutador: ")

    achou = False
    for count in range(0,len(lutadores),1):
        if(lutadores[count].nome == lutador):
            inscrito = lutadores[count]
            achou = True
            break

    if(achou == False):
        print("\nLutador não cadastrado, por favor cadastre-o antes\n")
        menu_lutador(lutadores, torneios)    


    torneio = input("Entre com o torneio que este lutador deve ser inscrito: ")
    ok = False
    while(ok == False):
        if(torneio != ''):
            ok = True
        else:
            print("\nTorneio inválido\n")
            torneio = input("Torneio: ")

    achou = False
    for count in range(0,len(torneios),1):
        if(torneios[count].nome == torneio):
            validacao = validar_candidato(inscrito, torneios[count])
            if(validacao == True):
                torneios[count].lutadores_inscritos.append(inscrito)
                torneios[count].vitorias.append([inscrito,0])
                torneios[count].derrotas.append([inscrito,0])
            achou = True
            break

    if(achou == False):
        print("\nTorneio não criado, por favor, o crie antes\n")
        menu_torneio(lutadores, torneios)
    elif(achou == True and validacao == False):
        print("\nLutador não qualificado para este torneio. Tente outros torneios.\n")
        menu_torneio(lutadores, torneios)
    
    print("\nLutador Inscrito!\n")
    menu_torneio(lutadores, torneios)

def validar_candidato(inscrito, torneio):
    achouFaixa = False
    achouPeso = False
    for count in range(0,len(torneio.faixas),1):
        if(inscrito.faixa == torneio.faixas[count]):
            achouFaixa = True
            break
    for count in range(0,len(torneio.pesos),1):
        if(inscrito.peso >= torneio.pesos[count][0] and inscrito.peso <= torneio.pesos[count][1]):
            achouPeso = True
            break
        
    if(achouPeso == True and achouFaixa == True and inscrito.estiloLuta == torneio.estiloLuta):
        return True
    else:
        return False   

def ver_torneios(lutadores, torneios):
    for count in range(0,len(torneios),1):
        print(f"Torneio {torneios[count].nome}\n")
    menu_torneio(lutadores, torneios)
    
    
def ver_ranking(lutadores, torneios):
    torneio = input("Entre com o nome do torneio desejado: ")
    ok = False
    while(ok == False):
        if(torneio != ''):
            ok = True
        else:
            print("\nTorneio inválido\n")
            torneio = input("Torneio: ")
    achou = False
    print("1")
    for count in range(0, len(torneios), 1):
        print("2")
        if(torneio == torneios[count].nome):
            print("3")
            achou = True
            mergeSort(torneios[count].vitorias)
            for count2 in range(len(torneios[count].vitorias)-1,-1,-1):
                print(f"Colocado {len(torneios[count].vitorias)-count2}: {torneios[count].vitorias[count2][0].nome} com {torneios[count].vitorias[count2][1]} vitórias")

    if(achou == False):
        print("\nTorneio não criado, por favor, o crie antes\n")
    menu_torneio(lutadores, torneios)


def mergeSort(arr): # Algoritmo eficiente de sorting
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def ver_inscritos_torneio(lutadores, torneios):
    
    torneio = input("Entre com o nome do torneio desejado: ")
    ok = False
    while(ok == False):
        if(torneio != ''):
            ok = True
        else:
            print("\nTorneio Inválido.\n")
            torneio = input("Torneio: ")
    achou = False

    for count in range(0, len(torneios), 1):

        if(torneio == torneios[count].nome):

            achou = True
            for count2 in range(0, len(torneios[count].lutadores_inscritos),1):
                print(f"Lutador {count2+1}: {torneios[count].lutadores_inscritos[count2].nome}")

    if(achou == False):
        print("\nTorneio não criado, por favor, o crie antes\n")
    menu_torneio(lutadores, torneios)

def fazer_luta(lutadores, torneios):
    torneio = input("Entre com o nome do torneio desejado: ")
    ok = False
    while(ok == False):
        if(torneio != ''):
            ok = True
        else:
            print("\nTorneio Inválido.\n")
            torneio = input("Torneio: ")
    achou = False
    for count in range(0, len(torneios), 1):
        if(torneio == torneios[count].nome):
            pos0 = count
            achou = True
            ok = False
    
            lutador1 = input("Nome do lutador 1: ")
            while(ok == False):
                if(lutador1 != ''):
                    ok = True
                else:
                    print("\nNome inválido\n")
                    lutador1 = input("Nome do lutador 1: ")
            ok = False

            lutador2 = input("Nome do lutador 2: ")     # Achou - Torneio; Achou1 - lutador1; Achou2 - lutador2
            while(ok == False):                         # pos0 - torneio; pos1 - lutador1; pos2 - lutador2
                if(lutador2 != ''):
                    ok = True
                else:
                    print("\nNome inválido\n")
                    lutador2 = input("Nome do lutador 2: ")
            ok = False

            achou1 = False
            achou2 = False

            for count2 in range(0, len(torneios[count].vitorias), 1):
                if(torneios[count].vitorias[count2][0].nome == lutador1):
                    achou1 = True
                    pos1 = count2
                if(torneios[count].vitorias[count2][0].nome == lutador2):
                    achou2 = True
                    pos2 = count2

    if(achou == False):
        print("\nTorneio não criado, por favor, o crie antes\n")
        menu_torneio(lutadores, torneios)
    if(achou1 == False or achou2 == False):
        print("\nLutador(es) não encontrado(s) neste torneio, por favor, inscreva-o(s) antes.\n")
        menu_torneio(lutadores, torneios)


    vencedor = random.choice([torneios[pos0].vitorias[pos1][0],torneios[pos0].vitorias[pos2][0]])
    if(vencedor == torneios[pos0].vitorias[pos1][0]):
        torneios[pos0].vitorias[pos1][1] += 1
        torneios[pos0].derrotas[pos2][1] += 1
    else:
        torneios[pos0].vitorias[pos2][1] += 1
        torneios[pos0].derrotas[pos1][1] += 1
    print(f"\nLuta entre {lutador1} e {lutador2}!!\n")
    print(f"Vencedor é: {vencedor.nome}\n")
    menu_torneio(lutadores, torneios)
            
# Funções do menu Lutador abaixo

def cadastrar_lutador(lutadores, torneios):
    ok = False
    
    nome = input("Nome do lutador: ")
    while(ok == False):
        if(nome != ''):
            ok = True
        else:
            print("\nNome inválido\n")
            nome = input("Nome do lutador: ")
    ok = False

    
    idade = input("Idade do lutador: ")
    while(ok == False):
        try:
            idade = int(idade)
            ok = True
        except:
            print("\nIdade inválida\n")
            idade = input("Idade do lutador: ")
    ok = False

  
    peso = input("Peso do lutador: ")
    while(ok == False):
        try:
            peso = float(peso)
            ok = True
        except:
            print("\nPeso inválido\n")
            peso = input("Peso do lutador: ")
    ok = False
    
    
    forca = input("Forca do lutador: ")
    while(ok == False):
        try:
            forca = float(forca)
            ok = True
        except:
            print("\nForca inválida\n")
            forca = input("Forca do lutador: ")
    ok = False

    
    faixa = input("Faixa do lutador: ")
    while(ok == False):
        if(faixa != ''):
            ok = True
        else:
            print("\nFaixa inválida\n")
            faixa = input("Faixa do lutador: ")
    ok = False

    
    estiloLuta = input("Arte marcial do lutador: ")
    while(ok == False):
        if(estiloLuta != ''):
            ok = True
        else:
            print("\nArte Marcial inválida\n")
            estiloLuta = input("Arte Marcial do lutador: ")
    ok = False

    lutadores.append(lutador(nome, idade, peso, forca, faixa, estiloLuta))
    print("\nJogador Cadastrado!\n")
    menu_lutador(lutadores, torneios)
    

def ver_lutadores_cadastrados(lutadores, torneios):
    for count in range(0,len(lutadores),1):
        print(f"Lutador {count+1}: nome: {lutadores[count].nome}\n")
    menu_lutador(lutadores, torneios)
    

def ver_detalhes(lutadores, torneios):
    sair = False
    achou = False
    while(sair != True):
        lutador = input("Qual lutador você gostaria de ver detalhes?\n")
        for count in range(0,len(lutadores),1):
            if(lutadores[count].nome == lutador):
                achou = True
                print(f"\nLutador: nome: {lutadores[count].nome}, idade: {lutadores[count].idade}, peso: {lutadores[count].peso}, forca: {lutadores[count].forca}, faixa: {lutadores[count].faixa}, Arte Marcial: {lutadores[count].estiloLuta}, Vitórias: {lutadores[count].vitorias}, Derrotas: {lutadores[count].derrotas}\n")
        if(achou != True):
            print("\nJogador não cadastrado.\n")
            sair = True
        else:
            print("Gostaria de ver mais jogadores?")
            escolha = input("(s/n): ")
            if(escolha == 'n'):
                sair = True
    
    menu_lutador(lutadores, torneios)

    
# Funções Torneio Random
def torneio_random():
    print("torneio_random()")

# Classes

class lutador:

    #Mínimos
    #nome
    #idade
    #peso
    #forca
    #faixa
    #estiloLuta

    def __init__(self, nome, idade, peso, forca, faixa, estiloLuta):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.forca = forca
        self.faixa = faixa
        self.estiloLuta = estiloLuta

    def __str__(self):
        return f'Lutador -> nome: {self.nome}, idade: {self.idade}, peso: {self.peso}, forca: {self.forca}, faixa: {self.faixa}, estiloLuta: {self.estiloLuta}'


class torneio:

    #Minimos
    #nome
    #pesos
    #faixas
    #estiloLuta
    nome = ''
    pesos = []
    faixas = []
    estiloLuta = '' # Cada torneio só vai permitir 1 estilo de luta
    lutadores_inscritos = []
    vitorias = [] # [[lutador1,5],[lutador2,10],...]
    derrotas = [] # [[lutador1,1],[lutador2,5],...]

  #  def __init__(self, nome, pesos, faixas, estiloLuta):
   #     self.nome = nome
    #    self.pesos = pesos
     #   self.faixas = faixas
      #  self.estiloLuta = estiloLuta

    def __str__(self):
        return f'Torneio -> nome: {self.nome},pesos: {self.pesos}, faixas: {self.faixas}, estiloLuta: {self.estiloLuta}, lutadores: {self.lutadores_inscritos}'

    def setNome(self, nome):
        self.nome = nome

    def setPesos(self, peso_inicial, peso_final):
        self.pesos.append([peso_inicial, peso_final])

    def setFaixas(self, faixa):
        self.faixas.append(faixa)

    def setEstilo(self, estiloLuta):
        self.estiloLuta = estiloLuta
        


def main():
    lutadores = []
    torneios = []
    start_menu(lutadores, torneios)
    
    
main()
