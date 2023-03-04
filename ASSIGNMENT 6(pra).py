#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Que.1 Write a Python Program to Display Fibonacci Sequence Using Recursion?
def rec_fibo(n):
    if n <= 1:
        return n
    else:
        return(rec_fibo(n-1) + rec_fibo(n-2))
nterms = 20
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(rec_fibo(i))


# In[8]:


# Que.2 Write a Python Program to Find Factorial of Number Using Recursion?
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
num = 3
if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# In[9]:


# Que.3 Write a Python Program to calculate your Body Mass Index?
height = float(input("your height in Feet: "))
weight = float(input("your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))


# In[11]:


# Que.4 Write a Python Program to calculate the natural logarithm of any number?
import math
n = int(input("Enter the number: "))
a = math.log(n)
print("The value is:",a)


# In[13]:


# Que.5 Write a Python Program for cube sum of first n natural numbers?
def sum_cubes(n) :
    if n < 0:
        return
    sum = 0
    for i in range(n+1):
        sum += pow(i, 3)
    return sum

n = int(input('Enter n : '))
sum = sum_cubes(n)
print(f'Sum : {sum}')


# In[ ]:




