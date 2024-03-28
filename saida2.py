# Saída com strings formatadas

nome = "Joaozinho"
idade = 15

print("Nome:", nome , "Idade", 15)
out = "Nome:", nome , "Idade", 15
print(type(out))

print("Nome: {} Idade {}".format(nome, idade))
out2 = "Nome: {} Idade {}".format(nome, idade)
print(type(out2))

print("Nome: {0} Idade {1}, Mas a idade do {0} é {1}, ou seria {1}?".format(nome, idade))


print(f"Nome: {nome} Idade {idade}")