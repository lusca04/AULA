print("As notas vão de 0 a 100")
print("A presença é computada em % e é necessario ter uma presença de 0.75 ou mais para passar")
presenca = float(input("Presença do aluno:"))
semestre = 1
boletim = [0,0,0,0]
boletim[2] = presenca/100
#======================================== Calculo das notas ======================================
while semestre <= 2:
    chek1 = float(input("Nota do chekpoint 1:"))
    chek2 = float(input("Nota do chekpoint 2:"))
    chek3 = float(input("Nota do chekpoint 3:"))
    spt1 = float(input("Nota do sprint 1:"))
    spt2 = float(input("Nota do sprint 2:"))
    glb = float(input("Nota do global solution:"))
    menor_chek = chek1
    if chek3 < chek1:
        menor_chek = chek3
    if chek2 < chek1:
        menor_chek = chek2
    boletim[0] = (((chek1+chek2+chek3-menor_chek+spt1+spt2)/4)*0.4)+(glb*0.6)
    if semestre == 2:
        boletim[1] = (((chek1+chek2+chek3-menor_chek+spt1+spt2)/4)*0.4)+(glb*0.6)
    semestre = semestre + 1
boletim[3] = (boletim[0]*0.4 + boletim[1]*0.6)
#============================================ BOLETIM ========================================
print(f"Sua presença no ano é de: {boletim[2]:.2f}")
print(f"Sua nota do primeiro semestre é: {boletim[0]:.0f}")
print(f"Sua nota do segundo semestre é: {boletim[1]:.0f}")
print(f"Sua média final é: {boletim[3]:.2f}")
print()
#================================= Presenca//nota = resultado final ==========================
if boletim[3] >= 6 and boletim[2] >= 0.75:
    print('Resultado final: Aprovado')
if boletim[3] >= 6 and boletim[2] < 0.75:
    print("Resultado final: Reprovado por falta")
if boletim[3] <= 4:
    print("Resultado final: Reprovado")
if boletim[3] > 4 and boletim[3] < 6 and boletim[2] >=0.75:
    print('Resultado final: Em exame')
if boletim[3] > 4 and boletim[3] < 6 and boletim[2] < 0.75:
    print("Resultado final: Reprovado por falta")
