#!/usr/bin/env python3

# prints hex values of input inspired by the Hex On TSO option from ibm Mainframes

from sys import argv, stdin

def read_file(inputFile):

    for line in inputFile:
        hexout1, hexout2 = "|", "|"
        for char in line:
            hexChar = hex(ord(char))
            hexout1 += hexChar[-2]
            hexout2 += hexChar[-1]
        print(" " + line + hexout1 + "|\n" + hexout2 + "|\n")


if __name__ == "__main__":
    if len(argv) <= 1:
        inputFile = stdin
        read_file(inputFile)

    else:
        for e in range(1, len(argv)):
            try:
                with open(argv[e], mode="r", buffering=1) as inputFile:
                    read_file(inputFile)
            except FileNotFoundError:
                print("could not read file")


