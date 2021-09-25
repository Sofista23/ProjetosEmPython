while True:
    n1=float(input("Digitre o 1° número: "))
    n2=float(input("Digite o 2° número: "))
    r=str(input("Soma[so] / Subtração[su] / Multiplicação[m] / Divisão[d]: ")).upper().strip()
    
    if(r=="SO"):
        res=n1+n2
        print(f"A soma entre {n1} e {n2} é {res}.")

    elif(r=="SU"):
        if(n1>n2):
            res=n1-n2
            print(f"A subtração entre {n1} e {n2} é {res}.")
        else:
            res=n2-n1
            print(f"A soma entre {n2} e {n1} é {res}.")

    elif(r=="M"):
        res=n1*n2
        print(f"O produto entre {n1} e {n2} é {res}.")
    
    elif(r=="D"):
        if(n2==0):
            print("Impossível dividir algo por 0!")
        else:
            res=n1/n2
            print(f"A divisão entre {n1} e {n2} é {res}.")
    
    else:
        print("Valores Inválidos!")
    
    cont=str(input("Continuar[s/n]: ")).upper().strip()
    if(cont!="S" and cont!="N"):
        print("Valore Inválidos")
    elif(cont=="N"):
        break

print("Obrigado por usar a incrível calculadora 3000!")