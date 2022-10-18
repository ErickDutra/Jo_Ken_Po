from random import randint
from time import sleep



layout="""
=============================
           Escolha:
=============================
[0] pedra
[1] papel
[2] tesoura 

=============================
        [9] Sair
=============================
"""

def layout_placar(placar_jogador,placar_maquina):
    print(f""""
=============================
        PLACAR:
=============================

JOGADOR:{placar_jogador}

MAQUINA:{placar_maquina}

=============================
""")


def verificar(jogador,maquina):
    global placar_jogador
    global placar_maquina

    if jogador == 0 and maquina == 1 :
        print("Voce Perdeu !!!")
        placar_maquina += 1
    
        
    elif jogador == 0 and maquina == 2 :
        print("Voce ganhou !!!")
        placar_jogador += 1

    elif jogador == 0 and maquina == 0:
        print("Empate")

    if jogador == 1 and maquina == 2 :
        print("Voce Perdeu !!!")
        placar_maquina += 1 
      
    elif jogador == 1 and maquina == 0 :
        print("Voce ganhou !!!")
        placar_jogador += 1
        
    elif jogador == 1 and maquina == 1:
        print("Empate")

    if jogador == 2 and maquina == 0 :
        print("Voce Perdeu !!!")
        placar_maquina += 1 
        
    elif jogador == 2 and maquina == 1 :
        print("Voce ganhou !!!")
        placar_jogador += 1
        
    elif jogador == 2 and maquina == 2:
        print("Empate")


def resultado_maquina(maquina):
    if maquina == 0:
        print("Pedra !!!")
    elif maquina == 1:
        print("Papel")
    elif maquina == 2:
        print("Tesoura")


def tempo():
    sleep(0.5)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PO")
    

jogador =  0
print(layout)
placar_maquina = int(0)
placar_jogador = int(0)

while True :
    maquina = randint(0,2)
    jogador = int(input("Escolha:"))

    if jogador == 0 or jogador == 1 or jogador == 2 :
        tempo()
        sleep(0.5)
        resultado_maquina(maquina)
        sleep(0.5)
        verificar(jogador,maquina)
        sleep(0.5)
        layout_placar(placar_jogador,placar_maquina)
        
    elif jogador == 9:
            break 

    elif jogador != 0 or jogador != 1 or jogador != 2 or jogador != 9 :
        print("jogada invalida")
        jogador = int(input("Escolha:"))

    

    

    