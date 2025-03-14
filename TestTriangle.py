# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):

    # --------------------------- Valid Triangle Tests ---------------------------

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(5, 12, 13),'Right','5,12,13 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(13, 12, 5),'Right','13,12,5 is a Right triangle')

    def testEquilateralTriangle(self):  
        self.assertEqual(classifyTriangle(3, 3, 3),'Equilateral','3,3,3 should be equilateral')

    def testScalene(self):
        self.assertEqual(classifyTriangle(7, 8, 10), 'Scalene', '7 8 10 is a scalene triangle')

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(8, 9, 7), 'Scalene', '8 9 7 is a scalene triangle')

    def testScaleneC(self):
        self.assertEqual(classifyTriangle(10, 7, 9), 'Scalene', '10 7 9 is a scalene triangle')

    def testLargeTriangle(self):
        self.assertEqual(classifyTriangle(100, 150, 200), 'Scalene', '100 150 200 is a scalene triangle')

    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(5, 5, 8), "Isosceles", '5 5 8 is Isosceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isosceles', '8 5 5 is isosceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(5, 8, 5), 'Isosceles', '5 8 5 is isosceles')

    # --------------------------- Invalid Input Tests ---------------------------

    def testInvalidInputUpperBV(self):
        self.assertEqual(classifyTriangle(201, 150, 150), "InvalidInput", "Inputs are greater than 200.")

    def testInvalidInputLowerBV(self):
        self.assertEqual(classifyTriangle(0, 0, 0), "InvalidInput", "Value less than or equal to 0.")

    def testNonIntegerInputA(self):  # Renamed for clarity
        self.assertEqual(classifyTriangle(3.5, 4, 5), "InvalidInput", "a not int")

    def testNonIntegerInputB(self):  # Renamed for clarity
        self.assertEqual(classifyTriangle(3, "4", 5), "InvalidInput", "b is not int")

    def testInvalidInputString(self):
        self.assertEqual(classifyTriangle("a", "b", "c"), "InvalidInput", "Non-integer inputs")

    def testNegativeTriangle(self):
        self.assertEqual(classifyTriangle(-3, 4, 5), 'InvalidInput', 'Negative side length')

    # --------------------------- Not a Triangle Tests ---------------------------

    def testNotaTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', 'Sum of two sides less than third side')
    
    def testNotaTriangleB(self):
        self.assertEqual(classifyTriangle(1, 2, 3),'NotATriangle', "Sum of two sides equal third side")

    def testNotaTriangleC(self):
        self.assertEqual(classifyTriangle(5, 2, 3),'NotATriangle',"One side greater than sum of other two sides.")
        
    # --------------------------- Right Triangle Hypotenuse Tests ---------------------------

    def testRightBHypotenuse(self):
        self.assertEqual(classifyTriangle(6, 8, 10),'Right','B input is hypotenuse.')

    # --------------------------- Edge Cases and Miscellaneous Tests ---------------------------

    def testInstancesC(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', 'Standard 3, 4, 5 triangle')

    def testFloatInput(self):  # New test for floating-point inputs
        self.assertEqual(classifyTriangle(3.5, 4.5, 5.5), "InvalidInput", "Floating point values")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
