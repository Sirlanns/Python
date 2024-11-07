##27*-nome-nota.py
# Desenvolva um programa que leia os nomes e notas de 5 alunos e, em seguida, mostre o nome e a nota de cada um.

# Lista para armazenar os nomes e notas
alunos = []

# Loop para ler os dados dos alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    alunos.append((nome, nota))

# Exibir os nomes e notas dos alunos
print("\nNomes e notas dos alunos:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Nota: {aluno[1]}")