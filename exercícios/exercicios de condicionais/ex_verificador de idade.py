idade = int(input("Digite a sua idade:"))

if idade < 0 :
    print("ERROR: A idade não pode ser negativa. Tente novamente...")
elif idade < 12 :
    print("Criança")
elif idade <= 17:
    print("Adolescente")
else:
    print("Adulto")
