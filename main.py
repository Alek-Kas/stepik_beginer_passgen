import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
chars = ''  # будет содержать все символы, которые могут быть в генерируемом пароле.


def pass_gen():
    pass


print('Количество паролей для генерации - ', end='')
pass_total = int(input())
print('Длину одного пароля - ', end='')
pass_len = int(input())
print(f'Использовать в коде {digits}', end='')
q = input()
print(f'Использовать в коде {lowercase_letters}', end='')
q = input()
print(f'Использовать в коде {uppercase_letters}', end='')
q = input()
print(f'Использовать в коде {punctuation}', end='')
q = input()
for i in range(pass_total):
    pass_gen(chars, pass_len)
