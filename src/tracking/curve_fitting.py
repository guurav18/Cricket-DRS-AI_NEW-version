import numpy as np
import matplotlib.pyplot as plt

x = np.array([102,106,112,121])
y = np.array([58,67,92,97])

coeff = np.polyfit(x, y, 2)

curve = np.poly1d(coeff)

x_new = np.linspace(min(x), max(x) + 40, 200)
y_new = curve(x_new)

plt.scatter(x, y)
plt.plot(x_new, y_new)

plt.show()