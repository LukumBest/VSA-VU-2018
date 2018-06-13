# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.


#for num in a:
    #if num < 5:
        #print num


#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

#for number in c:
    #if number in b:
        #print number


#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.

#for letter in d:
    #if letter == "a":
        #print "*"
    #else:
        #print letter


#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

loop = 1
x = 0

u_str = raw_input("Enter a word and I will tell you if it is a palindrome.")
if len(u_str)%2 == 0:
    while x < (len(u_str) / 2) and loop == 1:
       if u_str[x] == u_str[-x + -1]:
           x = x + 1
       else:
           loop = loop + 1
else:
    while x < ((len(u_str) -1) / 2) and loop == 0:
        if u_str[x] == u_str[-x + -1]:
            x = x + 1
            loop = loop + 1
if loop == 0:
    print "It's a palindrome,"
elif loop == 1:
    print "It's not a palindrome."