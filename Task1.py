def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
a = 5

result = factorial(a)

print("The factorial of 5 is: ",result)