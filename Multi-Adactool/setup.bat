@echo off
SETLOCAL

REM Vérifie si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé. Veuillez l'installer avant de continuer.
    exit /b 1
)

REM Vérifie si pip est installé
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pip n'est pas installé. Veuillez l'installer avant de continuer.
    exit /b 1
)

REM Installer les dépendances à partir de requirements.txt
echo Installation des dépendances...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo L'installation des dépendances a échoué.
    exit /b 1
)

echo Installation terminée avec succès.

REM Exécute le fichier main.py
echo Lancement de l'application...
python main.py

ENDLOCAL
pause
