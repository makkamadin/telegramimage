from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from utils import *
import config
import time


def main():
    with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        while True:
            timee = round(time.time())
            if timee % 60 == 0:
                print(1)
                time.sleep(5)
                (H, M) = (int(time.strftime("%H", time.gmtime())), time.strftime("%M", time.gmtime()))
                current_time = "{}:{}".format(H+3, M)
                generate_image(current_time)
                image = client.upload_file('time.jpg')
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(image))


if __name__ == '__main__':
    main()
