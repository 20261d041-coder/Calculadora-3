import tkinter as tk
import math

# Funciones
def presionar(valor):
    entrada.set(entrada.get() + str(valor))

def limpiar():
    entrada.set("")

def borrar():
    entrada.set(entrada.get()[:-1])

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.set(str(resultado))
    except:
        entrada.set("Error")

def funcion_matematica(func):
    try:
        valor = float(entrada.get())

        if func == "sqrt":
            resultado = math.sqrt(valor)
        elif func == "sin":
            resultado = math.sin(math.radians(valor))
        elif func == "cos":
            resultado = math.cos(math.radians(valor))
        elif func == "tan":
            resultado = math.tan(math.radians(valor))
        elif func == "log":
            resultado = math.log10(valor)
        elif func == "ln":
            resultado = math.log(valor)

        entrada.set(str(resultado))
    except:
        entrada.set("Error")

# Ventana
ventana = tk.Tk()
ventana.title("💖 Calculadora Científica Rosada")
ventana.geometry("450x600")
ventana.config(bg="#FFC0CB")  # Rosa

entrada = tk.StringVar()

# Pantalla
pantalla = tk.Entry(
    ventana,
    textvariable=entrada,
    font=("Arial", 24),
    justify="right",
    bg="#FFF0F5",
    fg="#C71585"
)
pantalla.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# Estilo botones
color_btn = "#FF69B4"
color_texto = "white"

# Botones científicos
cientificos = [
    ("sin", lambda: funcion_matematica("sin")),
    ("cos", lambda: funcion_matematica("cos")),
    ("tan", lambda: funcion_matematica("tan")),
    ("√", lambda: funcion_matematica("sqrt")),
    ("log", lambda: funcion_matematica("log")),
]

for i, (texto, comando) in enumerate(cientificos):
    tk.Button(
        ventana,
        text=texto,
        command=comando,
        bg="#FF1493",
        fg="white",
        font=("Arial", 14, "bold")
    ).grid(row=1, column=i, sticky="nsew", padx=3, pady=3)

# Botones principales
botones = [
    ('7',2,0), ('8',2,1), ('9',2,2), ('/',2,3), ('^',2,4),
    ('4',3,0), ('5',3,1), ('6',3,2), ('*',3,3), ('(',3,4),
    ('1',4,0), ('2',4,1), ('3',4,2), ('-',4,3), (')',4,4),
    ('0',5,0), ('.',5,1), ('=',5,2), ('+',5,3), ('π',5,4),
]

for texto, fila, columna in botones:

    if texto == "=":
        comando = calcular

    elif texto == "π":
        comando = lambda: presionar(str(math.pi))

    elif texto == "^":
        comando = lambda: presionar("**")

    else:
        comando = lambda t=texto: presionar(t)

    tk.Button(
        ventana,
        text=texto,
        command=comando,
        bg=color_btn,
        fg=color_texto,
        font=("Arial", 16, "bold")
    ).grid(row=fila, column=columna, sticky="nsew", padx=3, pady=3)

# Botones especiales
tk.Button(
    ventana,
    text="C",
    command=limpiar,
    bg="#DB7093",
    fg="white",
    font=("Arial", 16, "bold")
).grid(row=6, column=0, columnspan=2, sticky="nsew", padx=3, pady=3)

tk.Button(
    ventana,
    text="⌫",
    command=borrar,
    bg="#DB7093",
    fg="white",
    font=("Arial", 16, "bold")
).grid(row=6, column=2, columnspan=3, sticky="nsew", padx=3, pady=3)

# Ajuste de tamaño
for i in range(7):
    ventana.grid_rowconfigure(i, weight=1)

for j in range(5):
    ventana.grid_columnconfigure(j, weight=1)

ventana.mainloop()

# Ventana
ventana = tk.Tk()
ventana.title("🧮 Calculadora Científica")
ventana.geometry("450x600")
ventana.config(bg="#FA8072")  # Salmón

# Pantalla
pantalla = tk.Entry(
    ventana,
    textvariable=entrada,
    font=("Arial", 24),
    justify="right",
    bg="#FFF5EE",
    fg="#8B3A3A"
)