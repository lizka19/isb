from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Decryptor:

    @staticmethod
    def unpadding(padded_data: bytes) -> bytes:
        """
        Удаляет PKCS7-дополнение из расшифрованных данных.

        :param padded_data: Расшифрованные данные с дополнением.
        :return: Оригинальные данные без дополнения.
        :raises ValueError: Если дополнение некорректное.
        """

        unpadder = sym_padding.PKCS7(algorithms.Blowfish.block_size).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()


    @staticmethod
    def decrypt_text(encrypted_text: bytes, key: bytes) -> bytes:
        """
        Дешифрует текст с использованием алгоритма Blowfish в режиме ECB.

        :param encrypted_text: Зашифрованный текст в байтах.
        :param key: Симметричный ключ для дешифрования.
        :return: Расшифрованный текст без дополнения.
        """

        cipher = Cipher(algorithms.Blowfish(key), modes.ECB())
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(encrypted_text) + decryptor.finalize()
        return Decryptor.unpadding(decrypted_padded)
