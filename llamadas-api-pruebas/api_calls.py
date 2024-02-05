import requests
import json
from api_config import (get_api_url, get_request_timeout, get_response_data_path, get_response_status_path)


def perform_api_call(method, resource, resource_id):
    url = get_api_url() + resource + ("/" + str(resource_id) if resource_id else "")
    headers = {"Content-Type": "application/json"}

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=get_request_timeout())
        elif method == "POST":
            data = read_json_file(resource + ".json")
            response = requests.post(url, json=data, headers=headers, timeout=get_request_timeout())
        elif method == "PUT":
            data = read_json_file(resource + ".json")
            response = requests.put(url, json=data, headers=headers, timeout=get_request_timeout())
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=get_request_timeout())
        else:
            raise ValueError("Invalid method")

        process_response(response, method, url)

    except requests.RequestException as e:
        print(f"Error: {e}")


def process_response(response, method, url):
    response_data = {
        "Method": method,
        "Url": url,
        "Status": response.status_code,
        "Content-Type": response.headers.get("Content-Type"),
        "Encoding": response.encoding
    }

    save_json_file(get_response_status_path(), response_data)
    save_json_file(get_response_data_path(), response.json())


def read_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)


def save_json_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
