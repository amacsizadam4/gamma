# points inside circle / all points =? pi/4

import random
import math


N = 1000000
counter=0
for i in range(N):
    x = random.random()
    y = random.random()
    if x <= 1 and x >= 0 and y>=0 and y <= math.sqrt(1-x*x):
        #print(x,y)
        counter+=1

    
print(counter)
pi=4*counter/N
print(pi)