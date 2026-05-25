# 4. Function Returning multiple Values 
# Problem : Create a function that returns both the area 
# and circumference of a circle given its radius 

import math
def circle_stats(radius):
    area =  round(math.pi * radius ** 2)
    circumference = round(2 * math.pi * radius)
    return area , circumference

print(circle_stats(3))