#necessary libraries
import math
#using specific methods in this library for fun
from math import sin, cos, tan, pi

#gather user input and convert to integer
num = input('Please enter a number in degrees:\n')
num = float(num)

#converting to radians
num = math.radians(num)
print('This number in radians: \n ', num)

#outputting trig functions in radians
print('the cosine of the number you inputed is: \n', round(cos(num)))
print('the sine of the number you inputed is: \n', round(sin(num)))
print('the tangent of the number you inputed is: \n', round(tan(num)))

print('The quadrent this degree is in:\n')

#Deciding which quadrent the degree is in
if (num < pi/2 ):
    print('Qudrent 1')
elif (num < pi):
    print('Quadrent 2')
elif (num < (3/2)*pi):
    print('Quadrent 3')
else:
    print('Quadrent 4')


