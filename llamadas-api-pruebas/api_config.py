import json


def get_api_url():
    with open("config.json", "r") as file:
        config = json.load(file)
        return config["url"]


def get_request_timeout():
    with open("config.json", "r") as file:
        config = json.load(file)
        return config["request_time_out"]


def get_response_data_path():
    with open("config.json", "r") as file:
        config = json.load(file)
        return config["response_data"]


def get_response_status_path():
    with open("config.json", "r") as file:
        config = json.load(file)
        return config["response_status"]