import random

class Cipher:
    CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__ (self, key):
        self.key = key


class ShiftCipher (Cipher):
    ENCRYPT = 1
    DECRYPT = -1

    def __init__ (self, key):
        super().__init__(key)

    def _convert(self, message, shift_direc = 0):
        message = message.upper()
        converted_message = ''
        for character in message:
            if character in Cipher.CHARACTERS:
                char_ind = (Cipher.CHARACTERS.find(character) + self.key * shift_direc) % len(Cipher.CHARACTERS)
                converted_message += Cipher.CHARACTERS[char_ind]
            else:
                converted_message += character
        return converted_message

    def encrypt(self, message):
        return self._convert(message, shift_direc = ShiftCipher.ENCRYPT)

    def decrypt(self, message):
        return self._convert(message, shift_direc = ShiftCipher.DECRYPT)


class CaesarCipher (ShiftCipher):
    def __init__(self):
        super().__init__(3)

class MonoalphabeticCipher(Cipher):
    def __init__ (self, key = None):
        super().__init__(key)
        if self.key is None:
            self._set_random_key()

    def _convert(self, message, src_str, replacement_str):
        message = message.upper()
        converted_msg = ''
        for charac in message:
            if charac in Cipher.CHARACTERS:
                converted_msg += replacement_str[src_str.index(charac)]
            else:
                converted_msg += charac
        return converted_msg

    def encrypt(self, message):
        return self._convert(message, Cipher.CHARACTERS, self.key)

    def decrypt(self, message):
        return self._convert(message, self.key, Cipher.CHARACTERS)
    
    def _set_random_key(self):
        char_lst = list(Cipher.CHARACTERS)
        random.shuffle(char_lst)
        self.key = ''.join(char_lst)

if __name__ == '__main__':
    m = " welcome to ethical hacking"
    print("\n-----CAESAR CIPHER-----")
    caesar_cipher = CaesarCipher()
    e_m = caesar_cipher.encrypt(m)
    print("\nEncrypted message:")
    print(e_m)
    print("\nDecrypted message: ")
    print(caesar_cipher.decrypt(e_m))

    print("\n-----MONOALPHABETIC CIPHER-----")
    monoalph_cipher = MonoalphabeticCipher()
    e_m = monoalph_cipher.encrypt(m)
    print("\nEncrypted message:")
    print(e_m)
    print("\nDecrypted message: ")
    print(monoalph_cipher.decrypt(e_m))



