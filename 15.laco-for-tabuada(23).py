# algoritmo para exibir a tabuada de um número fornecido pelo usuário

# Gustavo Henrique - 2° ano F

# solicita ao usuário que insira um número:

numero = int(input("digite um número para ver sua tabuada: "))

# utilizando o laço for:

for i in range(1,11): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")