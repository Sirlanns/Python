print("Escolha entre calculadora funcional e tiração de média: \n")
print("1 - calculadora funcional")
print("2 - tiração de media")

escolha1 = int(input("Escolha uma opção: "))
if escolha1 == 1:
    print("Calculadora funcional")
    valorA = int(input("coloque o valorA: "))
    valorB = int(input("coloque o valorB: "))

    print("\ndigite a operação desejada para o calculo: ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - potenciação")
    print("6 - sair do progama")

    escolha = int(input("\nEscolha uma opção: \n"))
    if escolha == 1:
        print("\nSoma: ", valorA + valorB)
    elif escolha == 2:
        print("\nSubtração: ", valorA - valorB)
    elif escolha == 3:
        print("\nMultiplicação: ", valorA * valorB)
    elif escolha == 4:
        print("\nDivisão:  ", valorA / valorB)
    elif escolha ==  5:
        print("\npotenciação:  ", valorA ** valorB)
    elif escolha ==  6:
        print("\nPrograma encerrado")
elif escolha1 == 2:
    print("Tiração de media")
    valor_de_médias = int(input("escolha quantos valores terão na media:"))
    medias = [] #adicionar o valor à lista

    for i in range(valor_de_médias):
        valor = float(input(f"Digite o valor {i+1}: "))
        medias.append(valor) #adiciona o valor á lista

    #Calcula a média
    media = sum(medias) / len(medias)
    print(f"A média é: {media:.2f}")
