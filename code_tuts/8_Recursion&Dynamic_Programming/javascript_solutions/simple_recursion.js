/*
RECURSIVE FUNCTIONS
Author: Sebastian Opiyo

- A simple recursive function example. 
*/

const fib = (n) => {
    if (n <= 2) return 1;
    return fib(n - 1) + fib(n - 2);
};

// TESTS
console.log(fib(3));
console.log(fib(8));
console.log(fib(16));
console.log(fib(40));
console.log(fib(50));