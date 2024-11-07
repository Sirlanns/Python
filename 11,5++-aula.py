contador = 0
while contador <= 40:
    contador += 1 

    #verifica se o valor de 'contador' é multiplo de 4
    if (contador % 4 == 0):
        print ("pim") # Se for multiplo de 4, imprime "pim"
        continue # interrompe a interação atual e volta para  o início do loop

    # Se o número não for multiplo de 4, imprime o valor do contador
    print(contador)
# Apos o termino do loop, imprime a mensagem de finalisação
print("Fim do progama")
