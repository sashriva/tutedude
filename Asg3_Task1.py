def factorial(num):
    if num <=1:
        return 1
    else:
        return num*factorial(num-1)

i = int(input("Enter a number: "))

print("Factorial of number ",i," is",factorial(i))
