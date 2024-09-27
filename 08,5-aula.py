cigarros = int(input("Quantos cigarros você fuma por dia: "))
anos_fumando = int(input("Por quantos anos você tem fumado: "))

min_perdidos_diariamente = 10 * cigarros
dias_por_cigarro = min_perdidos_diariamente / 1440
dias_perdidos = dias_por_cigarro * (365 * anos_fumando)

print(f"\nO total de dias que você perdeu foi: {int(dias_perdidos)}\nCUIDADO!!!")
