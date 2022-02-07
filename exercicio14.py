def multa():
    
    peso = float(input("*Exercicio14* Digite o peso dos peixes em kg: "))
    
    excesso = peso - 50
    multa = excesso * 4
    
    print("A pescaria excedeu em",excesso,"kg e a multa que deverá ser paga é de R$",multa,"\n")