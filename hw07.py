'''
William Vongphanith
IntroCS pd6 sec10
HW07 - Now for something completely different...
2021-03-03
'''

import math as Math
'''
Are libraries allowed?
'''

'''
# Function A - add together two numbers
'''
def a(inp1,inp2):
    return inp1 + inp2

'''
# Function B - divide the second arg by first, third by second, and the first and second results.
# Basically inp1 * inp3 / inp2 ** 2
'''
def b(inp1,inp2,inp3):
    var1 = inp2 / inp1
    var2 = inp3 / inp2
    var3 = var2 / var1
    return var3

'''
# Function C - a mess.
# var1 gets inp2 to the inp1th power
# var2 gets inp3 to the inp2th root
# Then we find the remainder of var2 over var1
'''
def c(inp1,inp2,inp3):
    var1 = inp2 ** inp1
    var2 = inp3 ** (1 / inp2)
    var3 = var2 % var1
    return var3

'''
A bonus, this will make your head wobble and spin like a top.
Makes a list
Puts the three inputs into a list (for efficiency)
var1 = the three inputs multiplied together
For each input, we perform a variety of operations using var1
    First, we multiply var1 by the input
    Then we divide var1 by the input and are left with just
    the whole number part
    After we get the remainder of var1 divided with input
After we put them all into a list, get the ones that are even, and then add them together and return them.

'''
def d(inp1,inp2,inp3):
    list1 = []
    inputs = [inp1,inp2,inp3]
    var1 = inp1 * inp2 * inp3
    for item in inputs:
        list1.append(Math.floor(var1 * item))
        list1.append(Math.floor(var1 // item))
        list1.append(Math.floor(var1 % item))
    newlist = [item for item in list1 if int(item) % 2 == 0]
    newvar = 0
    for item in newlist:
        newvar += int(item)
    return newvar

'''
Test runs
'''
print("a(2,3)")
print(a(2,3))
print("=> should return 5\n")
print("b(5,5,10)")
print(b(5,5,10))
print("=> should return 2.0\n")
print("c(5,6,7)")
print(c(5,6,7))
print("=> should return 1.3830875542684884\n")
print("d(3,5,6)")
print(d(3,5,6))
print("=> should return 1308\n")
