diferença = 1
    pi = 0
    soma = 1
    negativo = 1
    
    while (diferença > (5*10**(-8))):
        ultimo_termo = pi
        pi = pi + 4/ (soma * negativo)
        soma += 2
        negativo *= -1
        
        diferença = (ultimo_termo - pi) * negativo
        
    print (pi)

