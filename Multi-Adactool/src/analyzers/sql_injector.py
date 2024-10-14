import sqlite3
import colorama
from colorama import Fore

# Initialiser Colorama
colorama.init(autoreset=True)

def create_database():
    # Créer une base de données fictive et une table pour l'exemple
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Insérer des données d'exemple
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
    
    connection.commit()
    connection.close()

def sql_injection_attack(username):
    # Connexion à la base de données
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Injection SQL potentielle
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(Fore.CYAN + "Access Granted:")
            for row in result:
                print(Fore.CYAN + f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}")
        else:
            print(Fore.CYAN + "No user found.")
    except Exception as e:
        print(Fore.CYAN + f"An error occurred: {e}")
    finally:
        connection.close()

def main():
    create_database()  # Créer la base de données et les utilisateurs
    print(Fore.CYAN + "=== SQL Injector ===")
    username = input(Fore.CYAN + "Enter username to test SQL Injection: ")
    
    # Effectuer l'injection SQL
    sql_injection_attack(username)

if __name__ == "__main__":
    main()
