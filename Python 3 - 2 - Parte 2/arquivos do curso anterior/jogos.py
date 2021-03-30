import forca
import adivinhacao

print("*********************************")
print("**********Jogos Python***********")
print("*********************************")

jogo = 0

jogo = int(input("Escolha seu jodo desejado!\n"
       "1 - Forca\n"
       "2 - Adivinhação\n"
       "-> "))

if(jogo == 1):
    print ("\n\nJogo da forca escolhido:\n\n")
    forca.jogar()
elif(jogo ==2):
    print ("\n\nJogo da adivinhação escolhido:\n\n")
    adivinhacao.jogar()

