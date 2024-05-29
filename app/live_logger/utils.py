import requests


def download_ipinfo(ip):
    try:
        data = requests.get(f'http://ipinfo.io/{ip}/json').json()
    except:
        return
    return data