### Anotação
##Caracteristicas principais
# Ordenadas: Cada elemento em uma lista tem um índice específico, começando em 0. Isso significa que você pode acessar elementos por sua posição.
# Mutáveis: Você pode modificar uma lista após sua criação, adicionando, removendo ou alterando elementos.
# Heterogêneas: Uma lista pode conter elementos de diferentes tipos de dados.
# Dinâmicas: O tamanho de lista não é fixo. Você pode adicionar ou remover elementos a qualquer momento.

##Acessando elementos
# - voce pode acessar um elemento especifivos de uma lista usando seu indice:
#   minha_lista = [1,2,3,"ola",9.0,True]
# primeiro_elemento = minha_listaa[0] # Acessa o primeiro elemento (1)
# ultimo _elemento = minha_lista[-1] # Acessa o ultimo elemento (True)

##Criando listas
#  - voce pode criar uma lista usando colchetes e separando os elementos com virgula
# minha_lista = [1,2,3,"ola",9.0,true]
# - voce tambem pode criar uma lista vazia
# lista_vazia = []

##Operações com listas
# - Acessar elementos: lista[0]
# - Modificar elementos: lista[2] = 10
# - Adicionar elementos ao final da lista: lista.append(6)
# - Inserir elementos em uma posição específica : lista.insert(2,8)
# - Remover o primeiro elementos com o valor especificado : lista.remove(4)
# - Remove e retorna o elemento em uma posição específica: lista.pop(1)
# - verificar existência: if 3 in lista

##Exempo: usando For para percorrer Lista
# Frutas = ["maçã","banana","laranja"]
#  for fruta in frutas:
#      print(fruta)

##Lista-número-inteiros.py (atividade)
# Crie uma lista de 5 números inteiros fornecidos pelo usuário e imprima o maior, o menor e a soma de todos os elementos.

print("escreva 5 numeros a seguir:")
minha_lista = []

# Usando um loop for para coletar os números
for i in range(5):
    numero = int(input(f"numero {i + 1}: "))
    minha_lista.append(numero)

print("maior: \n", max(minha_lista))
print("menor: \n", min(minha_lista))
print("soma: \n", sum(minha_lista))
print(minha_lista)