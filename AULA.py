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
# ------------------------------------------------- 2 semestre ---------------------------------------------------------------
# alunos = ["Lucas", "luquinhas", "lulu", "lu"]
# for celibato in alunos:
#     print(celibato)
# ------------------------------------------------------------------------------
# vini= [0,1,2,3,4,5,6,7,8,9,10]
# vinis = float(input("DIgite o Numero desejado: "))
# for sapo_cego in vini:
#     if sapo_cego == vinis:
#         print("ACHEI")
#         break
# else:
#     print("Tem certeza boy?")
# ----------------------------------------------------------------------------
# name= ["Lucas", "Lulu", "Lu", "Luquinhas"]
# nomes = input("DIgite o nome desejado: ").capitalize()
# for n in name:
#     if n == nomes:
#         print("ACHEI")
#         break
# else:
#     print("Tem certeza boy?")
# -----------------------------------------------------------------------------
# ii = 0
# iii = int(input("Digite qual tabuada voce quer: "))
# while ii <= 10:
#     for i in range(0,(iii*10)+1,iii):
#         print(iii, "x ", ii, "=", i)
#         ii = ii + 1
#     break
# ------------------------------------------------------------------------------
# ii = 0
# iii = int(input("Digite qual tabuada voce quer: "))
# q = [0]
# l = q[0]
# ll = q[0]
# for i in range(0,(iii*10)+1,iii):
#     q.append(i)
#     # print(q)
#     for u in q:
#         if u > l:
#             l = u
#             # print(q)
#             # print(l)
#         if u == 0:
#             ll = u * 2
#             # print(ll)
#             break
# print(l)
# print(ll)
# -------------------------------------------------------------------------------------------
# tabela = {"letuce": 0.45, "potato": 1.2, "tomato": 2.3, "been": 1.5}
# print(tabela)
# print(cadastro)
# cadastro.append([dados]["1"])
# cadastro = {"1":["43772981860", "Lucas",2005,"digimom"], "48150489835":["Gustavo",2004, "pokémom"],
#             "sp":["Paulista"], "rj":["ladrão"]}
# print(cadastro)
# print(cadastro[43772981860])
# cadastro ["43772981860"][0] = "Lucas"
# print(cadastro["43772981860"])
# cadastro = {"1":[0,0,0], "2":[0,0,0], "3":[0,0,0]}
# while True:
#     cadastro["1"][0] = input("Cpf: ")
#     cadastro["1"][1] = input("Nome: ")
#     cadastro["1"][2] = input("data de nascimento: ")
#     cadastro["2"][0] = input("Cpf: ")
#     cadastro["2"][1] = input("Nome: ")
#     cadastro["2"][2] = input("data de nascimento: ")
#     break
# print(cadastro["1"])
# print(f"Infos: {cadastro["1"][1]} do cpf {cadastro["1"][0]} nasceu em {cadastro["1"][2]}")

# cadastro = {"43772981860":["Lucas",2005,"digimom", 18],
            # "48150489835":["Gustavo",2004, "pokémom", 19]}
# chaves = input("key pass:")
# if chaves == cadastro.items(valores[2]):
    # for chave, valores in cadastro.items():
        # print("nome:", valores[0])
        # print("cpf:", chave)
        # print("Keyword", valores[2])
        # print(f"Ano nasc. e idade: {valores[1]}/{valores[3]}\n")
        # print("Keyword", valores[2])
# ------------------------------------------------------------------------------------------------------------
# nomes = ("A1", "B2" ,"C1", "D2", "E1", "F2", "G1")
# # print(nomes)
# # nem da pra mudar ssa poha
# # print(nomes[1])
# a, b, c, d, e, f, g = nomes
# print(a)
# print(b)
# print(c)
# print(e)
# print(f)
# print(g)
# print(type(nomes))

# food = ("bolo",)
# # tem q ter 2 algarismos dentro da lista para ser uma truple
# print(food)
# print(type(food))
# print(len(food))
# 
# animais = ["ARTHUR", "Gustavo", "Lucas", "vinicius"]
# animais_tupla = tuple(animais)
# animais_tupla_02 = tuple(animais)
# print(tuple(animais))
# print(animais_tupla_02, animais_tupla)
# print(animais_tupla)
# a,b,c,d = animais_tupla
# print(a)
