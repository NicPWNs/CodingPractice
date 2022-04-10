#!/usr/bin/env python3
'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

maxNum = int(input())
list = []

for x in range(1,maxNum):
    if x % 2 == 1:
        list.append(x)


print(list)