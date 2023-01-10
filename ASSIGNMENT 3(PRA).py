#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
A=float(input("Enter Your Number: "))
if A>0:
    print(A,"is positive")
elif A<0:
    print(A,"is negative")
else:
   print(A,"is Zero")

#2. Write a Python Program to Check if a Number is Odd or Even?
B=float(input("Enter Your Number: "))
if B%2==0:
    print(B,"is Even")
else:
    print(B,"is odd")

#3. Write a Python Program to Check Leap Year?
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

#4. Write a Python Program to Check Prime Number?

N = int(input("Enter a number: "))
flag = False
if N == 1:
    print(N, "is not a prime number")
elif N > 1:
    for i in range(2, N):
        if (N % i) == 0:
            flag = True
            break
    if flag:
        print(N, "is not a prime number")
    else:
        print(N, "is a prime number")

# 5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
