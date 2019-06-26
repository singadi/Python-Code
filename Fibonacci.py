#Fibonacci number sequence
def getFibonacci(n):
    if(n == 0):
        return 0
    else:
        if(n == 1):
            return 1
        else:
            if(n > 1):
                return getFibonacci(n-1) + getFibonacci(n-2)


print('Fibonacci for 0 -', getFibonacci(0))
print('Fibonacci for 1 -', getFibonacci(1))
print('Fibonacci for 2 -', getFibonacci(2))
print('Fibonacci for 3 -', getFibonacci(3))
print('Fibonacci for 30 -', getFibonacci(30))
