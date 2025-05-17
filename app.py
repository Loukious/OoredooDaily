import requests
from dotenv import load_dotenv
import os
load_dotenv()


def ClaimDaily():
    url = "https://tn-oo-dailystickers.timwe.com/api/events/register/check-in"
    headers = {
        "Authorization": "Bearer " + os.getenv("TOKEN"),
        "mec": os.getenv("MEC"),
        "user-agent": "Mozilla/5.0 (Linux; Android 15; M2102J20SG Build/BP1A.250505.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/136.0.7103.60 Mobile Safari/537.36"
    }
    with requests.session() as s:
        r = s.post(url, headers=headers, json={}).json()
    print(r["description"])


ClaimDaily()
