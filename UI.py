import tkinter as tk
from tkinter import *
import calculator

root = tk.Tk()
root.geometry('1000x700')
root.title("Ucalc Interfaz")
root.attributes('-fullscreen', True)


# Definir la función para abrir una nueva ventana
def abrir_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.geometry("300x200")
    nueva_ventana.title("AYUDA")
    etiqueta = tk.Label(nueva_ventana, text="1. Ingresa los datos en cada variable. \n 2. Haz click en calcular y espera a que se procesen los datos. \n 3. La calculadora regresará resultados a partir de la información dada")
    etiqueta.pack()
# Crear un botón para abrir la nueva ventana
boton = tk.Button(root, text="¿AYUDA?", command=abrir_ventana)
boton.pack()


# Crea una etiqueta para el título "VALORES DE ENTRADA"
title_label = tk.Label(root, text='VALORES DE ENTRADA', font=('Arial', 14))
title_label.pack(pady=10)
title_label.place(relx=0.019, rely=0.1)
# Crea una etiqueta para el título "RESULTADO"
title_label = tk.Label(root, text='RESULTADO', font=('Arial', 16))
title_label.pack(pady=10)
title_label.place(relx=0.5, rely=0.1)


# Crea una entrada para el primer valor (m)
first_entry = tk.Entry(root, width=9, font=('Arial', 10))
first_entry.pack(pady=5)
first_entry.place(relx=0.18, rely=0.162)
# Crea una entrada para el segundo valor (g)
second_entry = tk.Entry(root, width=9, font=('Arial', 10))
second_entry.pack(pady=5)
second_entry.place(relx=0.18, rely=0.212)
# Crea una entrada para el tercer valor (K)
Third_entry = tk.Entry(root, width=9, font=('Arial', 10))
Third_entry.pack(pady=5)
Third_entry.place(relx=0.18, rely=0.262)
# Crea una entrada para el Cuarto valor (Hf)
Fourth_entry = tk.Entry(root, width=9, font=('Arial', 10))
Fourth_entry.pack(pady=5)
Fourth_entry.place(relx=0.18, rely=0.312)
# Crea una entrada para el QUINTO valor (Ho)
Fifth_entry = tk.Entry(root, width=9, font=('Arial', 10))
Fifth_entry.pack(pady=5)
Fifth_entry.place(relx=0.18, rely=0.362)
# Crea una entrada para el SEXTO valor (L)
Sixth_entry = tk.Entry(root, width=9, font=('Arial', 10))
Sixth_entry.pack(pady=5)
Sixth_entry.place(relx=0.18, rely=0.412)
# Crea una entrada para el SEPTIMO valor (t)
seventh_entry = tk.Entry(root, width=9, font=('Arial', 10))
seventh_entry.pack(pady=5)
seventh_entry.place(relx=0.18, rely=0.462)


# Crear los botones donde estaran los valores de entrada, donde si les picas, sale que son
def mostrar_masa():
    texto.config(text="Masa del Objeto")
    texto.place(x=55, y=115)
button = tk.Button(root, text='m', font=('Arial', 9), command=mostrar_masa)
button.pack(pady=5)
button.place(relx=0.147, rely=0.16)

texto = tk.Label(root, text="")
texto.pack()


def mostrar_gravedad():
    texto.config(text="gravedad del Objeto")
    texto.place(x=36, y=152)
button = tk.Button(root, text='g', font=('Arial', 9), command=mostrar_gravedad)
button.pack(pady=5)
button.place(relx=0.147, rely=0.21)

texto = tk.Label(root, text="")
texto.pack()


def mostrar_Constante():
    texto.config(text="Constante del Objeto")
    texto.place(x=30, y=190)
button = tk.Button(root, text='K', font=('Arial', 9), command=mostrar_Constante)
button.pack(pady=5)
button.place(relx=0.147, rely=0.26)

texto = tk.Label(root, text="")
texto.pack()

button = tk.Button(root, text='Hf', font=('Arial', 9))
button.pack(pady=5)
button.place(relx=0.147, rely=0.31)

button = tk.Button(root, text='Ho', font=('Arial', 9))
button.pack(pady=5)
button.place(relx=0.147, rely=0.36)

button = tk.Button(root, text='L', font=('Arial', 9))
button.pack(pady=5)
button.place(relx=0.147, rely=0.41)

button = tk.Button(root, text='t', font=('Arial', 9))
button.pack(pady=5)
button.place(relx=0.147, rely=0.46)


# Crear el botón pa calcular (aun no funciona xdd)
boton = tk.Button(root, text="CALCULAR")
boton.place(relx=0.185, rely=0.51)

root.mainloop()
