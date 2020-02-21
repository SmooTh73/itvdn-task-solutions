first = input('First word: ')
second = input('Second word: ')

if ' ' in first or ' ' in second:
    print('Ви ввели більше 1 слова')
else:
    print('{}, {}'.format(first, second))