import string,random

letters = string.ascii_letters
symbols = '()!@#$%_+-'
digits = string.digits

characters = symbols + letters + digits

password = ''
def generate_password(length):
    return password.join(random.sample(characters,length))


