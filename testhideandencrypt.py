import os
from PIL import Image

from Steganography.imageobfuscation import ImageObfuscation

from Encryption.Encryption import Encryption

ORIGINAL_IMAGE_FILE_PATH = "example_images"
IMAGE_NAME = "mario.png"


class TestHideAndEncrypt(object):
    @staticmethod
    def encode_text_and_encrypt():
        img = Image.open(os.path.join(ORIGINAL_IMAGE_FILE_PATH, IMAGE_NAME))
        # image mode needs to be 'RGB'
        print(img, img.mode)  # test
        # create a new filename for the modified/encoded image
        encoded_image_file_name = "enc_" + IMAGE_NAME
        # don't exceed 255 characters in the message
        secret_msg = "this is a secret message added to the image"
        print(len(secret_msg))  # test
        img_encoded = ImageObfuscation.encode_image(img, secret_msg)
        if img_encoded:
            # save the image with the hidden text
            img_encoded.save(os.path.join("encoded_images", encoded_image_file_name))
            print("{} saved!".format(IMAGE_NAME))

        encryption = Encryption()
        # encryption.encrypt()  # enter encryption method here

    @staticmethod
    def decrypt_image_and_decode_text():
        for encoded_file in os.listdir("encoded_images"):
            encoded_image = Image.open(os.path.join("encoded_images", encoded_file))
            hidden_text = ImageObfuscation.decode_image(encoded_image)
            print("File name: {file_name}\tHidden text:\n{h_text}".format(file_name=encoded_file, h_text=hidden_text))
