print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


from random import randint

numero_secreto = randint(0, 9)
total_tentativas = 0
pontos = 1000

print("Qual nivel de dificuldade?")
print("(1) facil (2) médio (3) difícil ")

nivel = int(input("defina o nível:"))

if nivel==1:
    total_tentativas = 10
elif nivel==2:
    total_tentativas = 5
else:
    total_tentativas = 3


for rodada in range(1, total_tentativas +1):

    print("Tentativa", rodada, "de", total_tentativas)
    chute_str = input("digite um número entre 0 e 9: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)
    if(chute < 0 or chute > 9):
        print("você deve digitar um número entre 0 e 9:")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou e fez {} pontos".format(pontos))
        #Serve para fazer com que a rodada seja maior que total_tentatvas e o jogo acabar após o acerto.
        rodada += 3
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if(maior):
          print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
          print("Você errou! O seu chute foi menor que o número secreto.")




print("Fim de jogo")
print("O número secreto era: ", numero_secreto)