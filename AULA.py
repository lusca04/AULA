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
# dep = float(input("Digite a quantia a ser depositada: "))
# tax = float(input("Quantia de juros: "))
# mes = 1
# while mes <= 24:
#     dep= dep+(dep*(tax/100))
#     print(f"{mes} é de R${dep:.2f}.")
#     mes= mes+1
# print(f"O Ganho é de R${dep:.2f}.")
#                                          LISTA
# lista = ['mayene', 'arthur', 'lucas', 'eduardo', 'pedro']         #lista começa na posição 0
# print(lista[2])                            #mandar printar a posição dentro da lista
# lista.sort()                               #arrumar em odrem alfabetica
# print(lista)                               #manda printar a lista
# idade =  [21,19,37,18]
# idade.sort()                               #arrumar em ordem crescente
# print(idade)
# idade.sort(reverse=True)                   #arrumar em ordem decrescente
# print(idade)
# idade.append(44)
# print(idade)
# idade.append([44,44])                      #adicionar uma lista dentro de outra lista
# print(idade)                                 #a lista dentro da lusta é considerada uma posição
# print(idade[5])
# print(idade[5][0])                           #posição da primeira lista e posição da lista dentro da lista
# idade.extend([3, 4])                         #adicionar mais de 1 item na lista
# print(idade)
# print(len(idade))                             #mostra quantos elementos tem na lista
# print(idade)
# print(idade[3:6])                               #colocar a posição inicial e a posição mais 1
# print(idade[:-1])                               #ele tira o ultimo elemento
# del idade[-3:]                                  #tira do fim ao fim
# idade.clear()                                   #limpa a lista
# print(idade)
# print(idade[-1])                                #printa o ultimo numero
# idade_backup = idade                            #copia a lista (tudo oq mudar em 1 lista muda em outra)
# print(idade_backup)
# idade_backup.append(122)
# print(idade)
# print(idade_backup)
# idade_backup = idade [:]                        #torna listas independentes de backup
# idade_backup = idade [0:3]                      #copia apenas os selecionados a outra lista
# idade.append(500)
# print(idade)
# print(idade_backup)
# del idade[2]                                    #deleta a coisa na posição

