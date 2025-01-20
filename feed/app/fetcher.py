import requests

def fetch_oscal_feed(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/AustralianCyberSecurityCentre/ism-oscal/main/controls.json"
    data = fetch_oscal_feed(url)
    print(data)
