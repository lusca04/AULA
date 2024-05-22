
        if check2 < check1:
            menor_nota = check2
        if check3 < check1:
            menor_nota = check3
        mediasem = (((check1 + check2 + check3 + sprint1 + sprint2 - menor_nota)/4) * 0.4) + (gs * 0.6)
        if sem == 1:
            notas_S1.extend([check1, check2, check3, sprint1, sprint2, gs])
            mediafin = mediafin + (mediasem * 0.4)
        elif sem == 2:
            notas_S2.extend([check1, check2, check3, sprint1, sprint2, gs])
            mediafin = mediafin + (mediasem * 0.6)
        sem = sem + 1
    print(f"\nDisciplina = {disc}")
    print(f"Frequência = {presenca}%")
    x1 = 0
    x2 = 0
    tipo = ''
    notas = notas_S1[:]
    print("\nNotas do 1º semestre:")
    while x1 < (len(notas_S1)+len(notas_S2)):
        if x1 < len(notas_S1):
            if x1 < 3:
                tipo = f'Checkpoint {x1 + 1}'
            if x1 >= 3:
                tipo = f"Sprint {x1 - 2}"
            if x1 == 5:
                tipo = 'Global Solution'
        if x1 == len(notas_S1):
            print("\nNotas do 2º semestre:")
            x2 = 0
        if x1 >= len(notas_S1):
            notas = notas_S2[:]
            if x2 < 3:
                tipo = f'Checkpoint {x2 + 1}'
            if x2 >= 3:
                tipo = f"Sprint {x2 - 2}"
            if x2 == 5:
                tipo = 'Global Solution'
        print(f"{tipo} = {notas[x2]}")
        x2 += 1
        x1 += 1
    print(f"\nMédia final = {mediafin:.0f}")
    if mediafin > 60 and presenca >= 75:
        print("Situação = Aprovado")
    elif mediafin >= 40 and presenca >= 75:
        print("Situação = Exame")
    else:
        print("Situação = Reprovado")
    sem = 1
    mediafin = 0
    notas_S1.clear()
    notas_S2.clear()
    sair = input("\nDeseja realizar os cálculos de outra disciplina (digite sim ou não)? ").upper()
    if sair == "NÃO":
        break
