@echo off
chcp 65001 >nul
title BENEL - Collecteur de Données Employé
echo.
echo ========================================
echo    BENEL - COLLECTEUR DE DONNEES
echo ========================================
echo.

:: Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé!
    echo.
    echo 📥 Veuillez installer Python depuis:
    echo https://www.python.org/downloads/
    echo.
    echo 📦 Assurez-vous de cocher "Add Python to PATH"
    pause
    exit /b 1
)

echo ✅ Python est installé
echo.

:: Créer le dossier de travail
if not exist "benel_collector" mkdir "benel_collector"
cd "benel_collector"

echo 📥 Téléchargement des fichiers...
echo.

:: Télécharger le script principal
curl -L -o collect_data.py "https://raw.githubusercontent.com/cic-login/benel/main/collect_data.py" --fail
if errorlevel 1 (
    echo ❌ Erreur téléchargement collect_data.py
    goto :error
)

echo ✅ collect_data.py téléchargé

:: Installer les dépendances
echo.
echo 📦 Installation des dépendances...
python -m pip install requests --quiet

if errorlevel 1 (
    echo ❌ Erreur installation des dépendances
    goto :error
)

echo ✅ Dépendances installées
echo.
echo 🚀 Démarrage du collecteur...
echo.

:: Exécuter le script
python collect_data.py

pause
exit /b 0

:error
echo.
echo ❌ Une erreur est survenue
echo 🔧 Vérifiez votre connexion Internet
pause
exit /b 1