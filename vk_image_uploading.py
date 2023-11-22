import requests


def upload_image_to_vk_group_wall(
        vk_token, group_id, vk_api, attachment, message
):
    params = {
        "owner_id": f"-{group_id}",
        "message": message,
        "attachment": attachment,
        "access_token" : vk_token,
        "v": vk_api,
    }

    url = f"https://api.vk.com/method/wall.post"

    response = requests.post(url, params=params)
    response.raise_for_status()

    return response.json()


def upload_image_to_vk_server(vk_token, group_id, vk_api, file_name):
    params = {
        "group_id": group_id,
        "access_token": vk_token,
        "v": vk_api,
    }
    server_url = f"https://api.vk.com/method/photos.getWallUploadServer"

    response = requests.get(server_url, params=params)
    upload_url = response.json().get("response").get("upload_url")

    with open(file_name, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()

        response_json = response.json()
        server = response_json.get("server")
        photo = response_json.get("photo")
        vk_hash = response_json.get("hash")

    params = {
        "group_id": group_id,
        "server": server,
        "hash": vk_hash,
        "photo": photo,
        "access_token": vk_token,
        "v": vk_api,
    }
    wall_save_photo_url = f"https://api.vk.com/method/photos.saveWallPhoto"

    response = requests.post(wall_save_photo_url, params=params)
    response.raise_for_status()
    return response.json()


def vk_get_groups(vk_token):
    params = {
        "filter": "admin",
        "access_token": vk_token,
        "v": "5.154",
    }

    url = f"https://api.vk.com/method/groups.get"

    response = requests.get(url, params=params)

    response.raise_for_status()
    return response.json()
