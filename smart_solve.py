#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Run this Step first to run the functions
def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y


# In[ ]:


num1 = float(input('Enter a number to do the Math: '))

num2 = float(input('Enter another number to do the calculation: '))

choice = input('Enter a choice of calculations (A, S, M, D): ')

# you dont have to run this Step as iam trying to call the variables to make sure iam doing it right


# In[ ]:


#Step 2 

print("Enter 'A' for Addition")
print("Enter 'S' for Subtraction")
print("Enter 'M' for Multiplication")
print("Enter 'D' for Division")


choice = input('Enter a choice of calculations (A, S, M, D): ')

if choice.lower() in ('add','a', 'addition', 'ad','sub', 's' ,'subtract', 'subtraction', 'm', 'multiply', 'multiplication', 'd', 'division', 'divide', 'div'):
    num1 = float(input('Enter a number to do the Math: '))
    num2 = float(input('Enter another number to do the calculation: '))

    if choice.lower() in ('add','a', 'addition', 'ad'):
        print('Result:', num1, '+', num2, ':', add(num1,num2))
    elif choice.lower() in ('sub', 's' ,'subtract', 'subtraction'):
        print('Result:', num1, '-', num2, ':', subtraction(num1,num2))  
    elif choice.lower() in ('m', 'multiply', 'multiplication'):
        print('Result:', num1, '*', num2, ':', multiplication(num1,num2))    
    elif choice.lower() in ('d', 'division', 'divide', 'div'):
        print('Result:', num1, '/', num2, ':', division(num1,num2))
    
    
else:
    print('Please input the right calculation method')
    



# In[2]:


def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y


# In[4]:


print("Enter 'A' for Addition")
print("Enter 'S' for Subtraction")
print("Enter 'M' for Multiplication")
print("Enter 'D' for Division")

while True:
    choice = input('Enter a choice of calculations (A, S, M, D): ')

    if choice.lower() in ('add','a', 'addition', 'ad','sub', 's' ,'subtract', 'subtraction', 'm', 'multiply', 'multiplication', 'd', 'division', 'divide', 'div'):
        num1 = float(input('Enter a number to do the Math: '))
        num2 = float(input('Enter another number to do the calculation: '))

        if choice.lower() in ('add','a', 'addition', 'ad'):
            print('Result:', num1, '+', num2, ':', add(num1,num2))
        elif choice.lower() in ('sub', 's' ,'subtract', 'subtraction'):
            print('Result:', num1, '-', num2, ':', subtraction(num1,num2))  
        elif choice.lower() in ('m', 'multiply', 'multiplication'):
            print('Result:', num1, '*', num2, ':', multiplication(num1,num2))    
        elif choice.lower() in ('d', 'division', 'divide', 'div'):
            print('Result:', num1, '/', num2, ':', division(num1,num2))


    else:
        print('Please input the right calculation method')
        
    next_calculation = input('do you wanna do another calculation (y/n): ')
    if next_calculation.lower() in ('no', 'nah', 'nope', 'n'):
        print('Thanks for using Me!')
        break




# In[ ]:




