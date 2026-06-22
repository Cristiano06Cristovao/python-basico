num1 = float(input("Digite um número:"))
sinal = input ("Digite um sinal:(+, -, *, /, **, //, %, !=)")
num2 = float(input("Digite outro número:"))
resultado = num1, sinal, num2

if sinal == "+":
   resultado = num1 + num2
elif sinal == "-":
   resultado = num1 - num2
elif sinal == "*":
   resultado = num1 * num2
elif sinal == "/":
   if num2!= 0:
    resultado = num1 / num2
   else:
      print("Erro de divisão por zero!")
      resultado = None
elif sinal == "**":
   resultado = num1 ** num2
elif sinal == "//":
   resultado = num1 // num2
elif sinal == "%":
   resultado = num1 % num2
elif sinal != 0:
   resultado = num1 != num2
else:
   print("Operador Incorrecto!")

if resultado is not None:
   print(f"Resultado: {num1} {sinal} {num2} = {resultado}")  
