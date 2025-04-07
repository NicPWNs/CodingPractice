#!/usr/bin/env python3
# Author: Nic Jones (NicPWNs)
# rot-cipher.py

textIn = str(input("\nEnter your text to rotate: "))
rotNum = int(input("Enter rotation (ROT) cipher key [13]: ") or "13")
textOut = ""

for i in range(len(textIn)):
    char = textIn[i]

    if char.isupper():
        textOut += chr((ord(char) + rotNum - 65) % 26 + ord("A"))

    elif char.islower():
        textOut += chr((ord(char) + rotNum - 97) % 26 + ord("a"))

    else:
        textOut += char

print("\n.....Processing.....\n")
print("[✅] Rotated text is: " + textOut)
print("[🔑] Used key: " + str(rotNum))
print("[❗] Note: Special characters are not rotated.\n")
