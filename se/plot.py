import matplotlib.pyplot as plt
import numpy as np

# x değer aralığı
x = np.linspace(-5, 5, 400)
y = x**2 - 2

plt.figure()

# Fonksiyonu çiz
plt.plot(x, y)

# Eksen isimleri
plt.xlabel("x")
plt.ylabel("y")

# Başlık
plt.title("f(x) = x² - 2")

# x ve y ölçeklerini eşitle
plt.gca().set_aspect('equal', adjustable='box')

# Izgara
plt.grid(True)

# Grafiği göster
plt.show()
