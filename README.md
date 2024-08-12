
# 🎉 py-Lottery 🎉

## 🎟️ Introduction

Welcome to **py-Lottery**, your very own Python-powered lottery game inspired by the thrills of "Loto Plus" and the "Lotería de la Ciudad de Buenos Aires"! This game brings the excitement of lottery drawings straight to your screen, with a beautiful graphical interface and engaging animations. Ready to try your luck? Let's dive in! 🎲

## 🌟 Features

- **✨ Interactive GUI**: Say goodbye to boring command lines! py-Lottery features a **Tkinter-based GUI** that makes it super easy to draw numbers and check winners.
- **🔢 Random Number Drawing**: Our game uses a smart recursive algorithm to ensure that each draw is unique and totally random.
- **🏆 Winner Identification**: Automatically checks all participants against the drawn numbers and crowns the lucky winners!
- **🎨 Animated Number Display**: Watch your numbers come to life as colorful, bouncing lottery balls!
- **🗂️ File Management**: Seamlessly reads and writes Excel files for participant data and agency details.
- **🚫 Error Handling**: No more crashes! Our game gently guides you through any issues, like missing files or out-of-range numbers.

## 🚀 Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/JoacoMarc/py-Lottery.git
    cd py-Lottery
    ```

2. **Extract the assets**:
   - **Important:** After cloning, make sure to **extract** any `.zip` files **directly into the project directory**. This will ensure that all necessary files are in the right place.

3. **Install required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
   - **Reminder:** Ensure that all libraries listed in `requirements.txt` are installed to avoid any issues running the program.

4. **Prepare the assets**:
   - Ensure the lottery ball images (`ball_0.png` to `ball_50.png`) are located in the `Balls_png` folder within the project directory.
   - Place the `apuestas.xlsx` file in the project directory, containing participant data with columns for DNI, agency, and six lottery numbers.

## 🎮 How to Play

1. **Run the game**:
    ```sh
    python lottery.py
    ```

2. **Navigate the GUI**:
   - 🎲 **Ver Números Sorteados**: Watch the animated lottery balls reveal your lucky numbers!
   - 🏅 **Ver Ganadores**: See if you're a winner by checking the results!
   - Both views are displayed in **beautifully large windows** for easy viewing.

## 🖼️ GUI Overview

The py-Lottery GUI is designed to be both fun and functional, with vibrant colors and smooth animations to enhance your lottery experience.


### Key Buttons

- **🎲 Ver Números Sorteados**: Click to reveal the drawn numbers with exciting animations.
- **🏅 Ver Ganadores**: Click to see the list of winners, displayed in a large and clear window.

## 🛠️ Code Overview

### Core Components

- **LotoPlusApp**: The heart of our Tkinter application, managing everything from user interaction to visual effects.
- **sorteo_de_numeros**: Ensures each lottery draw is fair and unique.
- **leer_archivo_excel**: Reads participant data from Excel, checks for winners, and organizes the results.
- **animate_drawing**: Brings the lottery balls to life with animations.
- **update_balls**: Manages the visual updates during the number draw.
- **display_winners**: Presents the winning participants in a clear and engaging format.

### Main Program Features

- **🎉 Number Consistency**: Once numbers are drawn, they remain consistent, ensuring fairness across the game.
- **💾 Reliable File Handling**: Manages your Excel files with care, preventing errors and data loss.

