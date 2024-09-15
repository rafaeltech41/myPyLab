import random
import string

def generate_password(length=12):
    # Definindo os caracteres permitidos: letras maiúsculas, minúsculas, números e caracteres especiais
    characters = string.ascii_letters + string.digits + string.punctuation
    # Gerando a senha de forma aleatória
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Gerando uma senha com 12 caracteres
print(generate_password())
