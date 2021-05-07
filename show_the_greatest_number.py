#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program gets 3 numbers as input and shows the greater one


def main():
    print("Insert 3 numbers:")

    number1_input = input()
    number2_input = input()
    number3_input = input()

    try:
        number1_float = float(number1_input)
        number2_float = float(number2_input)
        number3_float = float(number3_input)

        if number1_float > number2_float:
            if number1_float > number3_float:
                print("\nThe greatest number is: {}".format(number1_input))
            else:
                print("\nThe greatest number is: {}".format(number3_input))
        else:
            if number2_float > number3_float:
                print("\nThe greatest number is: {}".format(number2_input))
            else:
                print("\nThe greatest number is: {}".format(number3_input))
    except Exception:
        print("\nThis input is invalid, please, insert a number.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
