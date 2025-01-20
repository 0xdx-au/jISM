import requests
import time
import json
import os

def fetch_oscal():
    url = "https://raw.githubusercontent.com/AustralianCyberSecurityCentre/ism-oscal/main/controls.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        with open('/app/data/controls.json', 'w') as f:
            json.dump(data, f)
        print("Successfully fetched OSCAL data")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching OSCAL data: {e}")
        return None

if __name__ == '__main__':
    while True:
        data = fetch_oscal()
        if data:
            print(f"Loaded {len(data.get('controls', []))} controls")
        time.sleep(3600)  # Wait an hour before checking again
