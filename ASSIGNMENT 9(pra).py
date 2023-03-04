#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Que.1 Write a Python program to check if the given number is a Disarium Number?
def calculateLength(n):    
    len = 0  
    while(n != 0):    
        len = len + 1
        n = n // 10
    return len
   
num = int(input("Enter a number: "))    
digit = sum = 0 
len = calculateLength(num); 
temp = num    
while(temp > 0):    
    digit = temp % 10    
    sum = sum + int(digit ** len)
    temp = temp // 10    
    len = len - 1      
if sum == num :    
    print(num, "is a Disarium Number!!!")    
else:    
    print(num, "is not a Disarium Number!!!")


# In[16]:


# Que.2 Write a Python program to print all disarium numbers between 1 to 100?
def length_calculation(my_val):
    len_val = 0
    while(my_val != 0):
        len_val = len_val + 1
        my_val = my_val//10
    return len_val
def digit_sum(my_num):
    remaining = sum_val = 0
    len_fun = length_calculation(my_num)
    while(my_num > 0):
        remaining = my_num%10
        sum_val = sum_val + (remaining**len_fun)
        my_num = my_num//10
        len_fun = len_fun - 1
    return sum_val
ini_result = 0
print("The disarium numbers between 1 and 100 are : ")
for i in range(1, 101):
    ini_result = digit_sum(i)
    if(ini_result == i):
       print(i)


# In[22]:


# Que.3 Write a Python program to check if the given number is Happy Number?   
def isHappyNumber(num):    
    rem = sum = 0;     
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num = 68;    
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);    
if(result == 1):    
        print(str(num) + " is a happy number");    
    
elif(result == 4):    
    print(str(num) + " is not a happy number"); 


# In[23]:


# Que.4 Write a Python program to print all happy numbers between 1 and 100?  
    def isHappyNumber(num):    
    rem = sum = 0;    
          
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
  
print("List of happy numbers between 1 and 100: ");    
for i in range(1, 101):    
    result = i;    

    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    

    if(result == 1):    
        print(i)   
        print(" ")   


# In[27]:


# Que.5 Write a Python program to determine whether the given number is a Harshad Number?
num = 156  
rem = sum = 0;        
n = num;     
while(num > 0):    
    rem = num%10    
    sum = sum + rem    
    num = num//10;    
  
if(n%sum == 0):    
    print(str(n) + " is a harshad number")    
else:    
    print(str(n) + " is not a harshad number")  


# In[28]:


# Que.6 Write a Python program to print all pronic numbers between 1 and 100?
def isPronicNumber(num):    
    flag = False           
    for j in range(1, num+1):     
        if((j*(j+1)) == num):    
            flag = True;    
            break    
    return flag    
print("Pronic numbers between 1 and 100: ")    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i)    
        print(" ") 


# In[ ]:




