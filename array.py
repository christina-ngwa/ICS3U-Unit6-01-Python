#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: December 2019
# This program finds the average od random numbers


import random


def main():
    # this function uses an array
    avg = 0
    my_numbers = []

    # output
    print("Let's find the average of random numbers.")
    # process
    for counter in range(0, 10):
        num = random.randint(1, 100)
        my_numbers.append(num)
        print(my_numbers[counter], ". ", end="")
        avg = my_numbers[counter] + avg
    avg = avg / 10

    print("")
    print("")
    print("The average of these 10 numbers is: ", avg)


if __name__ == "__main__":
    main()
