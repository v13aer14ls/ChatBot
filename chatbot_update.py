import requests

url = "https://api.telegram.org/bot620155979:AAHMyrpOIi7z22PcDUu9uKIxA9vuepGR4hc/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]