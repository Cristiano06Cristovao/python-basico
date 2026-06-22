print(" CALCULADORA DE NOTAS CRISTIANO 1.0")
nota = int(input("Digite a sua nota:"))

if nota <= 49:
    print("Reprovado")
elif nota >= 50 and nota <= 64:
    print("Suficiente")
elif nota >= 65 and nota <= 79:
    print("Bom")
elif nota >= 80 and nota <= 89:
    print("Muito Bom")
elif nota >= 90 and nota <= 100:
    print("Excelente")
else:
    print("ERRO: Digite uma nota valida.")