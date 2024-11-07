#Esse código tem como função indicar o seu índice de massa corporal

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura * altura)

if imc < 18.5:
    print(f"seu imc é {imc:.2f}")
    print("Você está abaixo do peso!!!")

elif imc >= 18.5 and imc <= 24.9:
    print(f"seu imc é {imc:.2f}")
    print("Seu peso está normal")

elif imc >= 25 and imc <= 34.9:
    print(f"seu imc é {imc:.2f}")
    print("Você está com sobrepeso")

elif imc >= 35:
    print(f"seu imc é {imc:.2f}")
    print("Atenção!!! Você está obeso")
