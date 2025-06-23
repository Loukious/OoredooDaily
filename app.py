import requests
from dotenv import load_dotenv
import os
load_dotenv()


def GetToken():
    url = "https://tn-oo-dailystickers.timwe.com/api/auth"
    headers = {
        "authorization": "Basic " + os.getenv("AUTH"),
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "origin": "https://tn-oo-dailystickers.timwe.com",
        "mec": os.getenv("MEC"),
    }
    with requests.session() as s:
        r = s.post(url, headers=headers, json={}).json()
    return r["access_token"]

def ClaimDaily():
    url = "https://tn-oo-dailystickers.timwe.com/api/events/register/check-in"
    headers = {
        "Authorization": "Bearer " + GetToken(),
        "mec": os.getenv("MEC"),
        "user-agent": "Mozilla/5.0 (Linux; Android 15; M2102J20SG Build/BP1A.250505.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/136.0.7103.60 Mobile Safari/537.36"
    }
    with requests.session() as s:
        r = s.post(url, headers=headers, json={}).json()
    print(r["description"])


ClaimDaily()
