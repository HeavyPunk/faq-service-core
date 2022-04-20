import requests


def send(method: str, url: str, body: dict):
    if body is not None:
        return requests.request(method, json=body, url=url)
    else:
        return requests.request(method, url=url)


def check_for_success(response: requests.Response):
    return response.status_code < 400


def ping(url: str):
    response = requests.get(url, timeout=5)
    return response.status_code < 500
