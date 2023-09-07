import string, random

letters = string.ascii_letters
symbols = '()!@#$%_+-'
digits = string.digits

characters = symbols + letters + digits

password = ''
def generate_password(length):
    return '\n Generated Password: '+password.join(random.sample(characters,length) + '\n')


def choice(l):
    if l.lower() == "q":
        print('Thanks for using Password generator!')
        quit()
    else:
        return int(l)

def main():
    print('Welcome to Password Generator')
    print('Enter "Q" at any point quit the program')
    l = input('Enter desired length: ')
    print(generate_password(choice(l)))


if __name__=='__main__':
    while True:
        main()