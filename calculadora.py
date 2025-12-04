valor_1 = int(input('Digite o 1° valor: '))
valor_2 = int(input('Digite o 2° Valor: '))
menu = 1
while menu != 5:
    print('''O que você deseja fazer com esses números?
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS 
    [5] SAIR DO PROGRAMA''')
    menu = int(input('Escolha um comando do Menu: '))
    if menu == 1:
        print(f'[1] SOMAR > {valor_1} + {valor_2} = {valor_1+valor_2}.\n')
    if menu == 2:
        print(f'[2] MULTIPLICAR > {valor_1} x {valor_2} = {valor_1*valor_2}\n')
    if menu == 3:
        maior = valor_1 > valor_2
        print(f'[3] MAIOR NÚMERO > {max(valor_1,valor_2)}')
    if menu == 4:
        print(f'[4] NOVOS NÚMEROS')
        valor_1 = int(input('Digite o 1° valor: '))
        valor_2 = int(input('Digite o 2° Valor: '))
print('FIM DO PROGRAMA')