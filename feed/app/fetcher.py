import requests
import json
import time
import os
import psycopg2
from datetime import datetime

def get_db():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'ism'),
        user=os.getenv('DB_USER', 'ism'),
        password=os.getenv('DB_PASS', 'ism')
    )

def fetch_oscal():
    try:
        # First try loading from local cache
        with open('/app/data/controls.json', 'r') as f:
            return json.load(f)
    except:
        try:
            # If cache fails, fetch from GitHub
            url = "https://raw.githubusercontent.com/AustralianCyberSecurityCentre/ism-oscal/main/controls.json"
            print(f"Fetching OSCAL feed from: {url}")
            response = requests.get(url, timeout=10)
            data = response.json()
            
            # Save to cache
            with open('/app/data/controls.json', 'w') as f:
                json.dump(data, f)
            
            return data
        except Exception as e:
            print(f"Error fetching OSCAL: {e}")
            return None

def main():
    while True:
        try:
            data = fetch_oscal()
            if data:
                print(f"Successfully loaded {len(data.get('controls', []))} controls")
            time.sleep(3600)  # Check hourly
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Retry sooner on error

if __name__ == "__main__":
    main()
