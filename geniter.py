def myiterator(user_list):
    index = len(user_list) - 1
    while index >= 0:
        yield user_list[index]
        index = index - 1

mylist = [1, 2, 3, 4, 5]

for number in myiterator(mylist):
    print(number)