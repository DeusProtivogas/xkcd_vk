# XKCD comics uploader
A set of scripts that download XKCD comics and upload them to a Vkontakte group.

### Requirements
Python3 should be already installed. Requires libraries:
```
request
```
```
python-dotenv
```
Both can be installed by running
```
pip install -r requirements.txt
```

### Environment variables
- VK_KEY
- VK_GROUP_ID
- VK_API_VERSION

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

## Main script

Can be done by launching

```
python3 main.py
```

Obtains a random XKCD comics and uploads it to the Vkontakte group, specified by the variables. 

### xkcd_images.py

Gets comics from XKCD website and downloads it, provides the image and the description of the comics.

## vk_image_uploading

Scripts, responsible for work with VK api.

### vk_get_groups

Returns a list of groups the user is admin of.

### vk_server_upload_image

Uploads the downloaded image to VK server, to prepare it for future uploading to the group.

### vk_group_wall_upload_image

Posts the comics and its description to the group.

### check_vk_response

Checks responses from VK api for errors, raises exceptions if any found.