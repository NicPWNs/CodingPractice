#!/usr/bin/env python3
'''
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''

heroes=['spider man','thor','hulk','iron man','captain america']

print("1. Length of the list")
print(len(heroes))

print("2. Add 'black panther' at the end of this list")
heroes.append("black panther")
print(heroes)

print("3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'")
heroes.remove("black panther")
heroes.insert(3, "black panther")
print(heroes)

print("4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.")
heroes[1:3] = ["doctor strange"]
print(heroes)

print("5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)")
heroes.sort()
print(heroes)