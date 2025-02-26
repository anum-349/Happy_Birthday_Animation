import os
import random
import time
from random import randint
from playsound import playsound
import threading

# ANSI escape codes for colors
colors = {
    'crimson': '\033[38;2;220;20;60m',  
    'yellow': '\033[93m',
    'grey': '\033[90m',
    'red': '\033[91m',
    'green': '\033[92m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'teal': '\033[36m',         
    'coral': '\033[91m',        
    'peach': '\033[93m',        
    'lime': '\033[92;1m',       
    'zinc': '\033[90;1m',       
    'lavender': '\033[95;1m',   
    'olive': '\033[32m',        
    'navy': '\033[34m',         
    'orange': '\033[91;1m',     
    'purple': '\033[35m',       
    'violet': '\033[95;1m',     
    'pink': '\033[95m',
    'reset': '\033[0m'
}

def colored(text, color):
    return f"{colors.get(color, colors['white'])}{text}{colors['reset']}"

# Simulated ASCII Art
cake = [
    " ",
    "\t\t\t\t\t \t\t                ()   ()   ()",
    "\t\t\t\t\t \t\t            ____|| _ || _ ||___",
    "\t\t\t\t\t \t\t           |::::||:::||:::||:::|",
    "\t\t\t\t\t \t\t           |::::||:::||:::||:::|",
    "\t\t\t\t\t \t\t           |:::::::::::::::::::|",
    "\t\t\t\t\t \t\t       |:::::::::::::::::::::::::::|",
    "\t\t\t\t\t \t\t       |:::::::::::::::::::::::::::|",
    "\t\t\t\t\t \t\t     |:::::::::::::::::::::::::::::::|",
    "\t\t\t\t\t \t\t     |:::::::::::::::::::::::::::::::|",
    "\t\t\t\t\t \t\t      -------------------------------",
    "\t\t\t\t\t \t\t                \\^^^^^^^/",
    "\t\t\t\t\t \t\t                 \\^^^^^/",
    "\t\t\t\t\t \t\t                  \\^^^/",
    "\t\t\t\t\t \t\t                  /^^^\\",
    "\t\t\t\t\t \t\t                 /^^^^^\\",
    "\t\t\t\t\t \t\t                /^^^^^^^\\",
    "\t\t\t\t\t \t\t           -------------------"
]

happy = [
    "\t\t\t\t\t \t          _   _      _      ____    ____   __   __         ",
    "\t\t\t\t\t \t         | | | |    / \\    |  _ \\  |  _ \\  \\ \\ / /      ",
    "\t\t\t\t\t \t         | |_| |   / _ \\   | |_) | | |_) |  \\ V /         ",
    "\t\t\t\t\t \t         |  _  |  / ___ \\  |  __/  |  __/    | |      ",    
    "\t\t\t\t\t \t         |_| |_| /_/   \\_\\ |_|     |_|       |_|"    
]

Birthday = [
    "\t\t\t\t\t         ____    ___   ____    _____   _   _   ____       _     __   __ ",       
    "\t\t\t\t\t        | __ )  |_ _| |  _ \\  |_   _| | | | | |  _ \\     / \\    \\ \\ / / ",
    "\t\t\t\t\t        |  _ \\   | |  | |_) |   | |   | |_| | | | | |   / _ \\    \\ V /   ",     
    "\t\t\t\t\t        | |_) |  | |  |  _ <    | |   |  _  | | |_| |  / ___ \\    | | ",
    "\t\t\t\t\t        |____/  |___| |_| \\_\\   |_|   |_| |_| |____/  /_/   \\_\\   |_|"
]

To = [
    "\t\t\t\t\t \t\t\t    _____    ___",
    "\t\t\t\t\t \t\t\t   |_   _|  / _ \\     ",  
    "\t\t\t\t\t \t\t\t     | |   | | | |      ",
    "\t\t\t\t\t \t\t\t     | |   | |_| |   ", 
    "\t\t\t\t\t \t\t\t     |_|    \\___/  "
]

Laiba = [
    "\t\t\t\t\t \t\t    _          _      ___   ____       _",
    "\t\t\t\t\t \t\t   | |        / \\    |_ _| | __ )     / \\     ",                     
    "\t\t\t\t\t \t\t   | |       / _ \\    | |  |  _ \\    / _ \\       ",                  
    "\t\t\t\t\t \t\t   | |___   / ___ \\   | |  | |_) |  / ___ \\      ",                        
    "\t\t\t\t\t \t\t   |_____| /_/   \\_\\ |___| |____/  /_/   \\_\\ "
]

obj = [cake, happy, Birthday, To, Laiba]

# ---- Function to print character by character ----
def type_out(text_array, delay=0.03):
    for line in text_array:
        for char in line:
            print(colored(char, random.choice(list(colors.keys()))), end='', flush=True)
            time.sleep(delay)
        print() 

# ---- Prompt to start ----
str1= 'Press Enter and let the magic unfold.\nA delightful surprise awaits.\nAre you ready for an amazing experience?'
for i in str1:
    print(colored(i, 'crimson'), end='', flush=True)
    time.sleep(0.03)
print()  
time.sleep(1)
input(colored('If you’re ready, press Enter', 'purple'))
os.system('clear')

# Play Music
def play_sound(file_path):
    while True:  # Loop until script ends
        playsound(file_path)

# Path to your sound file
sound_file = "birthday.mp3"

# Create and start a daemon thread to play the sound in the background
sound_thread = threading.Thread(target=play_sound, args=(sound_file,), daemon=True)
sound_thread.start()

str2 ="\t\t\t\t\t\t\t✨✨✨ The moment of magic has arrived! ✨✨✨"
for i in str2:
    print(colored(i, 'magenta'), end='', flush=True)
    time.sleep(0.01)
print()
# Function to wish birthday 
def birthday_code():
    space = '    '  
    for i in range(10, 100):
        count = randint(1, 100)
        space = '   ' * count
        random_color = random.choice(list(colors.keys()))  
        
        if i % 10 == 0:
            line = "Happy Birthday To You " + "\U0001F370"
            print(space,end="")
            for char in line:
                print(colored(char, random.choice(list(colors.keys()))), end='', flush=True)
                time.sleep(0.05)
        elif i % 9 == 0: 
            line = "LOVE  YOU " + "\U0001F970 " +"LAIBA"
            print(space,end="")
            for char in line:
                print(colored(char, random.choice(list(colors.keys()))), end='', flush=True)
                time.sleep(0.05)
        elif i % 8 == 0:
            print(colored(space + "\U0001F618", random_color))
        elif i % 7 == 0:
            print(colored(space + "\U0001F973", random_color))
        elif i % 6 == 0:
            print(colored(space + "\U0001F49D", random_color))
        elif i % 5 == 0:
            print(colored(space + "\U0001F355", random_color))
        elif i % 4 == 0:
            print(colored(space + "\U0001F379", random_color))
        else:
            print(colored(space + "\U0001F382", random_color))
        time.sleep(0.1)

# ---- Function to create colorful bars ----
def colorful_bars(x, times=160):
    bar = '▼' if x == 'open' else '▲'
    for _ in range(times):
        print(colored(bar, random.choice(list(colors.keys()))), end='')

# ---- Function to print falling ASCII art ----
def fall(lsts, delay):
    for item in lsts:
        for line in item:
            print(colored(line, random.choice(list(colors.keys()))), end='\n', flush=True)
            time.sleep(delay)
            
#execute
colorful_bars('open')   
birthday_code() 
for item in obj:      
    type_out(item, 0.01)
colorful_bars('close')  
