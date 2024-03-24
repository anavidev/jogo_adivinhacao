from f_jogo_adivinhacao_numeros import *

resp_menu = menu_num()

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
    while resp_num in range(1,6):
        if resp_num == 1:
            sorteio()
            resp_num = chutes_mf() 
        elif resp_num == 2:
            sorteio() 
            resp_num = chutes(b)
        elif resp_num == 3:
            sorteio()
            resp_num = chutes(c)
        elif resp_num == 4:
            sorteio()
            resp_num = chutes(d)
        elif resp_num == 5:
            sorteio()
            resp_num = chutes(e)                                             
elif resp_menu == "X":
    exit()       
       
        
    

    
    