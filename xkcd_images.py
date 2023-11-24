import random
import requests


def get_random_url_filename():
    latest_url = "https://xkcd.com/info.0.json"

    response = requests.get(latest_url)
    response.raise_for_status()

    latest_comics = response.json().get("num")
    comics_num = random.randint(1, latest_comics)

    random_comic_url = f"https://xkcd.com/{comics_num}/info.0.json"
    file_name = f"xkcd_{comics_num}.png"

    return random_comic_url, file_name


def get_random_comic(url_random, file_name):

    response = requests.get(url_random)
    response.raise_for_status()
    response_parsed = response.json()

    image_link = response_parsed.get("img")
    message = response_parsed.get("alt")

    comic_response = requests.get(image_link)
    comic_response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(comic_response.content)
    return message
