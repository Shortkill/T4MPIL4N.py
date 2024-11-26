import os
from art import text2art
import pyfiglet
from colorama import Fore, Style

def print_ascii_art():
    os.system('clear')  

    
    banner = text2art("CyberForce")
    print(Fore.GREEN + banner + Style.RESET_ALL)

    
    text = pyfiglet.figlet_format("Welcome!")
    print(Fore.RED + text + Style.RESET_ALL)

    
    print(Fore.YELLOW + "Banner printed...\nThis is a demo force tool." + Style.RESET_ALL)

if __name__ == "__main__":
    print_ascii_art()
