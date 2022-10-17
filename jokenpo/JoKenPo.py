import random
import time



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

def verificar(jogador,maquina,placar_jogador: int,placar_maquina: int):
    placar_jogador = placar_jogador
    placar_maquina = placar_maquina
    
    if jogador == 0 and maquina == 1 :
        print("Voce Perdeu !!!")
        return placar_maquina + 1
    
        
    elif jogador == 0 and maquina == 2 :
        print("Voce ganhou !!!")
        return placar_jogador + 1

    elif jogador == 0 and maquina == 0:
        print("Empate")

    if jogador == 1 and maquina == 2 :
        print("Voce Perdeu !!!")

        return placar_maquina + 1
      
    elif jogador == 1 and maquina == 0 :
        print("Voce ganhou !!!")

        return placar_jogador + 1
        
    elif jogador == 1 and maquina == 1:
        print("Empate")

    if jogador == 2 and maquina == 0 :
        print("Voce Perdeu !!!")

        return placar_maquina + 1
        
    elif jogador == 2 and maquina == 1 :
        print("Voce ganhou !!!")

        return placar_jogador + 1
        
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
    time.sleep(0.5)
    print("JO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PO")
    
jogador =  0

inicio = 1
print(layout)

placar_maquina = int(0)
placar_jogador = int(0)

while jogador != 9 :

    if inicio != 0:
                print(placar_jogador,placar_maquina)

    maquina = random.randint(0,2)
    jogador = int(input("Escolha:"))

    tempo()
    time.sleep(0.5)
    resultado_maquina(maquina)
    time.sleep(0.5)

    verificar(jogador,maquina,placar_jogador,placar_maquina)
    

    inicio += 1
    
