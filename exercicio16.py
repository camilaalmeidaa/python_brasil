def tinta():
    
    metros = float(input("*Exercicio16* Digite o tamanho da area a ser pintada em metros quadrados: "))
    
    litros_tinta = metros/3
    
    latas_tinta = litros_tinta/18
    valor = latas_tinta*80
    
    print("A quatidade de latas de tinta necessarias é de",latas_tinta,"e o valor a ser pago é de R$",valor,"\n")