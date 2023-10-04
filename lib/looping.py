#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown in range(10, 0, -1):
        print(countdown)
        countdown -= 1
    print("Happy new year!")


print(happy_new_year())

def square_integers(int_list):
    return [i ** 2 for i in int_list]

print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

print(fizzbuzz())
