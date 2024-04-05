class Pessoa:    

    def __init__(self, name, age, cpf):
        self.nome = name
        self.idade = age
        self.cpf = cpf

    def apresentar(self):
        print(f'{self.nome} tem {self.idade} anos! CPF: {self.cpf}')




