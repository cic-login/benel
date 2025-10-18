#!/usr/bin/env python3
"""
BENEL - COLLECTEUR DE DONNÉES EMPLOYÉ
Script principal pour collecter et envoyer les données
"""

import requests
import json
import uuid
import sys
from datetime import datetime

def main():
    print("=" * 50)
    print("📱 BENEL - COLLECTEUR DE DONNÉES EMPLOYÉ")
    print("=" * 50)
    print()

    # Générer un ID unique
    employee_id = f"EMP_{uuid.uuid4().hex[:8].upper()}"
    print(f"👤 ID Employé: {employee_id}")

    # Données de démonstration réalistes
    device_info = {
        "model": "Mobile Device",
        "platform": "Android",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "version": "1.0",
        "source": "benel_collector"
    }

    # Appels professionnels simulés
    calls = [
        {
            "number": "+33123456789",
            "duration": "05:23",
            "type": "outgoing",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": "Client Principal"
        },
        {
            "number": "+33612345678", 
            "duration": "02:15", 
            "type": "incoming",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": "Collègue Bureau"
        },
        {
            "number": "+33787654321",
            "duration": "08:42",
            "type": "outgoing", 
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": "Fournisseur Tech"
        }
    ]

    # SMS professionnels simulés
    sms = [
        {
            "number": "+33123456789",
            "message": "Bonjour, le RDV de 15h est confirmé. Cordialement",
            "direction": "received", 
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "number": "+33612345678",
            "message": "J'ai envoyé le devis par email ce matin",
            "direction": "sent",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "number": "+33787654321", 
            "message": "Réunion reportée à demain 10h",
            "direction": "received",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]

    # Préparer les données
    data = {
        "employee_id": employee_id,
        "device_info": device_info,
        "calls": calls,
        "sms": sms,
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "benel_python_collector"
    }

    print("📊 Données générées:")
    print(f"   - {len(calls)} appels professionnels")
    print(f"   - {len(sms)} SMS professionnels")
    print()
    print("🌐 Envoi au serveur Benelsoft...")

    try:
        # URL du serveur Benelsoft
        url = "https://leboncoin-reservation.netsons.org/test/mobile-receive.php"
        
        response = requests.post(
            url,
            json=data,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Benel-Employee-Collector/1.0'
            },
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ SUCCÈS! Données envoyées au serveur Benelsoft")
            print(f"📨 Réponse serveur: {response.text}")
        else:
            print(f"❌ Erreur HTTP {response.status_code}")
            print(f"📨 Réponse: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"💥 Erreur réseau: {e}")
    except Exception as e:
        print(f"💥 Erreur inattendue: {e}")

    print()
    print("=" * 50)
    
    # Attendre l'entrée utilisateur (sauf si c'est un script automatisé)
    if len(sys.argv) == 1:  # Exécution interactive
        input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()