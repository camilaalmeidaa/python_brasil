def calcula_salario():
    
    valor_hora = float(input("*Exercicio15* Digite o valor que voce ganha por hora: "))
    horas = float(input("*Exercicio15* Digite a quantidade de horas trabalhadas: "))
    
    sal_bruto = valor_hora * horas
    
    ir = 0.11 * sal_bruto
    sal = sal_bruto - ir
    
    inss = 0.08 * sal
    sal2 = sal - inss
    
    sind = 0.05 * sal2
    sal_liq = sal2 - sind
    
    print("a. O salario bruto é de R$",sal_bruto,"\n")
    print("b. A quantia paga ao INSS é de R$",inss,"\n")
    print("c. A quantia paga ao sindicato é de R$",sind,"\n")
    print("d. O salario liquido é de R$",sal_liq,"\n")
    