#!/usr/bin/env python3
"""
BENEL - COLLECTEUR DE DONNÉES EMPLOYÉ
Version qui met à jour directement le JSON pour index.html
"""

import requests
import json
import uuid
import sys
from datetime import datetime

def update_employee_data():
    print("=" * 50)
    print("📱 BENEL - Mise à jour des données employé")
    print("=" * 50)
    print()

    # Générer un ID unique
    employee_id = f"EMP_{uuid.uuid4().hex[:8].upper()}"
    print(f"👤 ID Employé: {employee_id}")

    # Données de démonstration
    device_info = {
        "model": "Mobile Device",
        "platform": "Android",
        "version": "1.0",
        "screen": "1080x1920"
    }

    # Données professionnelles simulées
    calls = [
        {
            "number": "+33123456789",
            "duration": "05:23",
            "type": "outgoing",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "number": "+33612345678", 
            "duration": "02:15", 
            "type": "incoming",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]

    sms = [
        {
            "number": "+33123456789",
            "message": "RDV confirmé pour demain 14h",
            "direction": "received", 
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "number": "+33612345678",
            "message": "Devis envoyé par email",
            "direction": "sent",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]

    # Structure des données pour index.html
    employee_data = {
        "calls": calls,
        "sms": sms,
        "device_info": device_info,
        "ip_address": "192.168.1.1",
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "received_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("📊 Données créées:")
    print(f"   - {len(calls)} appels")
    print(f"   - {len(sms)} SMS")
    print()

    # Envoyer via mobile-receive.php
    try:
        url = "https://leboncoin-reservation.netsons.org/test/mobile-receive.php"
        
        # Données au format attendu par mobile-receive.php
        payload = {
            "employee_id": employee_id,
            "device_info": device_info,
            "calls": calls,
            "sms": sms,
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print("🌐 Envoi au serveur...")
        response = requests.post(
            url,
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ SUCCÈS! Données envoyées")
            print("📊 Les données apparaîtront dans le monitoring")
            print(f"🔗 Accédez à: https://leboncoin-reservation.netsons.org/test/index.html")
        else:
            print(f"❌ Erreur HTTP {response.status_code}")
            print(f"📨 Réponse: {response.text}")
            
    except Exception as e:
        print(f"💥 Erreur: {e}")
        print("🔧 Vérifiez que mobile-receive.php fonctionne")

    print()
    print("=" * 50)
    
    if len(sys.argv) == 1:
        input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    update_employee_data()