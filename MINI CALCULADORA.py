print('Bem Vindo a Calculadora, para usar:')
texto = input("digite sua conta aqui:")
try:
    resultado = eval(texto)
    print("O resultado é:", resultado)
except Exception as e:
    print("Poderia verificar os operadores por favor?")
while True:
    texto2 = input("deseja continuar?(sim ou nao)")
    if texto2 == "nao":
        print("volte sempre :)")
        break
    else:
        texto2 == "sim"
        texto = input("digite sua conta aqui:")
        try:
            resultado = eval(texto)
            print("O resultado é:", resultado)
        except Exception as e:
            print("Poderia tentar novamente escrevendo a conta toda por favor?")
