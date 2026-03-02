# data_fetcher.py
import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "hvuQ6NjIxuF0lAiZcjZ5yl0Sl0Yf86gbiHbQnETG"

def fetch_data(name):
    headers = {"X-Api-Key": API_KEY}
    params = {"name": name}
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

