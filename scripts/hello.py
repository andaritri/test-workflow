#!/usr/bin/env python3

def print_message():
    """print message"""
    for _ in range(10):
        print("from caller workflow!")

        
if __name__ == "__main__":
    print_message()
