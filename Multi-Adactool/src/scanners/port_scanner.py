import socket
from colorama import init, Fore, Style

# Initialisation de colorama pour Windows et autres systèmes
init(autoreset=True)

def scan_ports(target, port_range):
    """Scanne les ports d'un hôte donné dans une plage spécifiée."""
    print(f"{Fore.CYAN}Scanning ports on {target}...{Style.RESET_ALL}")

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout de 1 seconde pour chaque connexion
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"{Fore.CYAN}Port {port} is open{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Port {port} is closed{Style.RESET_ALL}")
        
        sock.close()

def main():
    print(f"{Fore.CYAN}=== Port Scanner ==={Style.RESET_ALL}")
    target = input(f"{Fore.CYAN}Enter the target IP or domain (e.g., example.com): {Style.RESET_ALL}")
    start_port = int(input(f"{Fore.CYAN}Enter start port: {Style.RESET_ALL}"))
    end_port = int(input(f"{Fore.CYAN}Enter end port: {Style.RESET_ALL}"))
    
    # Créer une plage de ports à scanner
    port_range = range(start_port, end_port + 1)

    # Scanner les ports
    scan_ports(target, port_range)

if __name__ == "__main__":
    main()
