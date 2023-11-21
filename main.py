import os
from dotenv import load_dotenv
from xkcd_images import get_random_comics
from vk_image_uploading import vk_server_upload_image, \
    vk_group_wall_upload_image


def main():
    load_dotenv()
    vk_token = os.environ['VK_KEY']
    group_id = os.environ['VK_GROUP_ID']
    vk_api_version = os.environ['VK_API_VERSION']

    message, image_name = get_random_comics()
    image_data = vk_server_upload_image(
        vk_token, group_id, vk_api_version, image_name
    )

    attachment = f"photo{image_data.get('response')[0].get('owner_id')}_" \
                 f"{image_data.get('response')[0].get('id')}"
    vk_group_wall_upload_image(
        vk_token, group_id, vk_api_version, attachment, message
    )
    os.remove(image_name)


if __name__ == '__main__':
    main()
