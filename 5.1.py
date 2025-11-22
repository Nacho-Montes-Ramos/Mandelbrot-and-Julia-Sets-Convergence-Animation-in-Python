# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 11:56:58 2025

@author: nacho
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import imageio.v2 as imageio

os.makedirs("framesMandelbrot", exist_ok=True)
os.makedirs("framesJulia", exist_ok=True)

pm = 800
x = np.linspace(-2, 1, pm)
y = np.linspace(-1.5, 1.5, pm)
X, Y = np.meshgrid(x, y)
c = X + 1j * Y
CM = np.zeros((pm, pm))
VM = np.zeros((pm, pm))
zM = 0
#Variables de Mandelbrot

pj = 800
xj = np.linspace(-2, 2, pj)
yj = np.linspace(-2, 2, pj)
XJ, YJ = np.meshgrid(xj, yj)
cj = XJ + 1j * YJ
CJ = np.zeros((pj, pj))
VJ = np.zeros((pj, pj))
#Variables Julia

for n in range (0, 501):
    zM = zM**2 + c
    zM[np.abs(zM)>2] = 2
    CM = np.abs(zM) < 2
    VM[CM] = n
    plt.imsave(f"framesMandelbrot/frame_{n:03d}.png", VM, cmap="inferno")
#Conjunt de Mandelbrot

framesMandelbrot = []
file_list = sorted(os.listdir("framesMandelbrot"))

for filename in file_list:
    if filename.endswith(".png"):
        framesMandelbrot.append(imageio.imread(f"framesMandelbrot/{filename}"))

imageio.mimsave("animacionMandelbrot.gif", framesMandelbrot, fps=10)
#Creo .gif de Mandelbrot

for n in range (0, 501):
    if n == 0:
        zJ = cj
    else:
        zJ = zJ**2 - 0.7269 + 1j*0.1889
    zJ[np.abs(zJ)>2] = 2
    CJ = np.abs(zJ) < 2
    VJ[CJ] = n
    plt.imsave(f"framesJulia/frame_{n:03d}.png", VJ, cmap="inferno")
#Conjunt de Julia

framesJulia = []
file_list = sorted(os.listdir("framesJulia"))

for filename in file_list:
    if filename.endswith(".png"):
        framesJulia.append(imageio.imread(f"framesJulia/{filename}"))

imageio.mimsave("animacionJulia.gif", framesJulia, fps=15)
#Creo .gif de Julia


plt.figure()
plt.imshow(CM, cmap='gray')

plt.figure()
plt.imshow(VM, cmap='jet')

plt.figure()
plt.imshow(CJ, cmap='gray')

plt.figure()
plt.imshow(VJ, cmap='jet')









