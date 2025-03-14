# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, return 'Right'
    """
    
    # verify that all 3 inputs are integers  
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # The sum of any two sides must be strictly greater than the third side for a valid triangle
    if not ((b + c > a) and (a + c > b) and (a + b > c)):
        return 'NotATriangle'

    # Now we know we have a valid triangle
    if a == b == c:  # All three sides are equal
        return 'Equilateral'

    # Check for right triangle using the Pythagorean theorem (order doesn't matter)
    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        return 'Right'

    # Check for isosceles triangle (two sides equal)
    if a == b or b == c or a == c:
        return 'Isosceles'

    # If it's not equilateral, isosceles, or right, it must be scalene (all sides different)
    return 'Scalene'
