import tkinter as tk
from tkinter import messagebox
from nltk import CFG, ChartParser

from AST import parse_and_print_ast

# Definir la gramática
gramatica = CFG.fromstring("""
    E -> E '+' T | E '-' T | T
    T -> T '*' F | T '/' F | F
    F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

parser = ChartParser(gramatica)

def TratarExpresion(expresion):
    expresion = expresion.strip()  # Elimina espacios extra al inicio y al final
    expresion = expresion.lower()  # Convierte toda la expresión a minúsculas
    return ' '.join(list(expresion))  # Separa cada carácter con un espacio

def Get_AST():
    # Obtener la expresión ingresada
    Input = entrada.get()
    expresion = TratarExpresion(Input)
    return parse_and_print_ast(expresion)

def analizar_expresion():
    # Obtener la expresión ingresada
    Input = entrada.get()
    expresion = TratarExpresion(Input)

    if not expresion:
        messagebox.showerror("Error", "Por favor ingresa una expresión.")
        return
    
    # Separar los tokens de la expresión
    fragmentos = expresion.split()
    try:
        # Generar el árbol de derivación
        arboles = list(parser.parse(fragmentos))
        if arboles:
            resultado.delete("1.0", tk.END)  # Limpiar área de texto
            for tree in arboles:
               
                tree.pretty_print()
                tree.draw()  # Mostrar el árbol en una ventana gráfica
        else:
            messagebox.showinfo("Sin resultados", "No se encontró ninguna derivación para la expresión ingresada.")
    except ValueError as e:
        messagebox.showerror("Error")

def showDerivationLeft():
    Input = entrada.get()
    expresion = TratarExpresion(Input)

    if not expresion:
        messagebox.showerror("Error", "Por favor ingresa una expresión.")
        return
    
    expresion = expresion.split()

    try:
        resultado.delete("1.0", tk.END)  # Limpiar área de texto
        resultado.insert(tk.END, "Derivaciones:\n")
        for tree in parser.parse(expresion):
            for derivacion in tree.productions():
                resultado.insert(tk.END, f"{derivacion}\n")
    except:
        messagebox.showerror("Error")
    
def showDerivationRight():
    Input = entrada.get()
    expresion = TratarExpresion(Input)

    if not expresion:
        messagebox.showerror("Error", "Por favor ingresa una expresión.")
        return
    
    # Separar la expresión en tokens
    fragmentos = expresion.split()  

    try:
        resultado.delete("1.0", tk.END)  # Limpiar área de texto
          # Parsear la expresión como está
        arboles = list(parser.parse(fragmentos))
        if arboles:
            resultado.insert(tk.END, "Derivaciones:\n")

            for tree in arboles:
                
                # Mostrar las producciones en orden inverso
                derivaciones = list(tree.productions())

                for derivacion in reversed(derivaciones):
                    resultado.insert(tk.END, f"{derivacion}\n")
        else:
                messagebox.showinfo("Sin resultados", "No se encontró ninguna derivación para la expresión ingresada.")

    except:
        messagebox.showerror("Error")
    

        
        

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Sintáctico con NLTK")
ventana.geometry("600x400")
ventana.configure(bg="#212121")  # Fondo 

# Entrada para la expresión
tk.Label(ventana, text="Ingrese la expresión:", font=("Arial", 14), fg="white", bg="#212121").pack(pady=10)
entrada = tk.Entry(ventana, width=50, font=("Arial", 14), bg="#424242", fg="white", insertbackground="white")
entrada.pack(pady=5)

# Botón para analizar
tk.Button(
    ventana, 
    text="Analizar", 
    font=("Arial", 14), 
    command=analizar_expresion, 
    bg="#6A1B9A", 
    fg="white", 
    activebackground="#512D6D", 
    activeforeground="white"
).pack(pady=10)

# Botón para AST
tk.Button(
    ventana, 
    text="Obtener AST", 
    font=("Arial", 14), 
    command=Get_AST, 
    bg="#6A1B9A", 
    fg="white", 
    activebackground="#512D6D", 
    activeforeground="white"
).pack(pady=10)

# Botón para Derivacion
tk.Button(
    ventana, 
    text="Obtener Derivacion por izquierda", 
    font=("Arial", 14), 
    command=showDerivationLeft, 
    bg="#6A1B9A", 
    fg="white", 
    activebackground="#512D6D", 
    activeforeground="white"
).pack(pady=10)

# Botón para Derivacion
tk.Button(
    ventana, 
    text="Obtener Derivacion por derecha", 
    font=("Arial", 14), 
    command=showDerivationRight, 
    bg="#6A1B9A", 
    fg="white", 
    activebackground="#512D6D", 
    activeforeground="white"
).pack(pady=10)

# Área de texto para mostrar resultados
resultado = tk.Text(ventana, height=15, font=("Courier", 12), bg="#424242", fg="white", insertbackground="white")
resultado.pack(pady=10)

# Iniciar el loop de la ventana
ventana.mainloop()
