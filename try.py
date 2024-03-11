import math
print('Bem Vindo a Calculadora')
escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
if escolha == "soma":
    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
if escolha == "sub":
    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
if escolha == "mult":
    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")

if escolha == "soma":
    if Quantidade_de_Números == "2":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        soma2 = n1 + n2
        print("O Resultado da soma com dois valores é:", soma2)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                texto2 == "sim"
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                soma2 = n1 + n2
                print("O Resultado da soma com dois valores é:", soma2)
    if Quantidade_de_Números == "3":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        soma3 = n1 + n2 + n3
        print("O Resultado da soma com dois valores é:", soma3)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                texto2 == "sim"
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                soma3 = n1 + n2 + n3
                print("O Resultado da soma com dois valores é:", soma3)
    if Quantidade_de_Números == "4":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        soma4 = n1 + n2 + n3 + n4
        print("O Resultado da soma com dois valores é:", soma4)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                texto2 == "sim"
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                n4 = float(input("Valor 4:"))
                soma4 = n1 + n2 + n3 + n4
                print("O Resultado da soma com dois valores é:", soma4)
    if Quantidade_de_Números == "5":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        soma5 = n1 + n2 + n3 + n4 + n5
        print("O Resultado da soma com dois valores é:", soma5)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                texto2 == "sim"
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                n4 = float(input("Valor 4:"))
                n5 = float(input("Valor 5:"))
                soma5 = n1 + n2 + n3 + n4 + n5
                print("O Resultado da soma com dois valores é:", soma5)
    if Quantidade_de_Números == "6":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        soma6 = n1 + n2 + n3 + n4 + n5 + n6
        print("O Resultado da soma com dois valores é:", soma6)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                texto2 == "sim"
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                n4 = float(input("Valor 4:"))
                n5 = float(input("Valor 5:"))
                n6 = float(input("Valor 6:"))
                soma6 = n1 + n2 + n3 + n4 + n5 + n6
                print("O Resultado da soma com dois valores é:", soma6)
    if Quantidade_de_Números == "7":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
        print("O Resultado da soma com dois valores é:", soma7)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                texto2 == "sim"
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                n4 = float(input("Valor 4:"))
                n5 = float(input("Valor 5:"))
                n6 = float(input("Valor 6:"))
                n7 = float(input("Valor 7:"))
                soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                print("O Resultado da soma com dois valores é:", soma7)
    if Quantidade_de_Números == "8":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
        print("O Resultado da soma com dois valores é:", soma8)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                n4 = float(input("Valor 4:"))
                n5 = float(input("Valor 5:"))
                n6 = float(input("Valor 6:"))
                n7 = float(input("Valor 7:"))
                n8 = float(input("Valor 8:"))
                soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                print("O Resultado da soma com dois valores é:", soma8)
    if Quantidade_de_Números == "9":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        n9 = float(input("Valor 9:"))
        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
        print("o resultado da soma com nove numeros é:", soma9)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                n4 = float(input("Valor 4:"))
                n5 = float(input("Valor 5:"))
                n6 = float(input("Valor 6:"))
                n7 = float(input("Valor 7:"))
                n8 = float(input("Valor 8:"))
                n9 = float(input("Valor 9:"))
                soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                print("o resultado da soma com nove numeros é:")
    if Quantidade_de_Números == "10":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        n9 = float(input("Valor 9:"))
        n10 = float(input("Valor 10:"))
        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
        print("O Resultado da soma com dois valores é:", soma10)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else:
                n1 = float(input("Valor 1:"))
                n2 = float(input("Valor 2:"))
                n3 = float(input("Valor 3:"))
                n4 = float(input("Valor 4:"))
                n5 = float(input("Valor 5:"))
                n6 = float(input("Valor 6:"))
                n7 = float(input("Valor 7:"))
                n8 = float(input("Valor 8:"))
                n9 = float(input("Valor 9:"))
                n10 = float(input("Valor 10:"))
                soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                print("O Resultado da soma com dois valores é:", soma10)
