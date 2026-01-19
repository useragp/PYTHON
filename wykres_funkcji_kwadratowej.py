from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

print("Rónanie kwadratowe : ax^2 +bx + c = 0")
a = 2
b = -5
c = -4

delta = (b**2) - (4 * a * c)

if delta > 0:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)

elif delta == 0:
    x0 = -b / (2*a)

else:
    print("brak miejsc zeroych")
p = int(-b / (2* a))

x = np.linspace(p-5,p+5 , 100) #np.linspace(start, stop, num)
y = (a*x**2 + b*x + c)
plt.grid()
plt.plot(x, y)
plt.show()



