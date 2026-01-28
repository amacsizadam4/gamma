import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 400)
y = x**2 - 2

plt.figure()

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")

plt.title("f(x) = x² - 2")

plt.gca().set_aspect('equal', adjustable='box')

plt.grid(True)

plt.show()
