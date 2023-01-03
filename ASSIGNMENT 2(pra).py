#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Que.1
print("we convert kilometers to miles")
a=float(input("Enter kilometers: "))
b=a*0.621
print("Miles: ",b)


# In[ ]:


#Que.2
print("we convert Celsius to Fahrenheit")
x=float(input("Enter Celsius: "))
y=((x*9)/5)+32
print("Fahrenheit: ",y)


# In[7]:


#Que.3
import calendar
yy=2023
mm=1
print(calendar.month(yy,mm))


# In[5]:


#Que.4
import cmath
print("Quadratic equation is ax2 + bx +c = 0")
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
d=(b**2)-(4*a*c)
sol1 = (-b + cmath.sqrt(d))/(2*a)
sol2 = (-b - cmath.sqrt(d))/(2*a)
print(f"solutins are: {sol1} , {sol2}")


# In[6]:


#Que.5

a=10
b=20

a=a+b
b=a-b
a=a-b

print("a:",a)
print("b:",b)


# In[ ]:




