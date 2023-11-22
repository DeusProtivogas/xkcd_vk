import os
from dotenv import load_dotenv

from xkcd_images import get_random_comic
from xkcd_images import get_random_url_filename
from vk_image_uploading import vk_server_upload_image
from vk_image_uploading import vk_group_wall_upload_image


def main():
    load_dotenv()
    vk_token = os.environ['VK_KEY']
    group_id = os.environ['VK_GROUP_ID']
    vk_api_version = os.environ['VK_API_VERSION']

    url_comic, comic_name = get_random_url_filename()

    try:
        message = get_random_comic(url_comic, comic_name)
        image_owner_id = vk_server_upload_image(
            vk_token, group_id, vk_api_version, comic_name
        )

        attachment = f"photo{image_owner_id.get('response')[0].get('owner_id')}_" \
                     f"{image_owner_id.get('response')[0].get('id')}"
        vk_group_wall_upload_image(
            vk_token, group_id, vk_api_version, attachment, message
        )
    except ValueError:
        print("Error occured!")
    finally:
        os.remove(comic_name)


if __name__ == '__main__':
    main()
