import os
import requests
from dotenv import load_dotenv

from xkcd_images import get_random_comic
from xkcd_images import get_random_url_filename
from vk_image_uploading import upload_image_to_vk_server
from vk_image_uploading import upload_image_to_vk_group_wall


def main():
    load_dotenv()
    vk_token = os.environ['VK_KEY']
    group_id = os.environ['VK_GROUP_ID']
    vk_api_version = os.environ['VK_API_VERSION']

    url_comic, comic_name = get_random_url_filename()

    try:
        message = get_random_comic(url_comic, comic_name)
        image_owner_id = upload_image_to_vk_server(
            vk_token, group_id, vk_api_version, comic_name
        )

        attachment = f"photo{image_owner_id.get('response')[0].get('owner_id')}_" \
                     f"{image_owner_id.get('response')[0].get('id')}"
        upload_image_to_vk_group_wall(
            vk_token, group_id, vk_api_version, attachment, message
        )
    except requests.HTTPError as e:
        print(e)
    except ValueError:
        print("Error occurred!")
    finally:
        os.remove(comic_name)


if __name__ == '__main__':
    main()
