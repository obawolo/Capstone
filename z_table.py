# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Graph of the standard normal distribution
x = []
y = []
i = -4
# x values
while i < 4:
    x.append(round(i,3))
    i += 0.01
    
    
# Constant for the formula
e = 2.71828182846
pi = 3.14159265359

# f(x) = (1 / sqrt(2pi)) * e^(-x^2/2)
c = 1 / ((2*pi)**.5)

# y values 
for a in x:
    #exponent(x) part
    exp = (-a**2)/2
    #the forumla
    f = c*(e**exp)
    y.append(f)

"""
import matplotlib.pyplot as plt
plt.plot(x,y)
#plt.show
"""

# calculating area of the curve, integration module
import scipy.integrate

# setting lower limit to negative infinite
neg_inf = -float('inf')

# f(x) = (1 / sqrt(2pi)) * e^(-x^2/2)
def f(x):
    expo = (-x**2)/2
    standard_normal_curve = c*(e**expo)
    return standard_normal_curve

z_table = []

for row in x:
        probability, error = scipy.integrate.quad(f, neg_inf, row)
        z_table.append([row, round(probability,5)])
        #print(row, round(probability,5))

# returns the probability of the z_score
# z_table row index = (z_score + 4)  * 100
def z_score_probability(z_score):
    row_index = int((z_score + 4) * 100)
    z_row = z_table[row_index]
    z_prob = z_row[1]
    return z_prob
#print (z_score_probability(2))

# conversion from x sample value to z_score
# z = (x-u)/s_d
def x_to_z(mean, standard_deviation, sample_input):
    z_score = (sample_input - mean) / standard_deviation
    return z_score
#print(x_to_z(50, 10, 30))

# conversion from z score to x value
# x = u + (z*s_d)
def z_to_x(mean, standard_deviation, z_score):
    x_value = mean + (z_score*standard_deviation)
    return x_value


z1 = x_to_z(74, 8, 98)
z2 = x_to_z(74, 8, 82)
z1p = z_score_probability(-3)
z2p = z_score_probability(3)
z = 1 - z1p
print(z)

#print(z_table)

"""
import csv
with open('z_table.csv', 'w', newline='') as zTableFile:
    z_table_writer = csv.writer(zTableFile,delimiter=',')
    for row in z_table:
        z_table_writer.writerow(row)
"""



    
