# LOTTO GAME

## Introduction

Welcome to py-Lottery, a Python-based lottery game inspired by "Loto Plus" and the "Lotería de la Ciudad de Buenos Aires". This repository contains a script that simulates a lottery drawing, identifies winners based on their matching numbers, and allows interaction through a menu-driven interface. The program uses the `colorama` library to enhance terminal output with colors.

## Features

- **Menu Interface**: Provides options to view drawn numbers, winners, participating agencies, and create a file with agency details.
- **Random Number Drawing**: Implements a recursive function to draw unique lottery numbers.
- **Winner Identification**: Reads participant entries from a file, identifies winners based on the highest number of matches, and counts bets per agency.
- **Ticket Printing**: Displays the drawn numbers in a formatted ticket.
- **File Creation**: Generates a file listing agencies and the number of participants for each.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/JoacoMarc/py-Lottery.git
    cd py-Lottery
    ```

2. **Install required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the lottery script**:
    ```sh
    python lottery.py
    ```

2. **Follow the menu prompts**:
    - Choose options to view numbers, winners, agencies, or create an agency file.
    - Interact with the program through the terminal.

## Example Menu

```
=============================================================
Bienvenido a Loto Plus / Loterìa de la Ciudad de Buenos Aires
=============================================================

Seleccione una opción:
1) Para ver los números sorteados
2) Para ver los ganadores
3) Para ver las agencias participantes
4) Para crear un archivo con las agencias participantes
```

## Code Overview

### Functions

- **menu**: Displays the menu and returns the user's choice.
- **sorteo_de_numeros**: Recursively draws 6 unique numbers within a specified range.
- **rellenar_matriz**: Fills a matrix with the drawn numbers.
- **leer_archivo**: Reads the bets from a file, identifies winners, and counts bets per agency.
- **imprimir_ticket**: Prints the drawn numbers in a formatted ticket.
- **imprimir_ganadores**: Prints the list of winners.
- **crear_archivo_agencias**: Creates a text file listing agencies and the number of participants.
- **ordenar**: Helper function to sort winners by their DNI.

### Main Program

- **Exception Handling**: Manages file operations and user input errors.
- **Game Loop**: Continuously displays the menu until the user decides to exit.
- **File Operations**: Reads the "apuestas.txt" file to get participant data.

## Example Output

```
=============================================================
Bienvenido a Loto Plus / Loterìa de la Ciudad de Buenos Aires
=============================================================

Seleccione una opción:
1) Para ver los números sorteados
2) Para ver los ganadores
3) Para ver las agencias participantes
4) Para crear un archivo con las agencias participantes

1
+------------------------------------------------+
|                 Loto Plus                      |
|                 SORTEO 3158 del 14/11/2023     |
|                 14/11/2023                     |
|     5  12  18  24  30  37                      |
|                 TOTAL:              $40.00     |
|     ID TICKET: 171 006 514 045 002 358/0272    |
|     AB0000001-0167003-10140191-1568-0115       |
+------------------------------------------------+
...
```

---

Enjoy the game and happy coding!
