termo1 = 1
denominador = 3
termo2 = 1/denominador
n = 4 * (termo1-termo2)
while termo1 - termo2 > 0.00000005:
    termo1 = termo2
    denominador = (denominador*-1) + 2
    n += 4 *(termo1 - termo2)
print (n)
