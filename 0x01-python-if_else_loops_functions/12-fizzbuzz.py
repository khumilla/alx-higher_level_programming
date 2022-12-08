#!/usr/bin/python3

""" Print 1 - 100 with a space
    Multiples of 3, print Fizz instead of the number
    Multiples of 5, print Buzz instead
    Multiples of 3 and 5, print FizzBuzz
    """


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end='')
        elif number % 3 == 0:
            print("Fizz ", end='')
        elif number % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(number), end='')
