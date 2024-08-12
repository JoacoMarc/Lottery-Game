import random
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from colorama import init
from PIL import Image, ImageTk
import os

# Inicializa Colorama
init(autoreset=True)

class LotoPlusApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Loto Plus")
        self.geometry("700x500")
        self.configure(bg="#f0f0f0")
        
        # Cargar imágenes de bolas (más grandes)
        self.balls_images = [ImageTk.PhotoImage(Image.open(f"C:/Users/joaco/Desktop/Python/Projects/Lottery-Project/Balls_png/ball_{i}.png").resize((135, 135))) for i in range(51)]

        # Inicializar lista de números sorteados y ganadores
        self.lista_numeros = []
        self.lista_ganadores = []
        self.agencias = {}

        # Interfaz del menú
        self.create_widgets()
    
    def create_widgets(self):
        # Título
        title_label = tk.Label(self, text="Bienvenido a Loto Plus", font=("Arial", 24, "bold"), fg="blue", bg="#f0f0f0")
        title_label.pack(pady=20)

        subtitle_label = tk.Label(self, text="Lotería de la Ciudad de Buenos Aires", font=("Arial", 16), fg="black", bg="#f0f0f0")
        subtitle_label.pack(pady=10)

        # Botones del menú
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=20)

        btn_ver_numeros = tk.Button(button_frame, text="Ver Números Sorteados", command=self.show_numbers, font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=10)
        btn_ver_numeros.grid(row=0, column=0, padx=10, pady=10)

        btn_ver_ganadores = tk.Button(button_frame, text="Ver Ganadores", command=self.show_winners, font=("Arial", 14), bg="#2196F3", fg="white", padx=10, pady=10)
        btn_ver_ganadores.grid(row=0, column=1, padx=10, pady=10)

    def show_numbers(self):
        # Check if numbers have already been drawn
        if not self.lista_numeros:
            self.lista_numeros = sorteo_de_numeros()

        self.animate_drawing()

    def animate_drawing(self):
        # Crear ventana para mostrar la animación con tamaño más grande
        self.draw_window = tk.Toplevel(self)
        self.draw_window.title("Sorteo")
        self.draw_window.geometry("1000x400")  # Aumenta el tamaño de la ventana
        self.draw_window.configure(bg="#f0f0f0")
        
        # Espacio para mostrar las bolas
        self.ball_labels = [tk.Label(self.draw_window, bg="#f0f0f0") for _ in range(6)]
        for label in self.ball_labels:
            label.pack(side="left", padx=10)

        self.update_balls()

    def update_balls(self, i=0):
        if i < len(self.lista_numeros):
            num = self.lista_numeros[i]
            if 0 <= num < len(self.balls_images):  # Check to ensure num is within the correct range
                self.ball_labels[i].config(image=self.balls_images[num])
            else:
                print(f"Warning: Generated number {num} is out of range.")
            self.after(500, self.update_balls, i+1)  # Animar con un retraso de 0.5 segundos por bola
        else:
            self.draw_window.after(2000, self.draw_window.destroy)  # Cerrar la ventana de sorteo después de 2 segundos

    def show_winners(self):
        if not self.lista_ganadores:  # Calculate winners only if not already calculated
            try:
                self.lista_ganadores, self.agencias = leer_archivo_excel("C:/Users/joaco/Desktop/Python/Projects/Lottery-Project/apuestas.xlsx", self.lista_numeros)
            except FileNotFoundError:
                messagebox.showerror("Error", "Archivo de apuestas no encontrado.")
                return
            except Exception as e:
                messagebox.showerror("Error", str(e))
                return

        self.display_winners()

    def display_winners(self):
        # Ventana para mostrar ganadores con tamaño más grande
        winners_window = tk.Toplevel()
        winners_window.title("Ganadores")
        winners_window.geometry("800x600")  # Aumenta el tamaño de la ventana
        
        tk.Label(winners_window, text="Ganadores", font=("Arial", 18, "bold")).pack(pady=10)
        
        for i, ganador in enumerate(self.lista_ganadores, start=1):
            tk.Label(winners_window, text=f"{i}. DNI: {ganador['DNI']} - AGENCIA: {ganador['AGENCIA']}", font=("Arial", 14)).pack()

def sorteo_de_numeros(n=6, rango=50, lista_actual=[]):
    if n == 0:
        return lista_actual
    else:
        numero = random.randint(0, rango)
        if numero not in lista_actual:
            lista_actual.append(numero)
            return sorteo_de_numeros(n - 1, rango, lista_actual)
        else:
            return sorteo_de_numeros(n, rango, lista_actual)

def leer_archivo_excel(archivo, lista_numeros):
    # Leer archivo Excel de apuestas, identificando ganadores y contando apuestas por agencia
    df = pd.read_excel(archivo)
    ganadores = []
    agencias = {}
    mayor_numero_coincidente = 0

    for index, row in df.iterrows():
        numero_coincidente = sum(num in lista_numeros for num in row[2:])
        ganador = {"DNI": row["DNI"], "AGENCIA": row["AGENCIA"]}

        if numero_coincidente == mayor_numero_coincidente:
            ganadores.append(ganador)
        elif numero_coincidente > mayor_numero_coincidente:
            ganadores = [ganador]
            mayor_numero_coincidente = numero_coincidente

        agencias[row["AGENCIA"]] = agencias.get(row["AGENCIA"], 0) + 1

    return ganadores, agencias

if __name__ == "__main__":
    app = LotoPlusApp()
    app.mainloop()
