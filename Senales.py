#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:37:19 2022

@author: julio
"""
import numpy as np
import matplotlib.pyplot as plt


def grafica(x, y, label, paso, num, label_legend):  
    plt.figure(num)
    plt.plot(x,y, label = label_legend )
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.margins(paso)
    plt.grid()
    plt.title(label)
   
    
def escalonUnitario(lim_neg_x, lim_x, paso):
    t = np.arange(lim_neg_x,lim_x, paso)
    u = lambda t: np.piecewise(t, t>=0 , [2,0]) 
    u0 = u(t-5)
    grafica(t, u0, "Escalon Unitario", paso, 1, "")

    
def exponencial(lim_neg_x, lim_x, paso, omega, sigma):
    t = np.arange(lim_neg_x,lim_x, paso)
    s = complex(sigma, omega)
    senal = np.exp(s*t)
    grafica(t, np.real(senal), "Funcion exponencial", paso, 2, "Real")
    grafica(t, np.imag(senal), "Funcion exponencial", paso, 2, "Imaginaria")
    grafica(t, np.imag(senal), "Funcion exponencial", paso, 2, "Imaginaria")
    
def exponencialCausal(lim_neg_x, lim_x, paso, omega, sigma):
    t = np.arange(lim_neg_x,lim_x, paso)
    s = complex(sigma, omega)
    senal = np.exp(s*t)
    u = lambda t: np.piecewise(t, t>=0 , [1,0]) 
    u0 = u(t-0)
    senal = senal*u0
    grafica(t, np.real(senal), 'Funcion Exponencial Causal', paso, 3, "Real")
    grafica(t, np.imag(senal), 'Funcion Exponencial Causal', paso, 3, "Imaginaria")
    
    
def rectangular(lim_neg_x, lim_x, paso):
    t = np.arange(lim_neg_x,lim_x+5, paso)
    u = lambda t: np.piecewise(t, t>=0 , [1,0]) 
    u0 = u(t-0)
    u1 = u(t-10)
    rectangular = u0-u1
    grafica(t, rectangular, "Funcion Rectangular", paso, 4, "")
    

def impulsounitario(lim_neg_x,lim_x, paso):
    t= np.arange(lim_neg_x-5, lim_x+5, paso)
    n =len(t)
    u = np.zeros(n)
    origen_indice= 0
    for i in range(0,n):
        if np.sign(t[i])!=np.sign(t[i-1]):
            origen_indice=i
    origen_indice -=120
    u[origen_indice] = 1
    grafica(t, u ,"Funcion impulso", paso, 5, "")
    

    
#Variables generales
lim_neg_x = -10
lim_x = 10
paso = 0.1
sigma = 0 #s = 0+ 0j
omega = 4


escalonUnitario(lim_neg_x, lim_x, paso)
exponencial(lim_neg_x, lim_x, paso, omega, sigma)


#Para convertir cualquier señal en causal lo unico que necesitamos hacer es multiplicarla 
# por el escalon
exponencialCausal(lim_neg_x, lim_x, paso, omega, sigma)

#Al restar dos funciones escalones desplazadas en el tiempo, vamos a obtener 
# un ancho de pulso o una fincion rectangular

rectangular(lim_neg_x, lim_x, paso)


impulsounitario(lim_neg_x, lim_x, paso)


