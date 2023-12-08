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
        file.write(content)


def get_and_save(uri, file_name):
    response = requests.get(f"{printify_base_url}{uri}", headers=headers)
    content = json.loads(response.content)
    content_json = json.dumps(content, indent=2)
    save(content_json, file_name)


def post_and_save(uri, body, file_name):
    response = requests.post(f"{printify_base_url}{uri}", headers=headers, data=json.dumps(body))
    content = json.loads(response.content)
    content_json = json.dumps(content, indent=2)
    save(content_json, file_name)
    return content


def post(uri, body):
    requests.post(f"{printify_base_url}{uri}", headers=headers, data=json.dumps(body))
