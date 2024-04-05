
nomes = ['Matheus', 'Venicios', 'Zezinho', 'Luizinho']
idades = [24, 25, 19, 50]

for n in range(len(nomes)):
    print(f'{nomes[n]} tem {idades[n]} anos!')

for n, nome in enumerate(nomes):
    print(f'{nome} tem {idades[n]} anos!')


nomes.pop(2)

print(nomes)