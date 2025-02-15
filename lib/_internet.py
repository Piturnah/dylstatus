import urllib.request
hostname = "https://www.google.com"


def internet_connected():
    res = urllib.request.urlopen(hostname)
    if res.status == 200:
        return True
    else:
        return False


def get_block(module_info: dict):
    block = {"name": "internet"}

    if internet_connected():
        block["full_text"] = "Connected"
        block["color"] = "#00ff00"
    else:
        block["full_text"] = "Not Connected"
        block["color"] = "#ff0000"

    return block
