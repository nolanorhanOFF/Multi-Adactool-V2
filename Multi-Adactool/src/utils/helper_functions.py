import re
import socket

def is_valid_ip(ip):
    """Vérifie si l'adresse IP fournie est valide."""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def print_banner(message):
    """Affiche un message de manière formatée en tant que bannière."""
    banner = f"\n{'=' * 20}\n{message}\n{'=' * 20}\n"
    print(banner)

def handle_error(exception):
    """Gère et affiche les erreurs."""
    print(f"An error occurred: {str(exception)}")

def get_user_input(prompt):
    """Demande une entrée utilisateur avec le message fourni."""
    return input(prompt)

def print_success(message):
    """Affiche un message de succès."""
    print(f"[SUCCESS] {message}")

def print_failure(message):
    """Affiche un message d'échec."""
    print(f"[FAILURE] {message}")

def is_valid_domain(domain):
    """Vérifie si le domaine fourni est valide."""
    regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$'
    return re.match(regex, domain) is not None
