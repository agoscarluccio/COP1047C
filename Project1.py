# -*- coding: utf-8 -*-
"""
Income Tax Calculator
Author: Agostina Carluccio
COP1047C

Request
The customer requests a program that computes a person’s income tax.

Analysis
Analysis often requires the programmer to learn some things about the problem domain, 
in this case, the relevant tax law. For the sake of simplicity, let’s assume 
the following tax laws:

All taxpayers are charged a flat tax rate of 20%
All taxpayers are allowed a $10,000 standard deduction
For each dependent, a taxpayer is allowed an additional $3,000 deduction
Gross income must be entered to the nearest penny
The income tax is expressed as a decimal number
"""

taxRate = 0.20
standardDeduction = 10000
dependentDeduction = 3000

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))


incomeTax = (grossIncome - standardDeduction - 
             (dependentDeduction * numDependents)) * taxRate
print("The income tax is $", incomeTax)

