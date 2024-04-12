import re


email = input("Digite seu email: ")

# asadssds @ scxzxzcxzcxz . aassdss.aadsds


if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Por favor, insira um endereço de email válido.")
else:
    print("O e-mail é válido!")