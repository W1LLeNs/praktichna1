import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
y1 = x**2
y2 = x**3
plt.figure(figsize=(8,5))
plt.plot(x, y1, color='blue', label='y=x^2')
plt.plot(x, y2, color='red', label='y=x^3')

plt.title('Графіки функцій y=x^2 & y=x^3')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')

plt.legend()
plt.grid(True)

plt.show()


#---------------------------------

rand_data = np.random.randn(1000)

plt.figure(figsize=(8,5))

plt.hist(rand_data, bins=30, color='green', edgecolor='black')
plt.title('Гістограма випадкових значень')

plt.show()