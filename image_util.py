import base64


def base64_image(file_name):
    with open(f"Images/{file_name}", "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")
