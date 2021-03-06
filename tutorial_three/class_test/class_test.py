#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:27:30 2018
Here I test how working with classes works in Python.
@author: victor
"""

#Define an example class
class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
        
    def area(self):
        return self.x *self.y

    def perimeter(self):
        return 2*self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale 
        self.y = self.y * scale

rectangle = Shape(100,45)
print rectangle.area()
print rectangle.perimeter()
#describing the rectangle
rectangle.describe("A wide rectangle, more than twice\
 as wide as it is tall")

#making the rectangle 50% smaller
rectangle.scaleSize(0.5)

#re-printing the new area of the rectangle
print rectangle.area()
