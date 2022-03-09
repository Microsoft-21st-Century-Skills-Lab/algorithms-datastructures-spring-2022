'''
RECURSIVE FUNCTIONS
Author: Sebastian Opiyo

- Recursive function examples for Top-down with memoization & Bottom-up with tabulation. 
- DP Optimized recursive solution.

'''

# 1. Top-down with memoization
# Number of calls made 6 <fib(n) = n + 1 calls ==> O(n)
# Time complexity has been reduced from O(2^n) to O(n)
def calculate_fibonacci(n: int )-> int:
    memoize = [-1 for x in range(n + 1 )]
    return calculate_fibonacci_recur(memoize, n)

def calculate_fibonacci_recur(memoize, n):
    if n < 2:
        return n

    # If we have solved the problem already, simply return the cached result
    if memoize[n] >= 0:
        return memoize[n]
    
    # If not, we calculate and store
    memoize[n] = calculate_fibonacci_recur(memoize, n -1) + calculate_fibonacci_recur(memoize, n - 2)
    return memoize[n]



# 2.Bottom-up with tabulation
def calculateFibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i -1] + dp[i-2])
        # print(dp)
    return dp[n]



if __name__ == '__main__':
    # Top-down
    print(f'The 5th Fibonacci is --> {str(calculate_fibonacci(5))}')
    # print(f'The 10th Fibonacci is --> {str(calculate_fibonacci(10))}')
    # print(f'The 50th Fibonacci is --> {str(calculate_fibonacci(50))}')

    # Bottom-up
    # print(f'The 5th Fibonacci is --> {str(calculateFibonacci(5))}')
    # print(f'The 10th Fibonacci is --> {str(calculateFibonacci(10))}')
    # print(f'The 50th Fibonacci is --> {str(calculateFibonacci(50))}')