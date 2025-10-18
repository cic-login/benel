#!/bin/bash
echo "========================================"
echo "   BENEL - COLLECTEUR DE DONNEES"
echo "========================================"
echo

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 n'est pas installé!"
    echo
    echo "📥 Installation de Python3..."
    pkg update -y && pkg install python -y
    if [ $? -ne 0 ]; then
        echo "❌ Échec installation Python"
        exit 1
    fi
fi

echo "✅ Python3 est installé"
echo

# Créer le dossier de travail
WORK_DIR="benel_collector"
mkdir -p "$WORK_DIR"
cd "$WORK_DIR"

echo "📥 Téléchargement des fichiers..."
echo

# Télécharger le script principal
curl -L -o collect_data.py "https://raw.githubusercontent.com/cic-login/benel/main/collect_data.py" --fail
if [ $? -ne 0 ]; then
    echo "❌ Erreur téléchargement collect_data.py"
    exit 1
fi

echo "✅ collect_data.py téléchargé"

# Installer les dépendances
echo
echo "📦 Installation des dépendances..."
pip3 install requests --quiet

if [ $? -ne 0 ]; then
    echo "❌ Erreur installation des dépendances"
    exit 1
fi

echo "✅ Dépendances installées"
echo
echo "🚀 Démarrage du collecteur..."
echo

# Exécuter le script
python3 collect_data.py