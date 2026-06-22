lado1 = int(input("Digite um lado:"))
lado2 = int(input("Digite outro lado:"))
lado3 = int(input("Digite mais um lado:"))

if  lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os seus lados formam um triângulo")
    if lado1 == lado2 == lado3:
        print("Os seus lados formam um Equilátero")
    elif lado1 == lado2 != lado3:
        print("Os seus lados formam um Isósceles")
    else:
        print("Os seus lados formam um Escaleno")
else:
    print("Os seus lados não formam um triangulo")