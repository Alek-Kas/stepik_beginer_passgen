from random import choice

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
ambiguous = "il1Lo0O"
chars = ''  # будет содержать все символы, которые могут быть в генерируемом пароле.


def password_total():
    print('Введите количество паролей для генерации - ', end='')  # 0
    num = input()
    while not num.isdigit():
        print('Вы ввели не число, пожалуйста введите число: ')
        print('Введите количество паролей для генерации - ',  end='')
        num = input()
    return int(num)


def password_len():
    print('Введите длину одного пароля - ', end='')  # 1
    num = input()
    while not num.isdigit() or int(num) < 1:
        print('Вы ввели не число или число меньше 1, пожалуйста введите целое число больше 1: ')
        print('Введите длину одного пароля - ',  end='')
        num = input()
    return int(num)


def password_digits():
    print(f'Введите 1, если хотите использовать в пароле цифры: ', end='')
    q = input()
    return digits if q == '1' else ''


def password_lowercase_letters():
    print(f'Введите 1, если хотите использовать в пароле буквы в нижнем регистре: ', end='')
    q = input()
    return lowercase_letters if q == '1' else ''


def password_uppercase_letters():
    print(f'Введите 1, если хотите использовать в пароле буквы в верхнем регистре: ', end='')
    q = input()
    return uppercase_letters if q == '1' else ''


def password_punctuation():
    print(f'Введите 1, если хотите использовать в пароле символы пунктуации: ', end='')
    q = input()
    return punctuation if q == '1' else ''


def password_ambiguous(chars):
    print(f'Введите 1, если хотите исключить из пароля не однозначные символы: ', end='')
    chars_out = chars
    q = input()
    if q == '1':
        chars_out = ''
        for c in chars:
            if c not in ambiguous:
                chars_out += c
    return chars_out


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
