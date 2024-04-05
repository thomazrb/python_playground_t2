
class Pessoa:    

    def __init__(self, name, age, cpf):
        self.nome = name
        self.idade = age
        self.cpf = cpf

    def apresentar(self):
        print(f'{self.nome} tem {self.idade} anos! CPF: {self.cpf}')


pessoa1 = Pessoa('Matheus', 24, 1234)
pessoa2 = Pessoa('Venicios', 25, 1445)

pessoas = [pessoa1, pessoa2]

pessoa = Pessoa('Luizinho', 19, 3123)
pessoas.append(pessoa)
pessoa = Pessoa('Zezinho', 50, 3123)
pessoas.append(pessoa)

pessoas.pop(2)

for pessoa in pessoas:
    pessoa.apresentar()