
from tkinter import N


def fizzbuzz(n):
    ansList = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            ansList.append("FizzBuzz")
        elif i %3 == 0:
            ansList.append("Fizz")
        elif i %5 == 0:
            ansList.append("Buzz")
        else:
            ansList.append(str(i))
    return ansList
print(fizzbuzz(15))