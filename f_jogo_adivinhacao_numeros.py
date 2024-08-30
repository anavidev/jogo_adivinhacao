from random import randint
import os 

# atribuicao de variaveis

b = 9
c = 7
d = 5
e = 3

# funcao menu principal

def menu_principal():
    print("---------------------------------------------------")    
    print("-----------JOGO DE ADIVINHAÇÃO DE NÚMEROS----------") 
    print("---------------------------------------------------") 
    resposta_menu = input(("--Aperte 'J' para entrar no jogo ou 'X' para sair--\n")).upper()

    match resposta_menu:
        case 'J':
            os.system('cls')  or None
            print("Selecione o nível de dificuldade:")
            print("'1' -> MUITO FÁCIL (Número ilimitado de tentativas) \n"
                "'2' -> FÁCIL (",b,"tentativas) \n"
                "'3' -> MÉDIO (",c,"tentativas) \n" 
                "'4' -> DIFÍCIL (",d,"tentativas) \n"
                "'5' -> MUITO DIFÍCIL (",e,"tentativas)"
                )
        
            resposta_dificuldade = int(input())
            match resposta_dificuldade:
                case 1:
                    chutes_mf()
                case 2:           
                    chutes(b)
                case 3:
                    chutes(c)
                case 4:       
                    chutes(d)
                case 5:
                    chutes(e)
                case _:
                    exit()
        case 'X':
            os.system('cls')  or None
            exit()      

# funcao chutes  

def chutes_mf():
    numero_sorteado = randint(0,100)
    contador = 1
    print("\nO computador sorteou um número.\nTente adivinhar qual número entre 0 a 100 o computador sorteou.\n")
    print("Tentativa",contador,":")
    chute = int(input())
    while chute != numero_sorteado:
        if chute > numero_sorteado:
            print("O número que o computador escolheu é MENOR.")
        else:
            print("O número que o computador escolheu é MAIOR.")
        contador += 1   
        print("\nTentativa",contador,": ")
        chute = int(input()) 
    print("\nVocê acertou!\nO número de tentativas foi",contador)
    print()
    resposta_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
    match resposta_menu:
        case 'J':
            os.system('cls')  or None
            menu_principal()
        case 'X':
            os.system('cls')  or None
            exit()            

def chutes(x):
    numero_sorteado = randint(0,100)
    contador = 1
    print("\nO computador sorteou um número.\nTente adivinhar qual número entre 0 a 100 o computador sorteou.\n")
    print("Tentativa",contador,": \nVocê possui",x - contador,"tentativa(s) restantes.")
    chute = int(input())
    while chute != numero_sorteado and contador < x:
        if chute > numero_sorteado:
            print("O número que o computador escolheu é MENOR.")
        else:
            print("O número que o computador escolheu é MAIOR.")
        contador += 1   
        print("\nTentativa",contador,": \nVocê possui",x - contador,"tentativa(s) restantes.")
        chute = int(input())
    if chute == numero_sorteado:
        print("\nVocê acertou! \nO número de tentativas foi",contador)
        print()         
        resposta_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
        match resposta_menu:
            case 'J':
                os.system('cls')  or None
                menu_principal()
            case 'X':
                os.system('cls')  or None
                exit()
    else:
        print("\nVocê não conseguiu adivinhar. \nO número era",numero_sorteado)
        print()
        resposta_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
        match resposta_menu:
            case 'J':
                os.system('cls')  or None
                menu_principal()
            case 'X':
                os.system('cls')  or None
                exit()               