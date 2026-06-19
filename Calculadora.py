import tkinter as tk

# ---------------- FUNCIONES ----------------

def presionar(tecla):
    entrada.set(entrada.get() + str(tecla))

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(str(resultado))
    except:
        entrada.set("Error")

def limpiar():
    entrada.set("")

# ---------------- VENTANA ----------------

ventana = tk.Tk()
ventana.title("🍅 Calculadora Azul")
ventana.geometry("320x500")
ventana.config(bg="#87CEEB")  # azul cielo

entrada = tk.StringVar()

# ---------------- IMAGEN TOMATE ----------------

try:
    imagen_tomate = tk.PhotoImage(file="tomate.png")

    label_imagen = tk.Label(
        ventana,
        image=imagen_tomate,
        bg="#87CEEB"
    )
    label_imagen.grid(row=0, column=0, columnspan=4, pady=5)

except:
    label_imagen = tk.Label(
        ventana,
        text="🍅 Tomate no encontrado",
        bg="#87CEEB",
        font=("Arial", 14, "bold")
    )
    label_imagen.grid(row=0, column=0, columnspan=4)

# ---------------- PANTALLA ----------------

pantalla = tk.Entry(
    ventana,
    textvariable=entrada,
    font=("Arial", 22, "bold"),
    justify="right",
    bg="#F0F8FF",   # azul muy claro
    fg="#003366"
)

pantalla.grid(row=1, column=0, columnspan=4,
              padx=10, pady=10, sticky="nsew")

# ---------------- BOTONES ----------------

botones = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for texto, fila, columna in botones:

    if texto == "=":
        comando = calcular
        color = "#1E90FF"  # azul fuerte
    else:
        comando = lambda t=texto: presionar(t)
        color = "#4682B4"  # azul acero

    tk.Button(
        ventana,
        text=texto,
        font=("Arial", 16, "bold"),
        bg=color,
        fg="white",
        activebackground="#87CEFA",
        command=comando
    ).grid(row=fila, column=columna,
            sticky="nsew", padx=5, pady=5)

# ---------------- BOTÓN LIMPIAR ----------------

tk.Button(
    ventana,
    text="C",
    font=("Arial", 16, "bold"),
    bg="#1E90FF",
    fg="white",
    command=limpiar
).grid(row=6, column=0, columnspan=4,
       sticky="nsew", padx=5, pady=5)

# ---------------- AJUSTE DE GRID ----------------

for i in range(7):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

ventana.mainloop()