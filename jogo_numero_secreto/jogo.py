from random import *
print("Adivinhe um número entre 1 e 10")
numero = (randint(1,10))
acertou = False
while(not acertou):
    chute = input("chute ? : ")
    print(int(chute))    
    if(chute == str(numero)):
        acertou = True
        print("Acertou")
    else:
        print("Errou")