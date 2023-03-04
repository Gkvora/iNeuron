#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Que1. Write a Python Program to Add Two Matrices?
X = [[1,7,8],
    [4 ,7,6],
    [7 ,3,8]]

Y = [[9,3,1],
    [6,3,0],
    [0,0,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)


# In[4]:


# Que2.Write a Python Program to Multiply Two Matrices?
X = [[2,7,3],
    [4 ,8,6],
    [7 ,0,9]]

Y = [[0,8,1,8],
    [0,7,8,0],
    [4,9,9,1]]

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
    print(r)


# In[6]:


# Que3.Write a Python Program to Transpose a Matrix?
X = [[2,9],
    [2 ,7],
    [1 ,2]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)


# In[7]:


# Que4.Write a Python Program to Sort Words in Alphabetic Order?
my_str = "Hello Example With cased letters"
words = [word.lower() for word in my_str.split()]
words.sort()

print("sorted words are:")
for word in words:
    print(word)


# In[8]:


# Que5.Write a Python Program to Remove Punctuation From a String?
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)


# In[ ]:




