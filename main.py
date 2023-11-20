from random import choice

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
ambiguous = "iIl1Lo0O"
chars = ''  # будет содержать все символы, которые могут быть в генерируемом пароле.


def password_total():
    num = input('Введите количество паролей для генерации - ')
    while not num.isdigit():
        print('Вы ввели не число, пожалуйста введите число: ')
        num = input('Введите количество паролей для генерации - ')
    return int(num)


def password_len():
    num = input('Введите длину одного пароля - ')
    while not num.isdigit() or int(num) < 1:
        print('Вы ввели не число или число меньше 1, пожалуйста введите целое число больше 1: ')
        num = input('Введите длину одного пароля - ')
    return int(num)


def password_digits():
    q = input('Введите 1, если хотите использовать в пароле цифры: ')
    return digits if q == '1' else ''


def password_lowercase_letters():
    q = input('Введите 1, если хотите использовать в пароле буквы в нижнем регистре: ')
    return lowercase_letters if q == '1' else ''


def password_uppercase_letters():
    q = input('Введите 1, если хотите использовать в пароле буквы в верхнем регистре: ')
    return uppercase_letters if q == '1' else ''


def password_punctuation():
    q = input('Введите 1, если хотите использовать в пароле символы пунктуации: ')
    return punctuation if q == '1' else ''


def password_ambiguous(chars):
    q = input('Введите 1, если хотите исключить из пароля не однозначные символы: ')
    if q == '1':
        for c in ambiguous:
            chars = chars.replace(c, '')
    return chars


def generate_password(pass_len, chars):
    password = [choice(chars) for _ in range(pass_len)]
    return ''.join(password)


pass_total = password_total()
pass_len = password_len()
chars += password_digits()
chars += password_lowercase_letters()
chars += password_uppercase_letters()
chars += password_punctuation()
chars = password_ambiguous(chars)

if len(chars) < 1:
    print('Недостаточно символов для генерации пароля')
else:
    print()
    for i in range(pass_total):
        print(f'Пароль {i + 1}: ', end='')
        print(generate_password(pass_len, chars))
