import numpy as np

u = lambda t: np.piecewise(t, t>=0, [5,0])
#segundo parametro afecta al eje x.
#tercer parametro afecta el eje y +/-

a = -10
b = 10
dt = 0.1 #sirve para mejorar o disminuir la presicion en el eje X y Y

t = np.arange(-10, 10, 0.1)

u0 = u(t-0)
#afecta donde pasa de 0 a x en el eje Y

#grafica
import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(t, u0)

plt.title('Funcion 1')
plt.xlabel('t')
plt.ylabel('Escala u(t)')
plt.margins(dt)
plt.grid()
plt.show()