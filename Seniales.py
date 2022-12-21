import numpy as np
import matplotlib.pyplot as plt

def grafica(x, y, label, dt, num, label_legend):
    plt.figure(num)
    plt.plot(x, y, label = label_legend)
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.margins(dt)
    plt.grid()
    plt.title(label)

def EscalonUnitario(a, b, d, l, dt): #d desplazamiento, l amplitud.
    t = np.arange(a, b, dt)
    u = lambda t: np.piecewise(t, t>=0, [l,0])
    u0 = u(t-d)
    grafica(t, u0, "Escalon Unitario", dt, 1, "")

def Exponencial(a, b, dt, sigma, omega):
    t = np.arange(a, b, dt)
    s = complex(sigma, omega)
    senal = np.exp(s*t)
    grafica(t, abs(np.real(senal)), 'Funcion exponencial', dt, 2, "Real")
    grafica(t, np.imag(senal), 'Funcion exponencial', dt, 2, "Imaginaria")
    
def ExponencialCausal(a, b, dt, sigma, omega):
    t = np.arange(a, b, dt)
    s = complex(sigma, omega)
    senal =np.exp(s*t)
    u = lambda t: np.piecewise(t, t>=0, [1,0])
    u0 = u(t-0)
    senal = senal * u0
    grafica(t, np.real(senal), 'Funcion exponencial causal', dt, 3, "Real")
    grafica(t, np.imag(senal), 'Funcion exponencial causal', dt, 3, "Imaginaria")

def rectangular(a, b, t1, t2, lR, dt):
    t = np.arange(a, b, dt)
    u = lambda t: np.piecewise(t, t>=0, [lR,0])
    u0 = u(t-t1)
    u1 = u(t-t2)
    rectangular = u0 - u1
    grafica(t, rectangular, "Funcion rectangular", dt, 4, "")
    
def Impuslo(a, b, des, amp, dt):
    t = np.arange(a, b, dt)
    n = len(t)
    u = np.zeros(n)
    origen_indice = 0
    for i in range(0, n):
        if np.sign(t[i]) != np.sign(t[i-1]):
            origen_indice = i
        #sign(x) depende del parametro, -1 si x<0, 0 si x=0 1 si x>1
    u[origen_indice + des*10] = amp
    grafica(t, u, "Funcion impulso", dt, 5, "")

#main
print("Paremtros generales.")
a = float(input('Ingrese el limite inferior (eje X): '))
b = float(input('Ingrese el limite superior (eje X): '))
dt = float(input('Ingrese el paso (intervalo entre cada punto de los limites): '))

#-------------------------------------------------
#Modificaciones para las señales.
#-------------------------------------------------
#parametros de la escalon unitario.
print("------------------------- ESCALON UNITARIO.")
    #desplazamiento: controla si el salto se da en el eje X izquierda o derecha.
d = float(input('Ingrese el desplazamiento de la señal: '))
    #amplitud, controla si el salto se hace hacia arriba o hacia abajo.
l = float(input('Ingrese la amplitud de la señal: '))

#parametros de las funciones exponenciales.
#c = sigma + complejoj, conjunto complejo.
sigma = 0  
omega = 1 

#parametros de la grafica del rectangulo.
print("------------------------- RECTANGULAR.")
    #para dibujar el rectangulo en el eje X.
t1 = float(input('Ingrese el inicio (eje X): '))
t2 = float(input('Ingrese el fin (eje X): '))
    #para dibujar el rectangulo en el eje Y.
lR = float(input('Ingrese la amplitud de la señal: '))

#parametros de la grafica de impulso.
print("------------------------- IMPULSO.")
print("SOLO NUMEROS ENTEROS.")
    #se mueve izquierda o derecha en el eje X.
des = int(input('Ingrese el desplazamiento de la señal: '))
    #para hacerlo unitario l = 1
amp = int(input('Ingrese la amplitud de la señal: '))
    
#Llamada de las funciones.
EscalonUnitario(a, b, d, l, dt)
Exponencial(a, b, dt, sigma, omega)
ExponencialCausal(a, b, dt, sigma, omega)
rectangular(a, b, t1, t2, lR, dt)
Impuslo(a, b, des, amp, dt)

#Datos de investigacion.
#lambda: variable 
#piecewise: para una funcion a trozos, 