#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a for loop program.


def main():
    # This is the function to run for loop.

    number = 0
    # Input
    user_input_number = input("Enter a positive integer:")
    print("")

    # Process & output
    try:
        user_input_number = int(user_input_number)
        if user_input_number >= 0:
            for_number = user_input_number
            user_input_number = user_input_number + 1
            for number in range(user_input_number):
                for_number = number * number
                print("{0}² = {1}".format(number, for_number))
                number = number + 1
        elif user_input_number < 0:
            print("Sorry, you did not enter a positive integer!")
    except Exception:
        print("You are not type in an integer!")


if __name__ == "__main__":
    main()
