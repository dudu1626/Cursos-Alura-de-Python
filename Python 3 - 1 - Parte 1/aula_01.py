print("***********************************")
print(" Bem-vindo ao jogo de adivinhação!")
print("***********************************")

numero_secreto = 42
num_tentativas = 1
num_max_tentativas = 3


while(num_tentativas <= num_max_tentativas):

    print("Tentativa {} de {}.".format(num_tentativas, num_max_tentativas)) #string interpolation
                                # maneira de inserir as variáveis no print.
                                # outramaneira seria:  print("Tentativa", variavel, "de", variavel)
    chute = int(input("Digite seu número: "))  # transforma o input em int
                                               # qq coisa digitada no input é string

    if(numero_secreto == chute):
        print("Você acertou!")
        break
    else:
        if(numero_secreto < chute):
            print("Você errou! O número secreto é menor que o seu chute")
            num_tentativas = num_tentativas + 1

        elif(numero_secreto > chute): # "elif" é usado para fazer encadeamento de "if"
            print("Você errou! O número secreto é maior que o seu chute")
            num_tentativas = num_tentativas + 1


print("Fim de Jogo!")