import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("PRINTIFY_TOKEN")
headers = {
    "Authorization": f"Bearer {token}"
}
printify_base_url = "https://api.printify.com"


def save(response, file_name):
    content = json.loads(response.content)
    with open(f"Saves/{file_name}.json", "w") as file:
        file.write(json.dumps(content, indent=2))


def get_and_save(uri, file_name):
    response = requests.get(f"{printify_base_url}{uri}", headers=headers)
    save(response, file_name)


def post_and_save(uri, body, file_name):
    print(json.dumps(body, indent=2))
    response = requests.post(f"{printify_base_url}{uri}", headers=headers, data=json.dumps(body))
    print(response.status_code)
    print(response.content)
    save(response, file_name)
