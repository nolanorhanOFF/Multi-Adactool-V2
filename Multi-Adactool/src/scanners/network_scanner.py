import scapy.all as scapy
from colorama import init, Fore, Style

# Initialisation de colorama pour Windows et autres systèmes
init(autoreset=True)

def scan_network(ip_range):
    """Scanne le réseau pour découvrir les hôtes actifs."""
    print(f"{Fore.CYAN}Scanning network: {ip_range}...{Style.RESET_ALL}")
    
    # Envoie une requête ARP pour découvrir les hôtes
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print(f"{Fore.CYAN}Active hosts:{Style.RESET_ALL}")
    for element in answered_list:
        print(f"{Fore.CYAN}IP: {element[1].psrc} | MAC: {element[1].hwsrc}{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}=== Network Scanner ==={Style.RESET_ALL}")
    ip_range = input(f"{Fore.CYAN}Enter the IP range to scan (e.g., 192.168.1.1/24): {Style.RESET_ALL}")
    
    # Scanner le réseau
    scan_network(ip_range)

if __name__ == "__main__":
    main()
