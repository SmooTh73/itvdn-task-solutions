list_of_numbers = []
number_of_numbers = int(input("How many numbers do you want to write? "))
for number in range(number_of_numbers):
    number = int(input('Write the number: '))
    list_of_numbers.append(number)


for number in range(number_of_numbers - 1):
    for second_number in range(number_of_numbers - number - 1):
        if list_of_numbers[second_number] > list_of_numbers[second_number + 1]:
            list_of_numbers[second_number], list_of_numbers[second_number + 1] = list_of_numbers[second_number + 1], list_of_numbers[second_number]
list_of_numbers.sort(reverse=True)
print(list_of_numbers)    
