#!/usr/bin/env python3
import sys


def print_message(message="Hello"):
    """print message"""
    for _ in range(5):
        print("This was the message passed as argument: {}".format(message))

        
if __name__ == "__main__":
    print_message()
    print("This script was executed using Python {}".format(sys.version))
