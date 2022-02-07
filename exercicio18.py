def download():
    
    tam = float(input("*Exercicio18* Digite o tamanho do arquivo para download (em MB): "))
    vel = float(input("*Exercicio18* Digite a velocidade de um link de Internet (em Mbps): "))
    
    tempo_seg = tam/(vel/8) 
    tempo_min = tempo_seg/60
    
    print("O tempo aproximado de download do arquivo em minutos é de",tempo_min,"minutos\n")
    
    