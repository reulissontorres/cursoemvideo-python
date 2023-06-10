from math import radians, sin, cos, tan

angle = float(input('Enter the angle you desire: '))
sine = sin(radians(angle))
print('The angle of {} has a SINE of {:.2f}'.format(angle, sine))
cosine = cos(radians(angle))
print('The angle of {} has a COSINE of {:.2f}'.format(angle, cosine))
tangent = tan(radians(angle))
print('The angle of {} has a TANGENT of {:.2f}'.format(angle, tangent))
