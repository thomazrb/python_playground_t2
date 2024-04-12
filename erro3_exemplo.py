

while True:
    try:
        idade = int(input('Digite a sua idade (apenas números inteiros positivos): '))
    except:
        print('Idade inválida')
    else:
        if idade > 0:
            print('A sua idade é {0} anos.'.format(idade))
            break
        else:
            print('Idade inválida')

print('Acabou!')