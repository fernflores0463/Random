from math import *


def commandHelp():
    print("Here are the supported commands!")
    print("help - Help")
    print("pyth -  find the hypotenuse in a triangle given")
    print("summ - the summation of a number with a lower and an upper bound.")


def main():
    print("Welcome to Physics calculator! \nEnter a command:")
    command = input(">").upper()
    if command == "HELP":
        print("Here are the supported commands!")
        commandHelp()