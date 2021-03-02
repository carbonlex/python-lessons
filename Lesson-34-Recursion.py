### Hello n times ###
def hello(x):
    if x == 0:
        return
    else:
        print("Hello!")
        hello(x-1)

hello(0)


### Summa for example 5=0+1+2+3+4+5 ###

def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)

z = sum(10)
print(z)

### Factorial ###

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(2))

### Fibonacci ###

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(40))

