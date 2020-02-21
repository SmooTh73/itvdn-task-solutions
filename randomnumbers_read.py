import array
import os.path

filename = 'files/randomnumbers.bin'
filesize = os.path.getsize(filename)
count = filesize // array.array('i').itemsize
numbers = array.array('i', (0 for _ in range(count)))

with open(filename, 'rb') as file:
    file.readinto(numbers)

print(numbers)