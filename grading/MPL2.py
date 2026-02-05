"""
Write a program that creates a bar char with 12 bars.
 The values on the Y axis should be random integer numbers with the range <0, 100>. On the X axis just numbers 1, 2, … 12.

Use matplotlib library.
"""

import matplotlib.pyplot as plt
import random

def create_bar_chart():
    x = list(range(1, 13)) 
    y = [random.randint(0, 100) for _ in range(12)] 

    plt.bar(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Bar Chart with Random Values')
    plt.xticks(x)  
    plt.ylim(0, 100)  
    plt.show()

if __name__ == "__main__":
    create_bar_chart()