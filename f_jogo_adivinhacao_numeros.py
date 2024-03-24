from random import randint
import os 

b = 10
c = 8
d = 5
e = 3

def menu_num():
    print("---------------------------------------------------")    
    print("-----------JOGO DE ADIVINHAÇÃO DE NÚMEROS----------") 
    print("---------------------------------------------------") 
    resp_menu = input(("--Aperte 'J' para entrar no jogo ou 'X' para sair--\n")).upper()
    return(resp_menu)  

def chutes_mf():
    numero = randint(0,100)
    cont = 1
    print("Tentativa número",cont,": ")
    chute = int(input(""))
    while chute != numero:
        if chute > numero:
            print("O número que o computador escolheu é MENOR.")
        else:
            print("O número que o computador escolheu é MAIOR.")
        cont += 1   
        print("Tentativa número",cont,": ")
        chute = int(input("")) 
    print("Você acertou!")
    print("O número de tentativas foi",cont)
    print() 
    resp_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
    if resp_menu == "J":
        os.system('cls')  or None
        print("Selecione o nível de dificuldade:")
        print("'1' -> MUITO FÁCIL (Número ilimitado de tentativas) \n"
              "'2' -> FÁCIL (",b,"tentativas) \n"
              "'3' -> MÉDIO (",c,"tentativas) \n" 
              "'4' -> DIFÍCIL (",d,"tentativas) \n"
              "'5' -> MUITO DIFÍCIL (",e,"tentativas) \n"
            )
        resp_num = int(input(""))
        return(resp_num)
    elif resp_menu == "X":
        exit()        

def sorteio():
    print("O computador sorteou um número.")
    print("Tente adivinhar qual número entre 0 a 100 o computador sorteou: ")    

def chutes(x):
    numero = randint(0,100)
    cont = 1
    print("Tentativa número",cont,": ")
    chute = int(input(""))
    while chute != numero and cont < x:
        if chute > numero:
            print("O número que o computador escolheu é MENOR.")
        else:
            print("O número que o computador escolheu é MAIOR.")
        cont += 1   
        print("Tentativa número",cont,": ")
        chute = int(input(""))
    if chute == numero:
        print("Você acertou!")
        print("O número de tentativas foi",cont)
        print()
        resp_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
        if resp_menu == "J":
            os.system('cls')  or None
            print("Selecione o nível de dificuldade:")
            print("'1' -> MUITO FÁCIL (Número ilimitado de tentativas) \n"
                  "'2' -> FÁCIL (",b,"tentativas) \n"
                  "'3' -> MÉDIO (",c,"tentativas) \n" 
                  "'4' -> DIFÍCIL (",d,"tentativas) \n"
                  "'5' -> MUITO DIFÍCIL (",e,"tentativas) \n"
                )
            resp_num = int(input(""))
            return(resp_num)
        elif resp_menu == "X":
            exit()
    else:
        print("Você não conseguiu adivinhar")
        print("O número era",numero)  
        print()         
        resp_menu = input(("---Aperte 'J' para jogar novamente ou 'X' para sair---\n")).upper()
        if resp_menu == "J":
            os.system('cls')  or None
            print("Selecione o nível de dificuldade:")
            print("'1' -> MUITO FÁCIL (Número ilimitado de tentativas) \n"
                  "'2' -> FÁCIL (",b,"tentativas) \n"
                  "'3' -> MÉDIO (",c,"tentativas) \n" 
                  "'4' -> DIFÍCIL (",d,"tentativas) \n"
                  "'5' -> MUITO DIFÍCIL (",e,"tentativas) \n"
                )
            resp_num = int(input(""))
            return(resp_num)
        elif resp_menu == "X":
            exit()
    
  
   
                   