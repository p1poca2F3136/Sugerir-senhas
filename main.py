import random
import string

def generate_password(length):
    """
    Função para gerar senhas aleatórias com o tamanho especificado.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Exemplo de uso: gerar uma senha de 12 caracteres
password = generate_password(12) #Se alguém quiser que gere uma senha com mais caracteres basta substituir (12) pelo número desejado
print(password)