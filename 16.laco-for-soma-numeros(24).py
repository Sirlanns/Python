# um algoritmo que calcula a soma dos números pares entre 1 e 50

# Gustavo Henrique - 2° ano F

soma = 0 

# utilizando o laço for:

for numero in range(1,51):
    if numero % 2 == 0:
        soma += numero 

print(f" a soma dos números pares entre 1 e 50 é: {soma}.")