import random
import requests


def get_random_comics():

    url_latest = "https://xkcd.com/info.0.json"

    response = requests.get(url_latest)
    response.raise_for_status()

    latest_comics = response.json().get("num")
    comics_num = random.randint(1, latest_comics)

    url_random = f"https://xkcd.com/{comics_num}/info.0.json"
    response = requests.get(url_random)
    response.raise_for_status()

    image_link = response.json().get("img")
    message = response.json().get("alt")
    print(message)

    image = requests.get(image_link)
    image.raise_for_status()

    file_name = f"xkcd_{comics_num}.png"

    with open(file_name, 'wb') as file:
        file.write(image.content)

    return message, file_name
