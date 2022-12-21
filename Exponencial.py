import numpy as np
import matplotlib.pyplot as plt

a = -60
b = 65
dt = 2    #Mejora o disminuye la señal.
#se conforma un numero complejo:
    #s = sigma + omegaj
sigma = 0  
omega = 1

t = np.arange(a, b, dt)

s = complex(sigma, omega)

senal = np.exp(s*t)

plt.figure(1)
#plt.plot(t, abs(np.real(senal)), label = 'real')
#plt.plot(t, np.imag(senal), label = 'imaginario')
plt.plot(t, np.imag(senal)/np.real(senal), label = 'tangente.')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.margins(0.01)
plt.grid(True)
plt.title('Funcion exponencial')
plt.show()                          #Muestra la funcion si se esta usando la terminal.

#Con sigma en 0 y omega en 1 se generan las funciones seno y coseno
#la parte real es el: COSENO.
#la parte imaginaria es el: SENO