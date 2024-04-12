try:
    x = int(input('Digite um número: '))
    resposta = 10/x
except ValueError:
    print('Digite um número válido!')
except Exception as erro:
    print(f'Erro não previsto: {erro}')
else:
    print(f'10 dividido por {x} é igual a {resposta}!')
finally:
    print('Fim do meu programa!')