class ImageObfuscation(object):
    @staticmethod
    def encode_image(img, msg):
        """
        use the red portion of an image (r, g, b) tuple to
        hide the msg string characters as ASCII values
        red value of the first pixel is used for length of string
        """
        length = len(msg)
        # limit length of message to 255
        if length > 255:
            print("text too long! (don't exceed 255 characters)")
            return False
        # image needs to be in colors
        if img.mode != 'RGB':
            print("image mode needs to be RGB")
            return False
        # use a copy of image to hide the text in
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                # first value is length of msg
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index - 1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g, b))
                index += 1
        return encoded

    @staticmethod
    def decode_image(img):
        """
        check the red portion of an image (r, g, b) tuple for
        hidden message characters (ASCII values)
        """
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    r, g, b, a = img.getpixel((col, row))
                # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    msg += chr(r)
                index += 1
        return msg
