#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Que1.Write a Python program to find sum of elements in list?
a=[2,3,5,6,7,9]
sum=0
for i in a:
    sum+=i
print(sum)


# In[5]:


# Que2.Write a Python program to Multiply all numbers in the list?
a=[2,3,5,4]
mul=1
for i in a:
    mul*=i
print(mul)


# In[25]:


# Que3.Write a Python program to find smallest number in a list?
a=[1,2,3,5,6,7,9,0,-1,6666,-45677,90990]
a.sort()
a[0]


# In[26]:


# Que4.Write a Python program to find largest number in a list?
a=[1,2,3,5,6,7,9,0,-1,6666,-45677,90990]
a.sort()
a[-1]


# In[27]:


# Que5.Write a Python program to find second largest number in a list?
a=[1,2,3,5,6,7,9,0,-1,6666,-45677,90990]
a.sort()
a[-2]


# In[31]:


# Que6 Write a Python program to find N largest elements from a list?
def Nmaxelements(list1, N):
    final_list = []
    for i in range(0, N):
        max1 = 0
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];
        list1.remove(max1);
        final_list.append(max1)

    print(final_list)

list1 = [23, 67, 41, 895, 60, 83, 67, 96, 190]
N = 3
Nmaxelements(list1, N)


# In[32]:


# Que.7 Write a Python program to print even numbers in a list?
a=[23, 67, 41, 895, 60, 83, 67, 96, 190]
for i in a:
    if i%2==0:
        print(i)


# In[33]:


# Que.8 Write a Python program to print odd numbers in a List?
a=[23, 67, 41, 895, 60, 83, 67, 96, 190]
for i in a:
    if i%2!=0:
        print(i)


# In[40]:


# Que.9 Write a Python program to Remove empty List from List?
a= [5, 6, [], 3, [], [], 9,99,10]
b=[i for i in a if i!=[] ]
b


# In[41]:


# Que.10 Write a Python program to Cloning or Copying a list?
def Cloning(li1):
    li_copy = li1[:]
    return li_copy
li1 = [44, 86, 2, 17, 185, 1]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# In[43]:


# Que.11 Write a Python program to Count occurrences of an element in a list?
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

lst = [1, 6, 1, 10, 1, 20, 10, 1, 11]
x = 1
print('{} has occurred {} times'.format(x,countX(lst, x)))


# In[ ]:




