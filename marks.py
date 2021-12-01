# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:24:16 2021

@author: sunil
"""

m1 = int(input("Enter the marks of Hindi :"))
m2 = int(input("Enter the marks of English :"))
m3 = int(input("Enter the marks of Maths :"))
m3 = int(input("Enter the marks of Physics :"))
m4 = int(input("Enter the marks of Chemistry :"))
m5 = int(input("Enter the marks of Computer :"))
if (m1 or m2 or m3 or m4 or m5)>=75:
    print("Student is passed with distinction marks in one or more subjects")
else:
    print("Student is passed in the examination")