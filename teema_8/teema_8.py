from turtle import color
import matplotlib.pyplot as plt

import numpy as np

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y, linestyle='--', marker='x', color='#63621b', markersize=8, label="Laskuv joon")
plt.title("Lihtne graafik")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.show()


plt.scatter(x, y, color="b", label="Punktidest diagramm")
plt.legend()
plt.show()

plt.bar(x, y, color="b", label="Tilpidiagramm")
plt.legend()
plt.show()

plt.hist(x, y, color="#97fcc7", label="Histogramm")
plt.show()



plt.pie(x, y,)
plt.show()




x=np.arange(-10,10,1) #"linspace(-10,10,100*viimane num on punktide arv*")
y=2*x**2-4*x+5
plt.figure(facecolor="yellow")
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("y=2*x**2-4*x+5")
plt.title("Graafik")
plt.grid()
plt.savefig("graafik.png")
plt.show()



#ÜL 8,1
x=np.arange(-12,12,1)
y=-1/18*x**2+12

x2=np.arange(-4,4,1)
y2=-1/8*x2**2+6

x3=np.arange(-12,-4,1)
y3=-1/8*(x3+8)**2+6

x4=np.arange(4,12,1)
y4=-1/8*((x4-8)**2)+6

x5=np.arange(-4,-0.3,0.1)
y5=2*((x5+3)**2)-9

x6=np.arange(-4,0.2,0.1)
y6=1.5*(x6+3)**2-10


plt.plot(x, y,  color='blue', marker='x',  markersize=8)
plt.plot(x2, y2, color="green", marker='x', markersize=8)
plt.plot(x3, y3, color="yellow", marker='x', markersize=8)
plt.plot(x4, y4, color="red", marker='x', markersize=8)
plt.plot(x5, y5, color="purple", marker='x', markersize=8)
plt.plot(x6, y6, color="purple", marker='x', markersize=8)
plt.plot(facecolor="yellow")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Vihmavari")
plt.show()
