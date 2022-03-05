'''
RECURSIVE FUNCTIONS
Author: Sebastian Opiyo

- A simple recursive function example. 
'''

def recursive_func(n)-> int:
    if n <= 2:
        return 1
    return recursive_func(n -1 ) + recursive_func(n - 2)


if __name__ == '__main__':
    print(recursive_func(3))
    print(recursive_func(8))
    print(recursive_func(16))
    print(recursive_func(40))
    print(recursive_func(50))