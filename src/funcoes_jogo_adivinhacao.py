from random import randint
import os 

# atribuicao de variaveis
b = 9
c = 7
d = 5
e = 3

# funcao menu principal
def menu_principal():
    print(f"""
    ---------------------------------------------------
    -----------JOGO DE ADIVINHAÇÃO DE NÚMEROS----------
    ---------------------------------------------------""")    
    resposta_menu = input(("--Aperte 'J' para entrar no jogo ou 'X' para sair--\n")).upper()

    match resposta_menu:
        case 'J':
            os.system('cls')
            print(f"""
            Selecione o nível de dificuldade:
            1 -> MUITO FÁCIL (Número ilimitado de tentativas)
            2 -> FÁCIL ({b} tentativas)
            3 -> MÉDIA ({c} tentativas)
            4 -> DIFÍCIL ({d} tentativas)
            5 -> MUITO DIFÍCIL ({e} tentativas)""")
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
            os.system('cls')
            exit()      

# funcao chutes  
def chutes_mf():
    os.system('cls')
    print("Dificuldade MUITO FÁCIL")
    numero_sorteado = randint(0,100)
    contador = 1
    print(f"\nO computador sorteou um número.\nTente adivinhar qual número entre 0 a 100 o computador sorteou.\nTentativa {contador}:")
    chute = int(input())
    while chute != numero_sorteado:
        if chute > numero_sorteado:
            print("O número que o computador escolheu é MENOR.")
        else:
            print("O número que o computador escolheu é MAIOR.")
        contador += 1   
        print(f"\nTentativa {contador}: ")
        chute = int(input()) 
    print(f"\nVocê acertou!\nO número de tentativas foi {contador}\n")
    resposta_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
    match resposta_menu:
        case 'J':
            os.system('cls')  
            menu_principal()
        case 'X':
            os.system('cls')  
            exit()            

def chutes(x):
    os.system('cls')
    match x:
        case _ if x == b:
            print("Dificuldade FÁCIL")
        case _ if x == c:
            print("Dificuldade MÉDIA")
        case _ if x == d:
            print("Dificuldade DIFÍCIL")                
        case _ if x == e:
            print("Dificuldade MUITO DIFÍCIL")
        case _:
            print("Dificuldade inválida")
    numero_sorteado = randint(0,100)
    contador = 1
    print("\nO computador sorteou um número.\nTente adivinhar qual número entre 0 a 100 o computador sorteou.\n")
    print(f"Tentativa {contador}:")
    chute = int(input())
    while chute != numero_sorteado and contador < x:
        if chute > numero_sorteado:
            print("O número que o computador escolheu é MENOR.")
        else:
            print("O número que o computador escolheu é MAIOR.")
        contador += 1   
        print(f"\nVocê possui {x - contador} tentativa(s) restante(s).\nTentativa {contador}:")
        chute = int(input())
    if chute == numero_sorteado:
        print(f"\nVocê acertou!\nO número de tentativas foi {contador}\n")       
        resposta_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
        match resposta_menu:
            case 'J':
                os.system('cls')  
                menu_principal()
            case 'X':
                os.system('cls')  
                exit()
    print(f"\nVocê não conseguiu adivinhar. \nO número era {numero_sorteado}\n")
    resposta_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
    match resposta_menu:
        case 'J':
            os.system('cls')  
            menu_principal()
        case 'X':
            os.system('cls')  
            exit()               