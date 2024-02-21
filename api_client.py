import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("PRINTIFY_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
printify_base_url = "https://api.printify.com"


def save(content, file_name):
    with open(f"Saves/{file_name}.json", "w") as file:
        file.write(json.dumps(content, indent=2))


def get_and_save(uri, file_name):
    response = requests.get(f"{printify_base_url}{uri}", headers=headers)
    content = response.json()
    save(content, file_name)


def post_and_save(uri, body, file_name):
    response = requests.post(f"{printify_base_url}{uri}", headers=headers, data=json.dumps(body))
    content = response.json()
    save(content, file_name)
    return content


def post(uri, body):
    response = requests.post(f"{printify_base_url}{uri}", headers=headers, data=json.dumps(body))
    return response.json()


def get(uri):
    response = requests.get(f"{printify_base_url}{uri}", headers=headers)
    return response.json()


def put(uri, body):
    response = requests.put(f"{printify_base_url}{uri}", headers=headers, data=json.dumps(body))
    return response.json()
