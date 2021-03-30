import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")
    print("\n")

    # forma pela qual se insere um módulo (biblioteca) no python


    # numero_secreto = round(random.random()*100)
    # gerar um número aleatório entre 0 e 100 e arredondar
    # outra maneira seria (melhor)

    numero_secreto = random.randrange(1,101) # de 1 até 100
                                            # se quiser soemte os pares poderia ser
                                            # round.randrange(0,101,2) começa em 0 e vai até 100 de 2 em 2

    num_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    # print (numero_secreto)
    # para uso de testes

    nivel = int(input ("Escolha o nível de dificuldade do jogo:\n"
           "1 - Fácil\n"
           "2 - Médio\n"
           "3 - Difícil\n"
           "-> "))

    if(nivel == 1):
        num_tentativas = 20
        pontos = pontos - 200
    elif(nivel == 2):
        num_tentativas = 10
        pontos = pontos - 100
    else:
        num_tentativas = 5

    for rodada in range(1, num_tentativas + 1):
        # a sintaxe do for para ide de 2 em 2 ou mais é a seguinte:
        # for rodada in range(1, num_tentativas + 1, 2)
        print("Tentativa {} de {}".format(rodada, num_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
                # int() transforma a entrada input() em inteiro, porque o defaut é string

        if(chute<1 or chute>100):
            print("Você deve digitar um número maior que 1 e menor que 100!")
            continue

        if (numero_secreto == chute):
            print("Você acertou!"
                  "Você fez {} pontos".format(pontos))
            break
        else:
            if (chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (chute < numero_secreto):
                print("Você errou! O seu chute foi menor que o número secreto.")

                pontos_perdidos = abs(numero_secreto - chute)
                # usar a função abs() para colocar o numero absoluto evitar
                # que tenha numero negativo e o sistema de pontuação funcione

                pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"): # modo de operar o jogo separado
    jogar()