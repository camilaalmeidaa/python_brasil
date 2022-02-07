def tinta2():
    
    metros = float(input("*Exercicio17* Digite o tamanho da area a ser pintada em metros quadrados: "))
    
    litros_tinta = metros/6
    
    latas_tinta = litros_tinta/18
    galoes_tinta = litros_tinta/3.6
    valor_latas = latas_tinta*80
    valor_galoes = galoes_tinta*25
    
    print("a. A quatidade de latas de tinta necessarias é de",latas_tinta,"e o valor a ser pago é de R$",valor_latas,"\n")
    print("b. A quantidade de galoes de tinta necessarios é de",galoes_tinta,"e o valor a ser pago é de R$",valor_galoes,"\n")
    print("c. ------------------------------------------------------------------------------------------------------------\n")
    