print("As notas vão de 0 a 100")
presenca = float(input("Presença do aluno:"))
semestre = 1
while semestre <= 2:
    chek1 = int(input("Nota do chekpoint 1:"))
    chek2 = int(input("Nota do chekpoint 2:"))
    chek3 = int(input("Nota do chekpoint 3:"))
    spt1 = int(input("Nota do sprint 1:"))
    spt2 = int(input("Nota do sprint 2:"))
    glb = int(input("Nota do global solution:"))
    menor_chek = chek1
    if chek3 < chek1:
        menor_chek = chek3
    if chek2 < chek1:
        menor_chek = chek2
    media1 = (((chek1+chek2+chek3-menor_chek+spt1+spt2)/4)*0.4)+(glb*0.6)
    if semestre == 1:
        print(f"A média do primeiro semestre é:{media1:.0f}")
    if semestre == 2:
        media2 = (((chek1+chek2+chek3-menor_chek+spt1+spt2)/4)*0.4)+(glb*0.6)
        print(f"A média do segundo semestre é:{media2:.0f}")
    semestre = semestre + 1

mediaf = (media1*0.4) + (media2*0.6)
print(f"A média final é:{mediaf:.0f}")

if presenca < 75:
    print("REPROVADO")
else:
    print("APROVADO")

