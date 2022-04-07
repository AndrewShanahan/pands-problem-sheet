# Author: Andrew Shanahan
# Task: Write a program that reads in a text file and outputs the number of e's it contains.
# Reference 1: https://www.w3schools.com/python/python_file_handling.asp
# Reference 2: https://www.w3schools.com/python/python_file_open.asp
# Reference 3: https://www.w3schools.com/python/python_file_write.asp
# Reference 4: datacamp.com (a number of tutorials reviewed), youtube.com (numberous videos watched)

def letterCounter(contents, alphabet):
    counter = 0
    for letter in contents:
        if alphabet is letter:
            counter += 1
    return counter
e_counter = 0
