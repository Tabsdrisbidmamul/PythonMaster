print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = map(lambda x: x**2, numbers)
for s in squares:
    print(s)

squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

squares = [x ** 2 for x in numbers]
print(squares)