#factorial
def rfactorial(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*rfactorial(n-1))
a=int(input("Enter a number : "))
if a<0:
    print("Enter a postive number")
else:
    print("Factorial of the number is :",rfactorial(a))
#fibonacci series
def rfib(n):
    if n<=1:
        return n
    else:
        return(rfib(n-1)+rfib(n-2))
a=int(input("Enter the number of terms : "))
if a<=0:
    print("Enter a postive number : ")
else:
    print("Fibonacci series : ")
    for i in range(a):
        print(rfib(i))
#gcd
import math
def rgcd(a, b):
    if b == 0:
        return a
    else:
        return rgcd(b, a % b)
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
if a < 0 or b < 0:
    print("Please enter non-negative numbers.")
else:
    print("GCD of the given numbers is:", rgcd(a, b))
#lambda function returns even or odd
cutie=lambda x:x%2
n=int(input("Enter a number : "))
if cutie(n)==0:
    print("Even number")
else:
    print("Odd number")
