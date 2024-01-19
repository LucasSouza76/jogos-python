import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhacao")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute_string = input("Digite um numero entre 1 e 100: ")
        chute = int(chute_string)
        print("Voce digitou ", chute)
        
        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou o numero secreto e fez {}".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou ! O seu chute foi maior que o número secreto")
            elif(menor):
                print("Voce errou! O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos       
            
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()