result = []
def arithmetic_mean(*numbers):
    answer = input('Is it range or just numbers? ')
    if answer == 'range':
        if len(numbers) > 3:
            print('number of numbers need should be 3')
            return 0
        for number in range(numbers[0], numbers[1], numbers[2]):
            result.append(number)
        return sum(result) / len(result)
    elif answer == 'numbers':
        return sum(numbers) / len(numbers)
    

print(arithmetic_mean(10, 3, -1))

            