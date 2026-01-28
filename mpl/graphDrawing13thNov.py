import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 10, 200)

y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x, y1, label="sin", color='red')
plt.plot(x, y2, label="cos", color='springgreen')

plt.axhline(0, color='hotpink', linewidth=0.8)
plt.axvline(0, color='green', linewidth=0.8)

plt.title("test Graph")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

plt.show()