from tkinter import *
import tkinter as tk
i = 0
Root = tk.Tk()
Root.title("calculadora")
Root.config(bg="snow")
Root.resizable(False, False)
calculadora_cuadro = tk.Entry(Root)
calculadora_cuadro.config(font=("calibri", 20) )
calculadora_cuadro.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
def boton_puls(valor):
    global i
    calculadora_cuadro.insert(i, valor)
    i += 1
def borrar():
    global i
    calculadora_cuadro.delete(0, END)
    i = 0
def Motor():
    resultaod = eval(calculadora_cuadro.get())
    global i
    i = 0
    calculadora_cuadro.delete(0, END)
    calculadora_cuadro.insert(i, resultaod)

numero7 = tk.Button(Root, text="7", width=5, height=2, command=lambda:boton_puls(7))
numero7.grid(row=1, column=0)
numero8 = tk.Button(Root, text="8", width=5, height=2, command=lambda:boton_puls(8))
numero8.grid(row=1, column=1)
numero9 = tk.Button(Root, text="9", width=5, height=2, command=lambda:boton_puls(9))
numero9.grid(row=1, column=2)
numerodiv = tk.Button(Root, text="/", width=5, height=2, command=lambda:boton_puls("/"))
numerodiv.grid(row=1, column=3)
numero4 = tk.Button(Root, text="4", width=5, height=2, command=lambda:boton_puls(4))
numero4.grid(row=2, column=0, pady=5)
numero5 = tk.Button(Root, text="5", width=5, height=2, command=lambda:boton_puls(5))
numero5.grid(row=2, column=1, pady=5)
numero6 = tk.Button(Root, text="6", width=5, height=2, command=lambda:boton_puls(6))
numero6.grid(row=2, column=2, pady=5)
numeroX = tk.Button(Root, text="*", width=5, height=2, command=lambda:boton_puls("*"))
numeroX.grid(row=2, column=3, pady=5)
numero1 = tk.Button(Root, text="1", width=5, height=2, command=lambda:boton_puls(1))
numero1.grid(row=3, column=0, pady=5)
numero2 = tk.Button(Root, text="2", width=5, height=2, command=lambda:boton_puls(2))
numero2.grid(row=3, column=1, pady=5)
numero3 = tk.Button(Root, text="3", width=5, height=2, command=lambda:boton_puls(3))
numero3.grid(row=3, column=2, pady=5)
numeromen = tk.Button(Root, text="-", width=5, height=2, command=lambda:boton_puls("-"))
numeromen.grid(row=3, column=3, pady=5)
numero0 = tk.Button(Root, text="0", width=5, height=2, command=lambda:boton_puls(0))
numero0.grid(row=4, column=0, pady=5)
numeromas = tk.Button(Root, text="+", width=5, height=2, command=lambda:boton_puls("+"))
numeromas.grid(row=4, column=1, pady=5)
numeroigu = tk.Button(Root, text="=", width=5, height=2, command=Motor)
numeroigu.grid(row=4, column=3, pady=5)
borrar = tk.Button(Root, text="AC", width=5, height=2, command=borrar)
borrar.grid(row=4, column=2, pady=5)



Root.mainloop()
