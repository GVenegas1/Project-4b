#project-4b

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 10/22/2025
# Description: The function Calculates the Fibonacci number at a
# given position in the sequence using a while loop. Each number is the
#sum of the two previous  numbers.

def fib(n):
    """Return the nth Fibonacci number at a given position using a loop
        n ( int): the position of the fibonacci number
        Returns the Fibonacci number at position n"""
# returning 1 for the first two Fib numbers
    if n == 1 or n == 2:
        return 1
# storing the two previous Fib numbers as variables
    first, second = 1,1
    #start counting from the third position
    count = 3
# loop until we reach the desired position in n
    while count <= n:
        next_num = first + second # Calculate the next Fib number
        first = second  # Update first to be the previous second
        second = next_num   # second becomes the new number
        count = count + 1   # move to next position

#return the Fibonacci number at nth position
    return second

#term = fib(3)
#print(term)