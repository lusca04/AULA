dep = float(input("Digite a quantia a ser depositada: "))
tax = float(input("Quantia de juros: "))
mes = 1
while mes <= 24:
dep= dep+(dep*(tax/100))
print(f"{mes} é de R${dep:.2f}.")
mes= mes+1
print(f"O Ganho é de R${dep:.2f}.")
