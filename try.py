print('Bem Vindo a Calculadora Luquinhas')

escolha = input("Escolha (soma/soma3/menos/menos3/mult/mult3/div):")


if escolha == "soma":
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))
    soma = n1 + n2
    print("O Resultado da soma com dois valores é:", soma)

if escolha == "soma3":
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))
    n3 = float(input("Valor 3:"))
    soma3 = n1 + n2 + n3
    print("O Resultado da soma com três valores é:", soma3)

if escolha == "menos":
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))
    menos = n1 - n2
    print("O Resultado da subtração com dois valores é:", menos)

if escolha == "menos3":
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))
    n3 = float(input("Valor 3:"))
    menos3 = n1 - n2 - n3
    print("O Resultado da subtração com três valores é:", menos3)

if escolha == "mult":
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))
    mult = n1 * n2
    print("O Resultado da multiplicação com dois valores é:", mult)

if escolha == "mult3":
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))
    n3 = float(input("Valor 3:"))
    mult3 = n1 * n2 * n3
    print("O Resultado da multiplicação com três valores é:", mult3)

if escolha == "d":
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))
    d = n1 / n2
    print("O Resultado da divisão é:", d)
