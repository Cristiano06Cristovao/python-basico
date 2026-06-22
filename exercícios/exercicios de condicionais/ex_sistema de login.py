print("Login")
user =  "Cristiano"
senha = "Cristiano2006"
utilizador = input("Digite o seu utilizador:")
chave = input("Digite a sua senha:")
if utilizador.casefold() == user.casefold() and chave == senha:
    print("Acesso Permitido")
elif utilizador.casefold() == user.casefold() and chave != senha:
    print("Senha incorrecta")
else:
    print("Utilizador não Encontrado")