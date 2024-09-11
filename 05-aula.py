# Algoritmo média: criar um algoritmo que leia 4 notas
# e apresente uma media final

print("-- Algoritmo de calculo de média --\n")
valor1 = float(input("escrava sua nota da primeira unidade: "))
valor2 = float(input("escrava sua nota da segunda unidade: "))
valor3 = float(input("escrava sua nota da terceira unidade: "))
valor4 = float(input("escrava sua nota da quarta unidade: "))

media = valor1 + valor2 + valor3 + valor4
media2 = media / 2

print("\nsua média entre as notas da unidade foram: ", media2)
if(media2 > 7):{print("\nvocê passou !!!")}
if(media2 < 7):{print("\nvocê não passou :<")}
