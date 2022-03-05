'''
RECURSIVE FUNCTIONS
Author: Sebastian Opiyo

- A simple recursive function example. 
- DP Optimized recursive solution.

'''

# Create a cache list
def memoize(n:int):
    cache = [-1 for x in range(n + 1 )]
    return cache



if __name__ == '__main__':
    print(memoize(3))