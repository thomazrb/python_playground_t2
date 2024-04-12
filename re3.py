import re

def sanitize_input(input_text):
    sanitized_text = re.sub(r'[^a-zà-úA-ZÀ-Ú0-9 \.]', '', input_text)
    return sanitized_text


frase = input('Digite algo: ')
print(frase)
frase_sanitizada = sanitize_input(frase)
print(frase_sanitizada)