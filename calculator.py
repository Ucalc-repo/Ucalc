import tkinter
import math


m = float(input("masa del balón: "))
g = float(input("aceleracion gravitacional: "))
k = float(input("constante del resorte: "))
hf = float(input("altura final: "))
ho = float(input("altura inicial: "))
t = float(input("valor t: "))

theta = math.degrees(45)

L = (12*math.pow(t, 3)) + (5*math.pow(t, 2)) + (3*math.pow(t, 1)) + 10 

v2 = ((L * L) * g) / (2 * (math.cos(theta) * math.cos(theta)) * (hf - ho - (L * math.tan(theta))))

Xc = math.sqrt((m * (v2))/k)

print(Xc)