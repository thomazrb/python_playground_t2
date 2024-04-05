# objeto pessoa <- propriedades (atributos): nome, idade, genero, endereço, cpf... 

# Lista de pessoas: pessoas = [pessoa1, pessoa2, pessoa3 ]

# pessoa1.atributo
# pessoa1.metodo()

class Pessoa:
    nome = ''
    idade = 0

print('Oi')
pessoa1 = Pessoa()
pessoa1.nome = 'Matheus'
pessoa1.idade = 24

print(pessoa1.nome)

pessoa2 = Pessoa()
pessoa2.nome = 'Venicios'
pessoa2.idade = 25

print(pessoa2.nome)
print(pessoa1.nome)
print(pessoa1.idade)

pessoas = [pessoa1, pessoa2]

print(type(pessoa1))

for pessoa in pessoas:
    print(f'{pessoa.nome} tem {pessoa.idade} anos!')


