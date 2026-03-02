# data_fetcher.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
print(API_KEY)

API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(name):
    headers = {"X-Api-Key": API_KEY}
    params = {"name": name}
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

