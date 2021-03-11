#Steven Cen w/ William Vongphanith
#IntroCS pd6 sec10
#HW08
#2021-03-05

#imports the python math library for 'math.pi'
import math as Math

#area_circ(r) takes numeric input r and returns the area of a circle of radius r.

def area_circ(r):
    return Math.pi * r ** 2

#area_washer(radInner,radOuter) takes numeric inputs
#radOuter, radInnerand returns the area of a washer with
#inner radius radInner and outer radius radOuter.

def area_washer(radInner,radOuter):
    return area_circ(radOuter) - area_circ(radInner)
    
#sum_of_squares(a,b) takes numeric inputs a, b
#and returns the sum of their squares.

def sum_of_squares(a,b):
    return a ** 2 + b ** 2

'''
this is a block comment

function executions below
'''

print(area_circ(1))
print("area_circ(1) should be 3.14159265359\n")

print(area_circ(3))
print("area_circ(3) should be 28.2743338823\n")

print(area_circ(5))
print("area_circ(5) should be 78.5398163397\n")

print(area_washer(0,2))
print("area_washer(0,2) should be 12.5663706144\n")

print(area_washer(3,5))
print("area_washer(3,5) should be 50.2654824574\n")

print(area_washer(6,10))
print("area_washer(6,10) should be 201.06192983\n")

print(sum_of_squares(0,0))
print("sum_of_squares(0,0) should be 0")

print(sum_of_squares(1,2))
print("sum_of_squares(1,2) should be 5")

print(sum_of_squares(4,5))
print("sum_of_squares(4,5) should be 41")