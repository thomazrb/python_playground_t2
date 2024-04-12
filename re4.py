import re

padrao = r'^[1-9][0-9]*$'

if re.match(padrao, '3'):
    print('Deu bom!')
