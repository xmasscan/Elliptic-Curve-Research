#
#   Finding Rational Points on Elliptic Curves
#   MATH 496 : Independent Study @ UIC
#   Author: Michael Hanif Khan 
#   
#   This program takes coefficients a1 -> a6 and two points.
#   Based on these inputs, whether or not the curve is ellpitic is checked and addition is performed.

import fractions as frac

########################
#
#   calculate_determinant(a1,a2,a3,a4,a5,a6)
#   a1 ... a6 : Fraction Objects
#   
#   calculates weights b2,b4,b6, and b8.
#   uses weights to calculate the determinant
#
########################

# Weierstrass Equations for algerbraically describing Elliptic Curve Addition
# See Silverman's "The Arithmetic of Elliptic Curves" Page 42

# a is an array of the coefficients which are labeled as "a_i" where i is the index starting from 1.
# for clarity, indicies will be written as their 1-indexed index minus one. :)
# every element in a is a fraction.

# a = List of Weierstrass Weights input in the order:
# a_1, a_3, a_2, a_4, a_6
# Therefore:
# a_1 = a[0]
# a_3 = a[1]
# a_2 = a[2]
# a_4 = a[3]
# a_6 = a[4]

def calculate_determinant(a):
    # assuming a is an array of integers where as are passsed in order specified here:
    # a_1, a_3, a_2, a_4, a_6

    b2 = pow(a[0],2) + 4 * a[2]
    b4 = 2 * a[3] + a[0] * a[1]
    b6 = pow(a[1],2) + 4 * a[4]
    b8 = pow(a[0],2) * a[4] + 4 * a[2] * a[4] - a[0] * a[1] * a[3] + a[2] * pow(a[1],2)

    return -pow(b2,2) * b8 - 8 * pow(b4,3) - 27 * pow(b6,2) + 9 * b2 * b4 * b6

# See Silverman's "The Arithmetic of Elliptic Curves" Page 54
# lambda is a Python built in, so we will call it "l".

# a_1 = a[0]
# a_3 = a[1]
# a_2 = a[2]
# a_4 = a[3]
# a_6 = a[4]
def add_points(a, x1: frac.Fraction, y1: frac.Fraction, x2: frac.Fraction, y2: frac.Fraction):
    if x1 == x2:
        l_num = 3 * pow(x1,2) + 2 * a[2] * x1 + a[3] - a[0] * y1
        l_denom = 2 * y1 + a[0] * x1 + a[1]
        l = frac.Fraction(l_num,l_denom)

        v_num = -1 * pow(x1,3) + a[3] * x1 + 2 * a[4] - a[1] * y1
        v_denom = 2 * y1 + a[0] * x1 + a[1]
        v = frac.Fraction(v_num, v_denom)
    else:
        l_num = y2 - y1
        l_denom = x2 - x1
        l = frac.Fraction(l_num,l_denom)

        v_num = y1 * x2 - y2 * x1
        v_denom = x2 - x1
        v = frac.Fraction(v_num, v_denom)

    x3 = pow(l,2) + a[0] * l - a[2] - x1 - x2
    y3 = -(l + a[0]) * x3 - v - a[1]
    point = [x3,y3]
    return point

# Add a point to itself.
#
def check_order(a, x: frac.Fraction, y: frac.Fraction):
    point = [x,y]

    # Add point to itself 16 times OR until point == [0,0] i.e. "Point at Infinity"
    for i in range(0,16):
        try:
            point = add_points(a,point[0],point[1],x,y)
        except Exception as e:
            return i
    
    # If code is still running, loop terminated without returning.
    # Therfore, Order of point is not <= 16 and thusly must be infinite.
    return -1
