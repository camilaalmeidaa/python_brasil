def peso_ideal2():
    
    sexo = input("*Exercicio13* Digite M para mulher e H para homem: ")
    altura = float(input("*Exercicio13* Digite sua altura em metros: "))
    
    if(sexo == 'M' or sexo == 'm'):
        
        peso = (62.1 * altura) - 44.7
        print("O peso ideal para essa altura é de",peso,"kg\n")
        
    elif(sexo == 'H' or sexo == 'h'):
        
        peso2 = (72.7 * altura) - 58
        print("O peso ideal para essa altura é de",peso2,"kg\n")
    
    else:
        print("Informe o sexo corretamente. M para mulher ou H para homem")
        