#ferramenta break
#É uma ferramenta para interromper e encerrar um loop
#Isso quer dizer que vamos parar o loop naquele momento e vamos sair dele
#Execute o código abaixo e explique o que ele faz

while True:
    nome = input('Digite o seu nome ou escreva "sair": ')
    if nome == 'sair':
        break
    print(f'seu nome é {nome}')
print('acabou')