chek1 = float(input("Nota do chekpoint 1:"))
chek2 = float(input("Nota do chekpoint 2:"))
chek3 = float(input("Nota do chekpoint 3:"))
spt1 = float(input("Nota do sprint 1:"))
spt2 = float(input("Nota do sprint 2:"))
glb = float(input("Nota do global solution:"))
presenca = float(input("Presença do aluno:"))

menor_chek = chek1
if chek3 < chek1:
    menor_chek = chek3
if chek2 < chek1:
    menor_chek = chek2

semestre = 1
while semestre <= 2:
    media1= ((chek1+chek2+chek3-menor_chek+spt1+spt2/4)*0.4)+(glb*0.6)
    media1 = (media1*0.4)
    print(f'A média do primeiro semestre é: {media1:.2f}')
    semestre = semestre + 1
    if semestre == 2:
        chek1 = float(input("Nota do chekpoint 1:"))
        chek2 = float(input("Nota do chekpoint 2:"))
        chek3 = float(input("Nota do chekpoint 3:"))
        spt1 = float(input("Nota do sprint 1:"))
        spt2 = float(input("Nota do sprint 2:"))
        glb = float(input("Nota do global solution:"))
        media2 = ((chek1+chek2+chek3-menor_chek+spt1+spt2/4)*0.4)+(glb*0.6)
        media2 = (media2*0.6)
        print(f"A média do primeiro semestre é:{media2:.2f}")
if presenca >= 0.75
    print("Aprovado")
mediaf = (media1+media2/2)
print(f"mediaf = {mediaf:.2f}")


