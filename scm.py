import requests
import os
from dotenv import load_dotenv, find_dotenv

path = find_dotenv()

load_dotenv(path)

API_KEY = os.getenv("BREVO_API_KEY")

EMAIL = os.getenv("EMAIL")

def send_mail(booking_id,name,email,date,time,n_people,):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": API_KEY, 
        "content-type": "application/json"
    }

    payload = {
        "sender": {"name": "The Green Sprout Team", "email": EMAIL},
        "to": [{"email": email, "name": name}],
        "templateId": 1,
        "params": {
            "name": name,
            "booking_id": booking_id,
            "date": date,
            "time": time,
            "number": n_people,
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    #print(response.json())
    return (response.status_code)
    
    

