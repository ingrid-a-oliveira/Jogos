#base jogo de adivinhação
from random import randint
numero_maquina = randint(1,100)
print("A máquina escolherá um valor de 1 a 100 e você deverá adivinhar esse número para vencê-la.")
quantidade_tentativas = int(input("Quantas jogadas você acha necessário para vencer a máquina? "))

while quantidade_tentativas > 0:
    print(f"Você tem {quantidade_tentativas} tentativas!")
    palpite = int(input("Qual o seu palpite? "))
    if palpite < numero_maquina:
        print("O valor é maior!")
        quantidade_tentativas -= 1
        
    elif palpite > numero_maquina:
        print("O valor é menor!")
        quantidade_tentativas -= 1
    
    elif palpite == numero_maquina:
        print("Parabéns! Você ganhou!!!")
        break
        
if quantidade_tentativas == 0:
    print(f"O número escolhido pela máquina era {numero_maquina}.\nVocê perdeu! Tente novamente!")