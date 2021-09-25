import os
import random



jogadas=0
quemJoga=2 #1=CPU 2=Jogador
maxJogadas=9
jogarNovamente="S"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]



def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print(f"0:  {velha[0][0]} | {velha[0][1]} | {velha[0][2]}")
    print("   -----------")
    print(f"1:  {velha[1][0]} | {velha[1][1]} | {velha[1][2]}")
    print("   -----------")
    print(f"2:  {velha[2][0]} | {velha[2][1]} | {velha[2][2]}")
    print(f"Jogadas: {jogadas}")



def jogador():
    global jogadas  
    global quemJoga
    global vit
    global maxJogadas

    if(quemJoga==2 and jogadas<maxJogadas):
        linha=int(input("Linha para jogar: "))
        coluna=int(input("Coluna para jogar: "))

        while(velha[linha][coluna]!=" "):
            linha=int(input("Linha para jogar: "))
            coluna=int(input("Coluna para jogar: "))

        try:
            velha[linha][coluna]="X"
            quemJoga=1
            jogadas=1
        except:
            print("Linha ou Coluna INVÁLIDA!")


    
def CPU():
    global jogadas  
    global quemJoga
    global vit
    global maxJogadas

    if(quemJoga==1 and jogadas<maxJogadas):
        linha=random.randrange(0,3)
        coluna=random.randrange(0,3)

        while(velha[linha][coluna]!=" "):
            linha=random.randrange(0,3)
            coluna=random.randrange(0,3)

        velha[linha][coluna]="O"
        quemJoga=2
        jogadas+=1



def verificarVitoria():
    global velha
    vitoria="N"
    simbolos=["X","O"]

    for s in simbolos:
        vitoria="N"


        #Verificar Vitória em LINHAS
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il+=1
        if(vitoria!="N"):
            break


        #Verificar Vitória em COLUNAS
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="N"):
            break


        #Verifica Vitória em DIAGNAL 1
        soma=0
        iDiag=0
        while iDiag<3:
            if(velha[iDiag][iDiag]==s):
                soma+=1
            iDiag+=1
        if(soma==3):
            vitoria=s
            break


        #Verifica Vitória em DIAGNAL 2
        soma=0
        iDiagL=0
        iDiagC=2
        while iDiagC:
            if(velha[iDiagL][iDiagC]==s):
                soma+=1
            iDiagL+=1
            iDiagC-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria



def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    jogadas=0
    quemJoga=2 #1=CPU 2=Jogador
    maxJogadas=9
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]



while True:
    tela()
    jogador()
    CPU()
    tela()
    vit=verificarVitoria()

    if(vit!="N")or(jogadas>=maxJogadas):
        break



print("FIM DE JOGO")

if(vit=="X" or vit=="O"):
    if(vit=="X"):
        print("Você GANHOU!")

    else:
        print("CPU GANHOU!")
        
else:
    print("EMPATE!")