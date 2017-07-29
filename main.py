from testhideandencrypt import TestHideAndEncrypt
import os


def main():
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
