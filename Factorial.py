#Factorials
def getFactorial(n):
    if(n == 0 ):
        return 1
    else:
        return n * getFactorial(n-1)

print('Factorial for 0 -', getFactorial(0))
print('Factorial for 1 -', getFactorial(1))
print('Factorial for 2 -', getFactorial(2))
print('Factorial for 3 -', getFactorial(3))
print('Factorial for 30 -', getFactorial(30))