if escolha == "sub":
    if Quantidade_de_Números == "2":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        menos2 = n1 - n2
        print("O Resultado da subtração com dois valores é:", menos2)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else: texto2 == "sim"

                 n1 = float(input("Valor 1:"))
            n2 = float(input("Valor 2:"))
            menos2 = n1 - n2
            print("O Resultado da subtração com dois valores é:", menos2)
    if Quantidade_de_Números == "3":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        menos3 = n1 - n2 - n3
        print("O Resultado da subtração com três valores é:", menos3)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else: texto2 == "sim"
            n1 = float(input("Valor 1:"))
            n2 = float(input("Valor 2:"))
            n3 = float(input("Valor 3:"))
            menos3 = n1 - n2 - n3
            print("O Resultado da subtração com três valores é:", menos3)
    if Quantidade_de_Números == "4":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        menos4 = n1 - n2 - n3 - n4
        print("O Resultado da soma com dois valores é:", menos4)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else: texto2 == "sim"
            n1 = float(input("Valor 1:"))
            n2 = float(input("Valor 2:"))
            n3 = float(input("Valor 3:"))
            n4 = float(input("Valor 4:"))
            menos4 = n1 - n2 - n3 - n4
            print("O Resultado da soma com dois valores é:", menos4)
    if Quantidade_de_Números == "5":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        menos5 = n1 - n2 - n3 - n4 - n5
        print("O Resultado da soma com dois valores é:", menos5)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else: texto2 == "sim"
            n1 = float(input("Valor 1:"))
            n2 = float(input("Valor 2:"))
            n3 = float(input("Valor 3:"))
            n4 = float(input("Valor 4:"))
            n5 = float(input("Valor 5:"))
            menos5 = n1 - n2 - n3 - n4 - n5
            print("O Resultado da soma com dois valores é:", menos5)
    if Quantidade_de_Números == "6":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        menos6 = n1 - n2 - n3 - n4 - n5 - n6
        print("O Resultado da soma com dois valores é:", menos6)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else: texto2 == "sim"
            n1 = float(input("Valor 1:"))
            n2 = float(input("Valor 2:"))
            n3 = float(input("Valor 3:"))
            n4 = float(input("Valor 4:"))
            n5 = float(input("Valor 5:"))
            n6 = float(input("Valor 6:"))
            menos6 = n1 - n2 - n3 - n4 - n5 - n6
            print("O Resultado da soma com dois valores é:", menos6)
    if Quantidade_de_Números == "7":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
        print("O Resultado da soma com dois valores é:", menos7)
        while True:
            texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
            if texto2 == "nao":
                print("voltando ao menu")
                escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
                if escolha == "soma":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "sub":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "mult":
                    Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
                if escolha == "soma":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        soma2 = n1 + n2
                        print("O Resultado da soma com dois valores é:", soma2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        soma3 = n1 + n2 + n3
                        print("O Resultado da soma com dois valores é:", soma3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        soma4 = n1 + n2 + n3 + n4
                        print("O Resultado da soma com dois valores é:", soma4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        soma5 = n1 + n2 + n3 + n4 + n5
                        print("O Resultado da soma com dois valores é:", soma5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        soma6 = n1 + n2 + n3 + n4 + n5 + n6
                        print("O Resultado da soma com dois valores é:", soma6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                        print("O Resultado da soma com dois valores é:", soma7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                        print("O Resultado da soma com dois valores é:", soma8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                        print("O Resultado da soma com dois valores é:", soma10)
                if escolha == "sub":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        menos2 = n1 - n2
                        print("O Resultado da subtração com dois valores é:", menos2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        menos3 = n1 - n2 - n3
                        print("O Resultado da subtração com três valores é:", menos3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        menos4 = n1 - n2 - n3 - n4
                        print("O Resultado da soma com dois valores é:", menos4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        menos5 = n1 - n2 - n3 - n4 - n5
                        print("O Resultado da soma com dois valores é:", menos5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        menos6 = n1 - n2 - n3 - n4 - n5 - n6
                        print("O Resultado da soma com dois valores é:", menos6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                        print("O Resultado da soma com dois valores é:", menos7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                        print("O Resultado da soma com dois valores é:", menos8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                        print("O Resultado da soma com dois valores é:", menos9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                        print("O Resultado da soma com dois valores é:", menos10)
                if escolha == "mult":
                    if Quantidade_de_Números == "2":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        mult2 = n1 * n2
                        print("O Resultado da multiplicação com dois valores é:", mult2)
                    if Quantidade_de_Números == "3":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        mult3 = n1 * n2 * n3
                        print("O Resultado da multiplicação com dois valores é:", mult3)
                    if Quantidade_de_Números == "4":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        mult4 = n1 * n2 * n3 * n4
                        print("O Resultado da multiplicação com dois valores é:", mult4)
                    if Quantidade_de_Números == "5":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        mult5 = n1 * n2 * n3 * n4 * n5
                        print("O Resultado da multiplicação com dois valores é:", mult5)
                    if Quantidade_de_Números == "6":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        mult6 = n1 * n2 * n3 * n4 * n5 * n6
                        print("O Resultado da multiplicação com dois valores é:", mult6)
                    if Quantidade_de_Números == "7":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                        print("O Resultado da multiplicação com dois valores é:", mult7)
                    if Quantidade_de_Números == "8":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                        print("O Resultado da multiplicação com dois valores é:", mult8)
                    if Quantidade_de_Números == "9":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                        print("O Resultado da multiplicação com dois valores é:", mult9)
                    if Quantidade_de_Números == "10":
                        n1 = float(input("Valor 1:"))
                        n2 = float(input("Valor 2:"))
                        n3 = float(input("Valor 3:"))
                        n4 = float(input("Valor 4:"))
                        n5 = float(input("Valor 5:"))
                        n6 = float(input("Valor 6:"))
                        n7 = float(input("Valor 7:"))
                        n8 = float(input("Valor 8:"))
                        n9 = float(input("Valor 9:"))
                        n10 = float(input("Valor 10:"))
                        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                        print("O Resultado da multiplicação com dois valores é:", mult10)
                if escolha == "pot":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("elevado a:"))
                    pot2 = n1 ** n2
                    print("o resultado da pontencialização é:", pot2)
                if escolha == "d":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("divido por:"))
                    d = n1 / n2
                    print("O Resultado da divisão é:", d)
                if escolha == "raiz":
                    escolha = input("quadrada/cubica")
                    if escolha == "quadrada":
                        n1 = float(input("Valor 1:"))
                        raiz = math.sqrt(n1)
                        print("A raiz quadrada de", n1, "é:", raiz)
                    if escolha == "cubica":
                        n1 = float(input("Valor 1:"))
                        raiz = n1 ** (1 / 3)
                        print("A raiz cúbica de", n1, "é:", raiz)
            else: texto2=="sim"
            n1 = float(input("Valor 1:"))
            n2 = float(input("Valor 2:"))
            n3 = float(input("Valor 3:"))
            n4 = float(input("Valor 4:"))
            n5 = float(input("Valor 5:"))
            n6 = float(input("Valor 6:"))
            n7 = float(input("Valor 7:"))
            menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
            print("O Resultado da soma com dois valores é:", menos7)
    if Quantidade_de_Números == "8":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
        print("O Resultado da soma com dois valores é:", menos8)
    if Quantidade_de_Números == "9":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        n9 = float(input("Valor 9:"))
        menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
        print("O Resultado da soma com dois valores é:", menos9)
    if Quantidade_de_Números == "10":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        n9 = float(input("Valor 9:"))
        n10 = float(input("Valor 10:"))
        menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
        print("O Resultado da soma com dois valores é:", menos10)
if escolha == "mult":
    if Quantidade_de_Números == "2":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        mult2 = n1 * n2
        print("O Resultado da multiplicação com dois valores é:", mult2)
    if Quantidade_de_Números == "3":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        mult3 = n1 * n2 * n3
        print("O Resultado da multiplicação com dois valores é:", mult3)
    if Quantidade_de_Números == "4":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        mult4 = n1 * n2 * n3 * n4
        print("O Resultado da multiplicação com dois valores é:", mult4)
    if Quantidade_de_Números == "5":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        mult5 = n1 * n2 * n3 * n4 * n5
        print("O Resultado da multiplicação com dois valores é:", mult5)
    if Quantidade_de_Números == "6":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        mult6 = n1 * n2 * n3 * n4 * n5 * n6
        print("O Resultado da multiplicação com dois valores é:", mult6)
    if Quantidade_de_Números == "7":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
        print("O Resultado da multiplicação com dois valores é:", mult7)
    if Quantidade_de_Números == "8":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
        print("O Resultado da multiplicação com dois valores é:", mult8)
    if Quantidade_de_Números == "9":
            n1 = float(input("Valor 1:"))
            n2 = float(input("Valor 2:"))
            n3 = float(input("Valor 3:"))
            n4 = float(input("Valor 4:"))
            n5 = float(input("Valor 5:"))
            n6 = float(input("Valor 6:"))
            n7 = float(input("Valor 7:"))
            n8 = float(input("Valor 8:"))
            n9 = float(input("Valor 9:"))
            mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
            print("O Resultado da multiplicação com dois valores é:", mult9)
    if Quantidade_de_Números == "10":
        n1 = float(input("Valor 1:"))
        n2 = float(input("Valor 2:"))
        n3 = float(input("Valor 3:"))
        n4 = float(input("Valor 4:"))
        n5 = float(input("Valor 5:"))
        n6 = float(input("Valor 6:"))
        n7 = float(input("Valor 7:"))
        n8 = float(input("Valor 8:"))
        n9 = float(input("Valor 9:"))
        n10 = float(input("Valor 10:"))
        mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
        print("O Resultado da multiplicação com dois valores é:", mult10)
if escolha == "pot":
    n1 = float(input("Valor 1:"))
    n2 = float(input("elevado a:"))
    pot2 = n1**n2
    print("o resultado da pontencialização é:", pot2)
    while True:
        texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
        if texto2 == "nao":
            print("voltando ao menu")
            escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
            if escolha == "soma":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "sub":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "mult":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")

            if escolha == "soma":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    soma2 = n1 + n2
                    print("O Resultado da soma com dois valores é:", soma2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    soma3 = n1 + n2 + n3
                    print("O Resultado da soma com dois valores é:", soma3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    soma4 = n1 + n2 + n3 + n4
                    print("O Resultado da soma com dois valores é:", soma4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    soma5 = n1 + n2 + n3 + n4 + n5
                    print("O Resultado da soma com dois valores é:", soma5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    soma6 = n1 + n2 + n3 + n4 + n5 + n6
                    print("O Resultado da soma com dois valores é:", soma6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                    print("O Resultado da soma com dois valores é:", soma7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                    print("O Resultado da soma com dois valores é:", soma8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                    print("O Resultado da soma com dois valores é:", soma10)
            if escolha == "sub":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    menos2 = n1 - n2
                    print("O Resultado da subtração com dois valores é:", menos2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    menos3 = n1 - n2 - n3
                    print("O Resultado da subtração com três valores é:", menos3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    menos4 = n1 - n2 - n3 - n4
                    print("O Resultado da soma com dois valores é:", menos4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    menos5 = n1 - n2 - n3 - n4 - n5
                    print("O Resultado da soma com dois valores é:", menos5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    menos6 = n1 - n2 - n3 - n4 - n5 - n6
                    print("O Resultado da soma com dois valores é:", menos6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                    print("O Resultado da soma com dois valores é:", menos7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                    print("O Resultado da soma com dois valores é:", menos8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                    print("O Resultado da soma com dois valores é:", menos9)
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                    print("O Resultado da soma com dois valores é:", menos10)
            if escolha == "mult":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    mult2 = n1 * n2
                    print("O Resultado da multiplicação com dois valores é:", mult2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    mult3 = n1 * n2 * n3
                    print("O Resultado da multiplicação com dois valores é:", mult3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    mult4 = n1 * n2 * n3 * n4
                    print("O Resultado da multiplicação com dois valores é:", mult4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    mult5 = n1 * n2 * n3 * n4 * n5
                    print("O Resultado da multiplicação com dois valores é:", mult5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    mult6 = n1 * n2 * n3 * n4 * n5 * n6
                    print("O Resultado da multiplicação com dois valores é:", mult6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                    print("O Resultado da multiplicação com dois valores é:", mult7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                    print("O Resultado da multiplicação com dois valores é:", mult8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                    print("O Resultado da multiplicação com dois valores é:", mult9)
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                    print("O Resultado da multiplicação com dois valores é:", mult10)
            if escolha == "pot":
                n1 = float(input("Valor 1:"))
                n2 = float(input("elevado a:"))
                pot2 = n1 ** n2
                print("o resultado da pontencialização é:", pot2)
            if escolha == "d":
                n1 = float(input("Valor 1:"))
                n2 = float(input("divido por:"))
                d = n1 / n2
                print("O Resultado da divisão é:", d)
            if escolha == "raiz":
                escolha = input("quadrada/cubica")
                if escolha == "quadrada":
                    n1 = float(input("Valor 1:"))
                    raiz = math.sqrt(n1)
                    print("A raiz quadrada de", n1, "é:", raiz)
                if escolha == "cubica":
                    n1 = float(input("Valor 1:"))
                    raiz = n1 ** (1 / 3)
                    print("A raiz cúbica de", n1, "é:", raiz)
        else:
            texto2 == "sim"
            n1 = float(input("Valor 1:"))
            n2 = float(input("elevado a:"))
            pot2 = n1 ** n2
            print("o resultado da pontencialização é:", pot2)
if escolha == "d":
    n1 = float(input("Valor 1:"))
    n2 = float(input("divido por:"))
    d = n1 / n2
    print("O Resultado da divisão é:", d)
    while True:
        texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
        if texto2 == "nao":
            print("voltando ao menu")
            escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
            if escolha == "soma":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "sub":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "mult":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "soma":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    soma2 = n1 + n2
                    print("O Resultado da soma com dois valores é:", soma2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    soma3 = n1 + n2 + n3
                    print("O Resultado da soma com dois valores é:", soma3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    soma4 = n1 + n2 + n3 + n4
                    print("O Resultado da soma com dois valores é:", soma4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    soma5 = n1 + n2 + n3 + n4 + n5
                    print("O Resultado da soma com dois valores é:", soma5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    soma6 = n1 + n2 + n3 + n4 + n5 + n6
                    print("O Resultado da soma com dois valores é:", soma6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                    print("O Resultado da soma com dois valores é:", soma7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                    print("O Resultado da soma com dois valores é:", soma8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                    print("O Resultado da soma com dois valores é:", soma10)
            if escolha == "sub":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    menos2 = n1 - n2
                    print("O Resultado da subtração com dois valores é:", menos2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    menos3 = n1 - n2 - n3
                    print("O Resultado da subtração com três valores é:", menos3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    menos4 = n1 - n2 - n3 - n4
                    print("O Resultado da soma com dois valores é:", menos4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    menos5 = n1 - n2 - n3 - n4 - n5
                    print("O Resultado da soma com dois valores é:", menos5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    menos6 = n1 - n2 - n3 - n4 - n5 - n6
                    print("O Resultado da soma com dois valores é:", menos6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                    print("O Resultado da soma com dois valores é:", menos7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                    print("O Resultado da soma com dois valores é:", menos8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                    print("O Resultado da soma com dois valores é:", menos9)
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                    print("O Resultado da soma com dois valores é:", menos10)
            if escolha == "mult":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    mult2 = n1 * n2
                    print("O Resultado da multiplicação com dois valores é:", mult2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    mult3 = n1 * n2 * n3
                    print("O Resultado da multiplicação com dois valores é:", mult3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    mult4 = n1 * n2 * n3 * n4
                    print("O Resultado da multiplicação com dois valores é:", mult4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    mult5 = n1 * n2 * n3 * n4 * n5
                    print("O Resultado da multiplicação com dois valores é:", mult5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    mult6 = n1 * n2 * n3 * n4 * n5 * n6
                    print("O Resultado da multiplicação com dois valores é:", mult6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                    print("O Resultado da multiplicação com dois valores é:", mult7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                    print("O Resultado da multiplicação com dois valores é:", mult8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                    print("O Resultado da multiplicação com dois valores é:", mult9)
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                    print("O Resultado da multiplicação com dois valores é:", mult10)
            if escolha == "pot":
                n1 = float(input("Valor 1:"))
                n2 = float(input("elevado a:"))
                pot2 = n1 ** n2
                print("o resultado da pontencialização é:", pot2)
            if escolha == "d":
                n1 = float(input("Valor 1:"))
                n2 = float(input("divido por:"))
                d = n1 / n2
                print("O Resultado da divisão é:", d)
            if escolha == "raiz":
                escolha = input("quadrada/cubica")
                if escolha == "quadrada":
                    n1 = float(input("Valor 1:"))
                    raiz = math.sqrt(n1)
                    print("A raiz quadrada de", n1, "é:", raiz)
                if escolha == "cubica":
                    n1 = float(input("Valor 1:"))
                    raiz = n1 ** (1 / 3)
                    print("A raiz cúbica de", n1, "é:", raiz)
        else:
            texto2 == "sim"
            n1 = float(input("Valor 1:"))
            n2 = float(input("divido por:"))
            d = n1 / n2
            print("O Resultado da divisão é:", d)
if escolha == "raiz":
    escolha = input("quadrada/cubica")
    if escolha == "quadrada":
        n1 = float(input("Valor 1:"))
        raiz = math.sqrt(n1)
        print("A raiz quadrada de", n1, "é:", raiz)
    if escolha == "cubica":
        n1 = float(input("Valor 1:"))
        raiz = n1**(1/3)
        print("A raiz cúbica de", n1 ,"é:", raiz)
    while True:
        texto2 = input("deseja continuar usando o mesmo operador?(sim/nao)")
        if texto2 == "nao":
            print("voltando ao menu")
            escolha = input("Escolha (soma/sub/mult/pot/div/raiz):")
            if escolha == "soma":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "sub":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "mult":
                Quantidade_de_Números = input("Quantidade de valores que vai ser utilizado (2/3/4/5/6/7/8/9/10):")
            if escolha == "soma":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    soma2 = n1 + n2
                    print("O Resultado da soma com dois valores é:", soma2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    soma3 = n1 + n2 + n3
                    print("O Resultado da soma com dois valores é:", soma3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    soma4 = n1 + n2 + n3 + n4
                    print("O Resultado da soma com dois valores é:", soma4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    soma5 = n1 + n2 + n3 + n4 + n5
                    print("O Resultado da soma com dois valores é:", soma5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    soma6 = n1 + n2 + n3 + n4 + n5 + n6
                    print("O Resultado da soma com dois valores é:", soma6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    soma7 = n1 + n2 + n3 + n4 + n5 + n6 + n7
                    print("O Resultado da soma com dois valores é:", soma7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    soma8 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                    print("O Resultado da soma com dois valores é:", soma8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    soma9 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    soma10 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
                    print("O Resultado da soma com dois valores é:", soma10)
            if escolha == "sub":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    menos2 = n1 - n2
                    print("O Resultado da subtração com dois valores é:", menos2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    menos3 = n1 - n2 - n3
                    print("O Resultado da subtração com três valores é:", menos3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    menos4 = n1 - n2 - n3 - n4
                    print("O Resultado da soma com dois valores é:", menos4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    menos5 = n1 - n2 - n3 - n4 - n5
                    print("O Resultado da soma com dois valores é:", menos5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    menos6 = n1 - n2 - n3 - n4 - n5 - n6
                    print("O Resultado da soma com dois valores é:", menos6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    menos7 = n1 - n2 - n3 - n4 - n5 - n6 - n7
                    print("O Resultado da soma com dois valores é:", menos7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    menos8 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8
                    print("O Resultado da soma com dois valores é:", menos8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    menos9 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9
                    print("O Resultado da soma com dois valores é:", menos9)
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    menos10 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10
                    print("O Resultado da soma com dois valores é:", menos10)
            if escolha == "mult":
                if Quantidade_de_Números == "2":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    mult2 = n1 * n2
                    print("O Resultado da multiplicação com dois valores é:", mult2)
                if Quantidade_de_Números == "3":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    mult3 = n1 * n2 * n3
                    print("O Resultado da multiplicação com dois valores é:", mult3)
                if Quantidade_de_Números == "4":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    mult4 = n1 * n2 * n3 * n4
                    print("O Resultado da multiplicação com dois valores é:", mult4)
                if Quantidade_de_Números == "5":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    mult5 = n1 * n2 * n3 * n4 * n5
                    print("O Resultado da multiplicação com dois valores é:", mult5)
                if Quantidade_de_Números == "6":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    mult6 = n1 * n2 * n3 * n4 * n5 * n6
                    print("O Resultado da multiplicação com dois valores é:", mult6)
                if Quantidade_de_Números == "7":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    mult7 = n1 * n2 * n3 * n4 * n5 * n6 * n7
                    print("O Resultado da multiplicação com dois valores é:", mult7)
                if Quantidade_de_Números == "8":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    mult8 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                    print("O Resultado da multiplicação com dois valores é:", mult8)
                if Quantidade_de_Números == "9":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    mult9 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9
                    print("O Resultado da multiplicação com dois valores é:", mult9)
                if Quantidade_de_Números == "10":
                    n1 = float(input("Valor 1:"))
                    n2 = float(input("Valor 2:"))
                    n3 = float(input("Valor 3:"))
                    n4 = float(input("Valor 4:"))
                    n5 = float(input("Valor 5:"))
                    n6 = float(input("Valor 6:"))
                    n7 = float(input("Valor 7:"))
                    n8 = float(input("Valor 8:"))
                    n9 = float(input("Valor 9:"))
                    n10 = float(input("Valor 10:"))
                    mult10 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
                    print("O Resultado da multiplicação com dois valores é:", mult10)
            if escolha == "pot":
                n1 = float(input("Valor 1:"))
                n2 = float(input("elevado a:"))
                pot2 = n1 ** n2
                print("o resultado da pontencialização é:", pot2)
            if escolha == "d":
                n1 = float(input("Valor 1:"))
                n2 = float(input("divido por:"))
                d = n1 / n2
                print("O Resultado da divisão é:", d)
            if escolha == "raiz":
                escolha = input("quadrada/cubica")
                if escolha == "quadrada":
                    n1 = float(input("Valor 1:"))
                    raiz = math.sqrt(n1)
                    print("A raiz quadrada de", n1, "é:", raiz)
                if escolha == "cubica":
                    n1 = float(input("Valor 1:"))
                    raiz = n1 ** (1 / 3)
                    print("A raiz cúbica de", n1, "é:", raiz)
        else:
            texto2 == "sim"
            escolha = input("quadrada/cubica")
            if escolha == "quadrada":
                n1 = float(input("Valor 1:"))
                raiz = math.sqrt(n1)
                print("A raiz quadrada de", n1, "é:", raiz)
            if escolha == "cubica":
                n1 = float(input("Valor 1:"))
                raiz = n1 ** (1 / 3)
                print("A raiz cúbica de", n1, "é:", raiz)

#ta errado no sub2 else.