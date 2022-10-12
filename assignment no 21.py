#!/usr/bin/env python
# coding: utf-8

# # Assignment 21 Solutions

# 1.Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.

# In[1]:


def next_in_line(in_list,in_num):
    if len(in_list) > 1:
        in_list.append(in_num)
        in_list.remove(in_list[0])
        print(f'output --> {in_list}')
next_in_line([5,6,7,8,9],1)
next_in_line([7,6,3,23,17],10)
next_in_line([1,10,20,42],6)
next_in_line([],6)

# 2.Create the function that takes a list of dictionaries and returns the sum of people's budgets.
# In[2]:


def get_budget(in_dict):
    sum = 0
    for i in in_dict:
        sum+= i["budget"]
    print(f'output --> {sum}')
    
get_budget([
    {"name":"john","age":21,"budget":23000},
    {"name":"steve","age":32,"budget":40000},
    {"name":"Martin","age":16,"budget":2700}
    
])

get_budget([
    {"name":"john","age":21,"budget":29000},
    {"name":"steve","age":32,"budget":32000},
    {"name":"Martin","age":16,"budget":1600}
])


# 3.Create a function that takes a string and returns a string with its letters in alphabetical order.

# In[3]:


def alphabet_soup(in_string):
    out_string = ''.join(sorted(in_string))
    print(f'{in_string}-->{out_string}')
    
alphabet_soup("hello")
alphabet_soup("edabit")
alphabet_soup("hacker")
alphabet_soup("geek")
alphabet_soup("javascript")


# 4.What will be the value of your investment at the end of the 10 year period?

# In[5]:


def compound_intrest(principal,year,roi,cp):
    ci = principal*(1+(roi/cp)**(cp*year))
    print(f'output --> {ci:.2f}')
    
compound_intrest(100,1,0.05,1)
compound_intrest(3500,15,0.1,4)
compound_intrest(100000,20,0.15,365)


# 5.Write a function that takes a list of elements and returns only the integers.

# In[6]:


def return_only_int(in_list):
    out_list = []
    for i in in_list:
        if type(i) == int:
            out_list.append(i)
    print(f'{in_list}-->{out_list}')
    
return_only_int([9,2,"space","car","lion",16])
return_only_int({"hello",81,"basketball",123,"fox"})


# In[ ]:




