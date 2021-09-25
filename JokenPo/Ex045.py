from random import randint
r=randint(1,3)
print("Jogo do JOKENPO")
print("------------------------")
print("[1]Pedra" )
print("[2]Papel")
print("[3]Tesoura")
print("------------------------")
esc=int(input("Faça sua escolha: "))
print("------------------------")

if r==1:
    print("Seu adversário escolheu PEDRA")
    if esc==1:
        print("Você escolheu PEDRA")
        print("EMPATE!")
    elif esc==2:
        print("Você escolheu PAPEL")
        print("VOCÊ GANHOU!")
    elif esc==3:
        print("Você escolheu TESOURA")
        print("VOCÊ PERDEU!")
    else:
        print("INVÁLIDO!")

elif r==2:
    print("Seu adversário escolheu PAPEL")
    if esc==1:
        print("Você escolheu PEDRA")
        print("VOCÊ PERDEU!")
    elif esc==2:
        print("Você escolheu PAPEL")
        print("EMPATE!")
    elif esc==3:
        print("Você escolheu TESOURA")
        print("VOCÊ GANHOU!")
    else:
        print("INVÁLIDO!")

elif r==3:
    print("Seu adversário escolheu TESOURA")
    if esc==1:
        print("Você escolheu PEDRA")
        print("VOCÊ PERDEU!")
    elif esc==2:
        print("Você escolheu PAPEL")
        print("VOCÊ GANHOU!")
    elif esc==3:
        print("Você escolheu TESOURA")
        print("EMPATE!")
    else:
        print("INVÁLIDO!")

print("------------------------")