km = 0.15
aluguel = 60

percurso = int(input("Digite a quantidade de km rodados com seu carro: "))
dias = int(input("Digite a quantidade de dias que seu carro está alugado: "))

total_km = km * percurso
total_aluguel = aluguel * dias

resultado = total_km + total_aluguel

print(f"\nVocê pagará atualmente: R$ {resultado}")
