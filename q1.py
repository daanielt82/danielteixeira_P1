def raizes():
    a = int(input("Digite o 'a': "))
    b = int(input("Digite o 'b': "))
    c = int(input("Digite o 'c': "))
    delta = (b*b) - (4*a*c)
    raiz1 = (b*-1 + delta) / 2*a
    raiz2 = (b*-1 - delta) / 2*a
    complexa = 0
    if delta < 0:
        complexa = 1
        real = (b*-1)/2*a
        imag = (delta*-1)/2*a
        print(real)
        print(imag)
        return complexa
    else:
        complexa = 0
        print(raiz1)
        print(raiz2)
        return complexa
