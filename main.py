from encryption.symetric_encryption import SymetricEncryption
from Steganography.imageobfuscation import ImageObfuscation
from encryption.rsa_encryption import RSAEncryption
from testhideandencrypt import TestHideAndEncrypt

from tkFileDialog import askopenfilename
from Tkinter import Tk
from PIL import Image
import pickle
import os


def main():
    main_flow()


def choose_file():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def print_main_menu():
    print "\n\nWelcome! What would like to do?"
    print "\t1. Encrypt Message"
    print "\t2. Decrypt"
    print "\t3. Test"
    print "\t4. Exit"


def main_flow():
    while True:
        print_main_menu()
        choice = raw_input("Enter your choice: ")

        if choice == '1':
            encrypt()

        elif choice == '2':
            decrypt()

        elif choice == '3':
            test()

        elif choice == '4':
            break
        else:
            continue


def encrypt():
    message = raw_input("Enter Message: ")

    print "Choose image to obfuscate the message in it"
    image_path = choose_file()

    print "Choose encryption type"
    print "\t 1. RSA"
    print "\t 2. Symetric"
    while True:
        choice = raw_input("Enter your choice: ")
        if choice == '1':
            encryptor = RSAEncryption()
            break
        elif choice == '2':
            encryptor = SymetricEncryption()
            break
    encrypt_and_write_to_file(message, image_path, encryptor)


def encrypt_and_write_to_file(message, image_path, encryptor):
    image_data = Image.open(image_path)
    encoded_image = ImageObfuscation.encode_image(image_data, message)
    encoded_image_path = os.path.join("encoded_images",
                                      os.path.basename(image_path))
    encoded_image.save(encoded_image_path)
    with open(encoded_image_path, "rb") as decrypted_image, open(encoded_image_path + r".enc", "wb") as rsa_image:
        image_data = decrypted_image.read()
        pickle.dump((encryptor, encryptor.encrypt(image_data)), rsa_image)
        os.remove(encoded_image_path)


def decrypt():
    print "Choose Encrypted File:"
    file_path = choose_file()
    decrypted_file_path = file_path[:-4]
    with open(file_path, "rb") as encrypted_image, open(decrypted_file_path, "wb") as decrypted_image:
        encryptor, image_data = pickle.load(encrypted_image)
        decrypted_image.write(encryptor.decrypt(image_data))

    encoded_image = Image.open(decrypted_file_path)
    hidden_message = ImageObfuscation.decode_image(encoded_image)
    os.remove(decrypted_file_path)

    print "The Message is: %s" % (hidden_message, )


def test():
    for a_file in os.listdir("encoded_images"):
        os.remove(os.path.join("encoded_images", a_file))
    test_instance = TestHideAndEncrypt()
    test_instance.encode_text_and_encrypt_rsa()
    test_instance.decrypt_image_and_decode_text_rsa()
    for a_file in os.listdir("encoded_images"):
        os.remove(os.path.join("encoded_images", a_file))
    test_instance.encode_text_and_encrypt_symetric()
    test_instance.decrypt_image_and_decode_text_symetric()


if __name__ == "__main__":
    main()
