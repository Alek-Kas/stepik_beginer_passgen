import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
ambiguous = "il1Lo0O"
chars = ''  # будет содержать все символы, которые могут быть в генерируемом пароле.


def password_total():
    print('Введите количество паролей для генерации - ', end='')  # 0
    num = input()
    return num


def password_len():
    print('Введите длину одного пароля - ', end='')  # 1
    num = input()
    return num


def password_digits():
    pass


def password_lowercase_letters():
    pass


def password_uppercase_letters():
    pass


def password_punctuation():
    pass


def password_ambiguous():
    pass


def generate_password():
    pass


pass_total = password_total()
pass_len = password_len()
chars += password_digits()
chars += password_lowercase_letters()
chars += password_uppercase_letters()
chars += password_punctuation()
chars += password_ambiguous()

for i in range(pass_total):
    generate_password(pass_len, chars)
