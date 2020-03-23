import random
numbers = []

while len(numbers)<10:
    number=random.randint(1,100)
    numbers.append(number)
print(numbers)

#do tej pory wygenerowalam 10 przypadkowych liczb z zakresu 1-100


def sort(numbers):
    for x in range(0, len(numbers)-1):
        for y in range(0,len(numbers)-1):
            if numbers[y] > numbers[y + 1]:
                numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]
    return

sort(numbers)
print(numbers)
