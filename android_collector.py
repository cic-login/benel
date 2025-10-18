#!/usr/bin/env python3
"""
Script simple pour collecter et envoyer des données depuis Android
À exécuter avec Termux ou tout environnement Python sur Android
"""

import json
import requests
import uuid
from datetime import datetime
import socket
import subprocess
import sys

def get_android_info():
    """Récupère les informations de l'appareil Android"""
    try:
        # Informations de base
        device_info = {
            "device_id": str(uuid.uuid4())[:8],
            "timestamp": datetime.now().isoformat(),
            "hostname": socket.gethostname(),
            "platform": sys.platform,
            "python_version": sys.version
        }
        
        # Essayer de récupérer des infos Android via Termux
        try:
            # CPU info
            with open('/proc/cpuinfo', 'r') as f:
                cpu_info = f.read()
                device_info["cpu"] = "Android Device"
        except:
            device_info["cpu"] = "Unknown"
            
        return device_info
    except Exception as e:
        return {"error": str(e), "timestamp": datetime.now().isoformat()}

def generate_sample_data():
    """Génère des données d'exemple"""
    calls = [
        {
            "number": "+33123456789",
            "duration": "05:23",
            "type": "outgoing",
            "timestamp": datetime.now().isoformat(),
            "name": "Client Principal"
        },
        {
            "number": "+33612345678", 
            "duration": "02:15",
            "type": "incoming",
            "timestamp": datetime.now().isoformat(),
            "name": "Collègue Bureau"
        }
    ]
    
    sms = [
        {
            "number": "+33123456789",
            "message": "RDV confirmé pour demain 14h",
            "direction": "received",
            "timestamp": datetime.now().isoformat()
        },
        {
            "number": "+33612345678",
            "message": "Devis envoyé par email",
            "direction": "sent", 
            "timestamp": datetime.now().isoformat()
        }
    ]
    
    return calls, sms

def send_data():
    """Envoie les données au serveur"""
    print("🚀 Démarrage de la collecte...")
    
    # Générer l'ID employé
    employee_id = f"PYTHON_{str(uuid.uuid4())[:8]}"
    print(f"📝 ID Employé: {employee_id}")
    
    # Collecter les informations
    print("📱 Collecte des informations appareil...")
    device_info = get_android_info()
    
    print("📞 Génération des données d'appels...")
    calls, sms = generate_sample_data()
    
    # Préparer les données
    data = {
        "employee_id": employee_id,
        "device_info": device_info,
        "calls": calls,
        "sms": sms,
        "collected_at": datetime.now().isoformat(),
        "source": "python_script"
    }
    
    print(f"📊 Données à envoyer: {len(calls)} appels, {len(sms)} SMS")
    
    # Envoyer au serveur
    try:
        print("🌐 Envoi au serveur...")
        url = "https://leboncoin-reservation.netsons.org/test/mobile-receive.php"
        
        response = requests.post(
            url,
            json=data,
            headers={'Content-Type': 'application/json', 'User-Agent': 'Python-Employee-Monitor'},
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ SUCCÈS: Données envoyées avec succès!")
            print(f"📨 Réponse serveur: {response.text}")
        else:
            print(f"❌ ERREUR: Code {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"💥 ERREUR: {str(e)}")

def main():
    print("=" * 50)
    print("📱 EMPLOYEE MONITOR - COLLECTEUR DE DONNÉES")
    print("=" * 50)
    
    try:
        send_data()
    except KeyboardInterrupt:
        print("\n⏹️  Collecte annulée par l'utilisateur")
    except Exception as e:
        print(f"💥 Erreur inattendue: {e}")
    
    print("\n" + "=" * 50)
    input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()