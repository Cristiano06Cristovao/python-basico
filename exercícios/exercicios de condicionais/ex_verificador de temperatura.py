print("VERIFICADOR DE TEMPERATURA")

temperatura = float((input("Digite a temperatura:")))
if temperatura < 0:
    print("Está a congelar")
elif temperatura >= 0 and temperatura <= 14:
    print("Está Frio")
elif temperatura >= 15 and temperatura <= 24:
    print("Temperatura Agradavel")
elif temperatura >= 25 and temperatura <= 35:
    print("Está Calor")
else:
    print("Calor extremo. Hidrata-te")