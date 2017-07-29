from PIL import Image
import pickle
import os

from encryption.symetric_encryption import SymetricEncryption
from Steganography.imageobfuscation import ImageObfuscation
from encryption.rsa_encryption import RSAEncryption

ORIGINAL_IMAGE_FILE_PATH = "example_images"
IMAGE_NAME = "mario.png"


class TestHideAndEncrypt(object):
    def __init__(self):
        super(TestHideAndEncrypt, self).__init__()
        self._rsa_encryption = RSAEncryption()
        self._symetric_encryption = SymetricEncryption()

    def encode_text_and_encrypt_rsa(self):
        img = Image.open(os.path.join(ORIGINAL_IMAGE_FILE_PATH, IMAGE_NAME))
        # image mode needs to be 'RGB'
        print(img, img.mode)  # test
        # create a new filename for the modified/encoded image
        encoded_image_file_name = "enc_" + IMAGE_NAME
        # don't exceed 255 characters in the message
        secret_message = "this is a secret message added to the image"
#        print(len(secret_msg))  # test
        img_encoded = ImageObfuscation.encode_image(img, secret_message)
        if img_encoded:
            # save the image with the hidden text
            img_encoded.save(os.path.join("encoded_images", encoded_image_file_name))
            print("{} saved!".format(IMAGE_NAME))
        encoded_image_file_name = os.path.join("encoded_images", encoded_image_file_name)
        with open(encoded_image_file_name, "rb") as decrypted_image, open(encoded_image_file_name + r".rsa", "wb") as rsa_image:
            image_data = decrypted_image.read()
            pickle.dump(self._rsa_encryption.encrypt(image_data), rsa_image)
        os.remove(encoded_image_file_name)

    def decrypt_image_and_decode_text_rsa(self):
        for encoded_file in os.listdir("encoded_images"):
            encoded_file = os.path.join("encoded_images", encoded_file)
            with open(encoded_file, "rb") as encrypted_image, open(encoded_file[:-4], "wb") as decrypted_image:
                image_data = pickle.load(encrypted_image)
                decrypted_image.write(self._rsa_encryption.decrypt(image_data))
            os.remove(encoded_file)

        for encoded_file in os.listdir("encoded_images"):
            encoded_image = Image.open(os.path.join("encoded_images", encoded_file))
            hidden_text = ImageObfuscation.decode_image(encoded_image)
            print("File name: {file_name}\tHidden text:\n{h_text}".format(file_name=encoded_file, h_text=hidden_text))

    def encode_text_and_encrypt_symetric(self):
        img = Image.open(os.path.join(ORIGINAL_IMAGE_FILE_PATH, IMAGE_NAME))
        # image mode needs to be 'RGB'
        print(img, img.mode)  # test
        # create a new filename for the modified/encoded image
        encoded_image_file_name = "enc_" + IMAGE_NAME
        # don't exceed 255 characters in the message
        secret_message = "this is a secret message added to the image"
#        print(len(secret_msg))  # test
        img_encoded = ImageObfuscation.encode_image(img, secret_message)
        if img_encoded:
            # save the image with the hidden text
            img_encoded.save(os.path.join("encoded_images", encoded_image_file_name))
            print("{} saved!".format(IMAGE_NAME))
        encoded_image_file_name = os.path.join("encoded_images", encoded_image_file_name)
        with open(encoded_image_file_name, "rb") as decrypted_image, open(encoded_image_file_name + r".rsa", "wb") as rsa_image:
            image_data = decrypted_image.read()
            pickle.dump(self._symetric_encryption.encrypt(image_data), rsa_image)
        os.remove(encoded_image_file_name)

    def decrypt_image_and_decode_text_symetric(self):
        for encoded_file in os.listdir("encoded_images"):
            encoded_file = os.path.join("encoded_images", encoded_file)
            with open(encoded_file, "rb") as encrypted_image, open(encoded_file[:-4], "wb") as decrypted_image:
                image_data = pickle.load(encrypted_image)
                decrypted_image.write(self._symetric_encryption.decrypt(image_data))
            os.remove(encoded_file)

        for encoded_file in os.listdir("encoded_images"):
            encoded_image = Image.open(os.path.join("encoded_images", encoded_file))
            hidden_text = ImageObfuscation.decode_image(encoded_image)
            print("File name: {file_name}\tHidden text:\n{h_text}".format(file_name=encoded_file, h_text=hidden_text))
