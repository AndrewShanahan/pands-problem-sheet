# Write a program that asks a user to input a string and outputs every second letter in reverse order
# Task: enter a sentence "The quick fox jumps over the lazy dog".
# python secondstring.py
message = " The quick brown fox jumps over the lazy dog. "
print (message)
print (message.strip ())
print (message[::2][::-1])