import random
import array

numbers_bytes_array = array.array('i', [random.randint(-1000000, 1000000) for _ in range(1000)])

with open('files/randomnumbers.bin', 'wb') as file:
    file.write(numbers_bytes_array)

