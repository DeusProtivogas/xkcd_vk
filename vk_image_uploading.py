import requests


def upload_image_to_vk_group_wall(
        vk_token, group_id, vk_api, attachment, message
):
    url = f"https://api.vk.com/method/wall.post?owner_id=-{group_id}" \
          f"&message={message}&attachment={attachment}" \
          f"&access_token={vk_token}&v={vk_api}"

    response = requests.post(url)
    response.raise_for_status()

    return response.json()


def upload_image_to_vk_server(vk_token, group_id, vk_api, file_name):
    server_url = f"https://api.vk.com/method/photos.getWallUploadServer" \
                     f"?group_id={group_id}" \
                     f"&access_token={vk_token}&v={vk_api}"

    response = requests.get(server_url)
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

    wall_save_photo_url = f"https://api.vk.com/method/photos.saveWallPhoto?" \
                          f"&group_id={group_id}" \
                          f"&server={server}&hash={vk_hash}&photo={photo}" \
                          f"&access_token={vk_token}&v={vk_api}"

    response = requests.post(wall_save_photo_url)
    response.raise_for_status()
    return response.json()


def vk_get_groups(vk_token):
    url = f"https://api.vk.com/method/groups.get?" \
          f"filter=admin&access_token={vk_token}&v=5.154"

    response = requests.get(url)

    response.raise_for_status()
    return response.json()
