def write_hello(name):
    """Print Hello"""
    print("Congradulation " + name + " wish you the best!")

def summa(x,y):
    return x+y

def aaa():
    print("aaa")

def factorial(x):
    """Calculate Factorial of number X"""
    result = 1
    for i in range(1, x+1):
        result = result * i
    return result

print(factorial(4))
print(factorial(120))

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

print("--------------------")
write_hello("Alexey")
write_hello("Vasya")
aaa()

x = summa(33,22)
print(x)


