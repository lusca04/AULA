#Lucas Santos Rodrigues e Andre
chekpoint1S1 = float(input("chekpoint1S1="))
chekpoint2S1 = float(input("chekpoint2S1="))
chekpoint3S1 = float(input("chekpoint3S1="))
sprint1S1 = float(input("sprint1S1="))
sprint2S1 = float(input("sprint2S1="))
globlal_solutionsS1 = float(input("global solutionsS1="))

menor_chekS1 = chekpoint1S1
if chekpoint3S1 < chekpoint1S1:
    menor_chekS1 = chekpoint3S1
if chekpoint2S1 < chekpoint1S1:
    menor_chekS1 = chekpoint2S1

media_S1 = (((chekpoint1S1 + chekpoint3S1 + chekpoint2S1 - menor_chekS1 + sprint1S1 + sprint2S1)/4) * 0.4) + (globlal_solutionsS1 * 0.6)

chekpoint1S2 = float(input("chekpoint1S2="))
chekpoint2S2 = float(input("chekpoint2S2="))
chekpoint3S2 = float(input("chekpoint3S2="))
sprint1S2 = float(input("sprint1S2="))
sprint2S2 = float(input("sprint2S2="))
globlal_solutionsS2 = float(input("global solutionsS2="))

menor_chekS2 = chekpoint1S2
if chekpoint3S2 < chekpoint1S2:
    menor_chekS2 = chekpoint3S2
if chekpoint2S2 < chekpoint1S2:
    menor_chekS2 = chekpoint2S2

media_S2 = (((chekpoint1S2 + chekpoint3S2 + chekpoint2S2 - menor_chekS2 + sprint1S2 + sprint2S2)/4) * 0.4) + (globlal_solutionsS2 * 0.6)
media_final= (media_S1 * 0.4 + media_S2 * 0.6)/ 2
if media_final >= 6:
    print("aprovado")

if media_final < 4:
    print("reprovado")

if media_final >=4 and media_final < 6:
    print("exame")
print("sua nota=", media_final)
