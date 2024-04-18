#                                   exercicio 6
# pontos = 0
# questao = 1
#while questao <= 3:
  #resposta = input(f"Resposta {questao}:")
    #if questao == 1 and resposta == "a":
        #pontos = pontos + 3.33
    #elif questao == 2 and resposta == "b":
        # pontos = pontos + 3.33
   # elif questao == 3 and resposta == "c":
   #      pontos = pontos + 3.33
   # questao = questao + 1
# print(f"os pontos: {pontos:.0f}")
#                                   exercicio 7
# n = 1
# soma = 0
# while n<=10:
#     x = float(input(F"numero {n}:"))
#     soma = soma+x
#     n = n+1
#     cont += 1
# print(f"A soma é: {soma:.2f}")
# print(f"A média é: {soma/10:.2f}")
# print(f"A média é: {soma/(cont-1):.2f}")
#                                   exercicio 8/9
resp = input("O valor de deposito sera o mesmo todos os meses: (sim/nao)")
mes2= float(input("Por quantos meses sera armazenado?"))
dep = float(input("Digite a quantia a ser depositada: "))
tax = float(input("Quantia de juros: "))
mes = 1
while mes <= mes2:
    if resp == "sim":
        mes = mes2
        dep=(dep+((tax/100)*dep))*mes2
        print(f" Esta é a quantia no {mes} é {dep:.1f}")
        break
    elif resp == "nao":
        depmes = float(input("digite o valor a ser somado este mes:"))
        dep=dep+((tax/100)*dep) + depmes
        mes = mes-mes2
        print(f" Esta é a quantia no {mes} é {dep:.1f}")

