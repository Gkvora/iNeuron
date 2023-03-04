#!/usr/bin/env python
# coding: utf-8

# In[28]:


# que1. Write a Python Program to find sum of array?
import array as ar
def SumofArray(arr):
    sum=0
    n = len(arr)
    for i in range(n):
        sum = sum + arr[i]
    return sum 
a = ar.array('i',[1, 27, 2, 7])
print ('Sum of the array is ', SumofArray(a) ) 


# In[29]:


# que2.Write a Python Program to find largest element in an array?
import array as arr
a = arr.array('i',[34, 24, 11, 2])
print (' Greatest element in the array: ', max(a) ) 


# In[30]:


# que3.Write a Python Program for array rotation?
def rotateArray(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a

arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))


# In[31]:


# que4.Write a Python Program to Split the array and add the first part to the end?
def SplitArray(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n-1] = x
arr = [65, 70, 15, 86, 60, 76]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')


# In[32]:


# que5.Write a Python Program to check if given array is Monotonic?
def ismonotone(a):
    n=len(a) 
    if n==1:
        return True
    else:
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

A = [6, 5, 4, 1]
print(ismonotone(A))
b = [4, 6, 9, 0]
print(ismonotone(b))
c=[4,36,28]
print(ismonotone(c))
d=[3]
print(ismonotone(d))


# In[ ]:





# In[ ]:




