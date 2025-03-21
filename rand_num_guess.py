#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-03-21

# sets random number and makes user guess it.

import random


def main():
    print("Greetings! Please input a number")
    user_input = input("Please enter a number: ")
    Random_number = random.randint(0, 9)

    number = float(user_input)
    if number == Random_number:
        print("Congratulations! Correct!")
    else:
        print("Incorrect, try again :(")


if __name__ == "__main__":
    main()
