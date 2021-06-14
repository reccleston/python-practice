import sys

def is_disarium(num):
    sum = 0
    for i, digit in enumerate(str(num)):
        position = i + 1
        sum += int(digit) ** position
    return num == sum    

print(is_disarium(int(sys.argv[1])))