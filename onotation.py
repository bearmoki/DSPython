# mu  theta omni - 

# O(n) example:
# ran passed in a variable 
# and it ran n times (number of operations)
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

# drop constants - O(n^2)
# doesn't matter how many times
# it ran n times, it is still O(n) here because of drop constants

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
            # n * n = n^2
#  this is very inefficient from a time complexity standpoint

# Drop non-dominants

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)

    # O(n^2) + n -> O(n^2 + n) --> 
    # that stand alone n is small amount in that equation - as operation for n^2 increases - n takes a smaller portion
    # dominant - O(n^2) - so n gets dropped --> and we only have O(n^2)

def add_items(n):
    return n + n
    # if O(1) -> there is only ONE operation.
    # O(1) is constant time


# O(log n)
# can cut how long it takes to find an element by the power--> if it takes you three steps - log2(8) = 3 
# 1 2 3 4 5 6 7 8

# o(n log n) -> used with some sorting alogrithms (most efficient)
# when sorting strings, most efficient

# least efficient - O(n^2)
# O(n)
# O( log n) 
# O(1)


# Different Terms for Inputs -- used as a gotcha question in interviews
def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

        # can't say these two for loops are O(n) -> O(n) + O(n) --> O(n)
        # can't do this with function with two different parameters
        # this is instead: O(a) + O(b) --> O(a + b)

# Similarly, if we have nested for loops
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

        # this would instead be O(a * b)


 
# O(n^2) - Loop within a loop
# O(n) proportional
# O(log n) - divide and conquer
# O(1) - constant