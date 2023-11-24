import requests


def check_vk_response(response):
    if isinstance(response, dict) and response.get("error"):
        raise requests.HTTPError(
            f'Error {response.get("error").get("error_code")}, '
            f'{response.get("error").get("error_msg")}'
        )


def post_image_to_vk_group_wall(
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
    parsed_response = response.json()
    check_vk_response(parsed_response)
    return parsed_response


def upload_image_to_vk_server(vk_token, group_id, vk_api, file_name):
    params = {
        "group_id": group_id,
        "access_token": vk_token,
        "v": vk_api,
    }
    server_url = f"https://api.vk.com/method/photos.getWallUploadServer"

    response = requests.get(server_url, params=params)
    response.raise_for_status()
    parsed_response = response.json()
    check_vk_response(parsed_response)
    upload_url = response.json().get("response").get("upload_url")

    with open(file_name, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(upload_url, files=files)
    response.raise_for_status()

    parsed_response = response.json()
    server = parsed_response.get("server")
    photo = parsed_response.get("photo")
    vk_hash = parsed_response.get("hash")

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
    check_vk_response(response)
    response.raise_for_status()
    return response.json()
