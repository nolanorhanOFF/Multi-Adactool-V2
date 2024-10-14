import os
from colorama import Fore, Style, init

init(autoreset=True)  # Initialise colorama et réinitialise les styles après chaque print

def clear_console():
    """Efface la console selon le système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_cyan(text):
    """Affiche le texte en cyan."""
    print(f"{Fore.CYAN}{text}{Style.RESET_ALL}")

def display_menu():
    """Affiche le menu avec la bannière en cyan."""
    print_cyan(" ▄▄▄      ▓█████▄  ▄▄▄       ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    ")
    print_cyan("▒████▄    ▒██▀ ██▌▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ")
    print_cyan("▒██  ▀█▄  ░██   █▌▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ")
    print_cyan("░██▄▄▄▄██ ░▓█▄   ▌░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ")
    print_cyan(" ▓█   ▓██▒░▒████▓  ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒")
    print_cyan(" ▒▒   ▓▒█░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░")
    print_cyan("  ▒   ▒▒ ░ ░ ▒  ▒   ▒   ▒▒ ░  ░  ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░")
    print_cyan("  ░   ▒    ░ ░  ░   ░   ▒   ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ")
    print_cyan("      ░  ░   ░          ░  ░░ ░                   ░ ░      ░ ░      ░  ░")
    print_cyan("           ░                ░                                           ")

def main():
    while True:
        clear_console()  # Efface la console à chaque itération
        display_menu()   # Affiche le menu

        print_cyan("Select an option:")
        print_cyan("1. Port Scanner")
        print_cyan("2. Network Scanner")
        print_cyan("3. Vulnerability Scanner")
        print_cyan("4. SQL Injector")
        print_cyan("5. Info Gatherer")
        print_cyan("6. DoS Attack Simulator")
        print_cyan("7. Phishing Tool")
        print_cyan("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            os.system('python src/scanners/port_scanner.py')
        elif choice == '2':
            os.system('python src/scanners/network_scanner.py')
        elif choice == '3':
            os.system('python src/analyzers/vulnerability_scanner.py')
        elif choice == '4':
            os.system('python src/analyzers/sql_injector.py')
        elif choice == '5':
            os.system('python src/gatherers/info_gatherer.py')
        elif choice == '6':
            os.system('python src/attacks/dos_attack.py')
        elif choice == '7':
            os.system('python src/attacks/phishing_tool.py')
        elif choice == '8':
            print_cyan("Exiting...")
            break
        else:
            print_cyan("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
