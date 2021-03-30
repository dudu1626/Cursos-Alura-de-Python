import random

def jogar():

    mensagem_inicial()

    palavra_secreta = carregar_palavra_secreta()

    letra_acerto = ["_" for letra in palavra_secreta]

    print(letra_acerto)
    print("")

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou): #enquanto nao enforcou ou não acertou

        chute = entrada_chute()

        if chute in palavra_secreta:
            teste_letras(palavra_secreta, chute, letra_acerto)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6 # se o numero de tentativas for igual a 6 enforcou = true

        acertou = "_" not in letra_acerto # quando todas as _ sumirem finaliza o jogo

        print("\n")
        print(letra_acerto)
        print("Você pode errar {} vezes".format(6-erros))



    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

######################
## Funções do Jogo: ##
######################

def mensagem_inicial():
    print("\n*********************************")
    print("***Bem-vindo ao jogo da Forca!***")
    print("*********************************")
    print("\nAdivinhe a palavra secreta!\nVocê só pode errar 6 vezes\n")

def carregar_palavra_secreta():
    palavras = []  # cria uma lista vazia para colocar as palavras
    with open("palavras.txt") as arquivo:  # abre o arquivo para a leitura
        for linha in arquivo:
            palavras.append(linha.strip())
            # adiciona as palavras na lista. usamos linha.strip
            # porque as linhas tem \n no final de cada palavra

    numero = random.randrange(0, len(palavras))  # para sortear a palavra
    palavra_secreta = palavras[numero].upper()  # forçar a palavra secreta ser maiúscula

    return palavra_secreta

def entrada_chute():
    chute = input("Digite uma letra -> ").strip().upper()
    # .lower() para deixar tudo em letra minúscula e funcionar, caso o usuário digite em
    # caixa alta e .strip() para tirar eventuais espaços em branco antes e depois da letra
    return chute

def teste_letras(palavra_secreta, chute, letra_acerto):
    index = 0
    for letra in palavra_secreta:

        if (chute == letra):
            letra_acerto[index] = letra

        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |       _    ")
        print(" |    \ (_)   ")
        print(" |     \      ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |       _    ")
        print(" |    \ (_)   ")
        print(" |     \ |    ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |       _     ")
        print(" |    \ (_) /  ")
        print(" |     \ | /   ")
        print(" |       |     ")
        print(" |             ")
        print(" |             ")

    if(erros == 5):
        print(" |       _     ")
        print(" |    \ (_) /  ")
        print(" |     \ | /   ")
        print(" |       |     ")
        print(" |      /      ")
        print(" |     /       ")

    if (erros == 6):
        print(" |       _     ")
        print(" |    \ (_) /  ")
        print(" |     \ | /   ")
        print(" |       |     ")
        print(" |      / \    ")
        print(" |     /   \   ")

    print(" |            ")
    print("_|____         ")
    print()

def imprime_mensagem_perdedor(palavra_secreta):
    print("\nQue pena, você foi enforcado!")
    print("A palavra era {}\n".format(palavra_secreta))
    print("     _______________        ")
    print("    /               \       ")
    print("   /                 \      ")
    print("  /                   \     ")
    print("  |   XXXX     XXXX   |     ")
    print("  |   XXXX     XXXX   |     ")
    print("  |   XXX       XXX   |     ")
    print("  |                   |     ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |       ")
    print("    | I I I I I I I |       ")
    print("    |  I I I I I I  |       ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \___I____/          ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if(__name__ == "__main__"): # modo de operar o jogo separado
    jogar()