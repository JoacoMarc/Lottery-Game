import random
from colorama import Fore, Style, init, Back

# Inicializa Colorama
init(autoreset=True)

def menu():
    # Muestra el menú con opciones
    print(Fore.MAGENTA + Style.BRIGHT + "=============================================================")
    print(Fore.CYAN + Style.BRIGHT + "Bienvenido a Loto Plus / Loterìa de la Ciudad de Buenos Aires")
    print(Fore.MAGENTA + Style.BRIGHT + "=============================================================", end="\n\n")
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Seleccione una opción:", end="\n")
    print(Fore.YELLOW + "1)" + Style.RESET_ALL + " Para ver los números sorteados")
    print(Fore.YELLOW + "2)" + Style.RESET_ALL + " Para ver los ganadores")
    print(Fore.YELLOW + "3)" + Style.RESET_ALL + " Para ver las agencias participantes")
    print(Fore.YELLOW + "4)" + Style.RESET_ALL + " Para crear un archivo con las agencias participantes", end="\n\n")
    input_usuario = int(input(""))

    return input_usuario

def sorteo_de_numeros(n=6, rango=41, lista_actual=[]):
    # Realiza un sorteo recursivo de 6 números, sin repetir números
    if n == 0:
        return lista_actual
    else:
        numero = random.randint(0, rango)
        if numero not in lista_actual:
            lista_actual.append(numero)
            return sorteo_de_numeros(n - 1, rango, lista_actual)
        else:
            return sorteo_de_numeros(n, rango, lista_actual)

def rellenar_matriz(matriz_num_sorteados, filas, columnas, lista_sorteados):
    # Rellena una matriz con los números sorteados
    i = 0
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(lista_sorteados[i])
            i += 1
        matriz_num_sorteados.append(fila)
    return matriz_num_sorteados


def leer_archivo(archivo):
    # Lee el archivo de apuestas, identificando ganadores y contando apuestas por agencia
    l = archivo.readline()
    
    ganadores = []
    agencias = {}
    cont=0
    mayor_numero_coincidente = 0
    while l:
        numero_coincidente = 0

        linea = l.split(";")
        linea[-1] = linea[-1].rstrip('\n')

        for i in range(2, len(linea)):
            num = int(linea[i])
            if num in lista_numeros:
                numero_coincidente += 1

        ganador={ "DNI": linea[0],
        "AGENCIA": linea[1],
        }
        
        if numero_coincidente == mayor_numero_coincidente:
            ganadores.append(ganador)
        elif numero_coincidente > mayor_numero_coincidente:
            ganadores = []
            ganadores.append(ganador)
            mayor_numero_coincidente = numero_coincidente

        
        try:
            agencias[str(linea[1])] = agencias[str(linea[1])]+1
        except KeyError:
            agencias[str(linea[1])] = 1

        cont+=1


        l = archivo.readline()

    return ganadores, agencias


def imprimir_ticket(matriz):    
    # Convertir cada fila de la matriz en una cadena y unirlas con saltos de línea
    numeros_sorteados = " ".join(" ".join(str(num) for num in fila) for fila in matriz)
    # Crear contenido del ticket
    lines = [
        "Loto Plus",
        "SORTEO 3158 del 14/11/2023",
        "14/11/2023",
        numeros_sorteados,
        "TOTAL:              $40.00",
        "ID TICKET: 171 006 514 045 002 358/0272",
        "AB0000001-0167003-10140191-1568-0115"
    ]

    max_width = max(len(line) for line in lines)
    border = "+" + "-" * max_width + "+"
    separator = "|" + " " * max_width + "|"


    print(Back.WHITE + Fore.BLACK + border)
    for line in lines:
        centered_line = line.center(max_width)
        print(Back.WHITE + Fore.BLACK + "|" + Fore.GREEN + Style.BRIGHT + centered_line + Back.WHITE + Fore.BLACK + "|")
        print(Back.WHITE + Fore.BLACK + separator)
    print(Back.WHITE + Fore.BLACK + border)


def imprimir_ganadores(lista_ganadores):
    # Imprime la lista de ganadores, mostrando DNI y agencia
    cont = 0
    print(Fore.GREEN + Style.BRIGHT + "\nGANADORES: ", end="\n\n")
    for ganador in lista_ganadores:
        cont += 1
        print(cont, "DNI:" , ganador["DNI"] , "   AGENCIA:",ganador["AGENCIA"])


def crear_archivo_agencias(agencias):
    # Crea un archivo de texto con la lista de agencias y la cantidad de apostadores en cada una
    with open("agencias.txt", "w") as archivo_agencias:
        for agencia, cantidad in agencias.items():
            archivo_agencias.write(f"{agencia}: {cantidad} apostadores\n")


def ordenar(e):
    # Función de ayuda para ordenar por DNI
    return e["DNI"]

# Manejo de excepciones y flujo principal del programa
try:
    archivo = open("apuestas.txt", "rt")

    while True:

        try:
            
            filas = 2
            columnas = 3
            matriz_num_sorteados = []

            lista_numeros = sorteo_de_numeros()

            lista_ganadores, agencias =(leer_archivo(archivo))

            while lista_ganadores == []:
                lista_numeros = sorteo_de_numeros()
                lista_ganadores, agencias =(leer_archivo(archivo))

            matriz = rellenar_matriz(matriz_num_sorteados, filas, columnas, lista_numeros)

            lista_ganadores.sort(key=ordenar)
            agencias = dict(sorted(agencias.items(), key=lambda x: x[1], reverse=True))


            input_usuario = menu()
            input_dos = 0

            while input_usuario != -1 and input_dos != -1:
                if input_usuario not in range(1,5):
                    print("Ingrese una opcion valida")
                    input_usuario = menu()
                if input_usuario == 1:
                    imprimir_ticket(matriz)
                    input_dos = int(input("\nIngrese 0 para volver al menu o -1 para terminar: "))
                    if input_dos == 0:
                        input_usuario = menu()
                elif input_usuario == 2:
                    imprimir_ganadores(lista_ganadores)
                    input_dos = int(input("\nIngrese 0 para volver al menu o -1 para terminar: "))
                    if input_dos == 0:
                        input_usuario = menu()
                elif input_usuario == 3:
                    print(agencias)
                    input_dos = int(input("\nIngrese 0 para volver al menu o -1 para terminar: "))
                    if input_dos == 0:
                        input_usuario = menu()
                elif input_usuario==4:
                    crear_archivo_agencias(agencias)
                    input_dos = int(input("\nIngrese 0 para volver al menu o -1 para terminar: "))
                    if input_dos == 0:
                        input_usuario = menu()

            break

        except ValueError:
            print()
            print("Error: Ingrese un numero, 1, 2 o 3")
            print()
        except Exception as e:
            print()
            print("Error: ", e)
            print()
except FileNotFoundError:
    print()
    print("No se encontro el archivo")
    print()
except IOError:
    print("Error al cerrar/abrir el archivo")
finally:
   archivo.close()