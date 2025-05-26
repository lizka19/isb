import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from file_work import FileHandler

class SymmetricKey:

    @staticmethod 
    def get_key_length() -> int:
        """
        Запрашивает у пользователя ввод корректной длины ключа Blowfish.
        :return: Корректная длина ключа от 32 до 448 бит (включительно), кратная 8.
        """

        while True:
            try:
                key_length = int(input("Введите длину симметричного ключа: "))
                if 32 <= key_length <= 448 and key_length % 8 == 0:
                    return key_length
                else:
                    print("Blowfish key length must be between 32 and 448 bits, in 8-bit steps.")
            except ValueError:
                print("Ошибка: введите целое число!")

    @staticmethod
    def generate_symmetric_key(key_length: int) -> bytes:
        """
        Генерирует случайный симметричный ключ заданной длины.
        :param key_length: Длина ключа в битах.
        :return: Сгенерированный симметричный ключ.
        """
        key = os.urandom(key_length // 8)
        return key

class AsymmetricKey:

    @staticmethod
    def generate_assymmetric_key() -> tuple:
        """
        Генерирует пару RSA ключей (приватный и публичный).
        :return: Кортеж (приватный_ключ, публичный_ключ) в виде объектов RSA.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_private_key(private_key: rsa.RSAPrivateKey, filename: str) -> None:
        """
        Сериализует и сохраняет приватный RSA ключ.
        :param private_key: Приватный ключ для сохранения.
        :param filename: Путь для сохранения ключа.
        :return: None
        """
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        FileHandler.write_to_file(filename, pem)

    @staticmethod
    def serialize_public_key(public_key: rsa.RSAPublicKey, filename: str) -> None:
        """
        Сериализует и сохраняет публичный RSA ключ.
        :param public_key: Публичный ключ для сохранения.
        :param filename: Путь для сохранения ключа.
        :return: None
        """
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        FileHandler.write_to_file(filename, pem)

    @staticmethod
    def load_private_key(path: str) -> RSAPrivateKey:
        """
        Загружает приватный RSA ключ из файла.
        :param path: Путь к файлу с приватным ключом.
        :return: Загруженный приватный ключ.
        """
        key_data = FileHandler.read_file(path)
        return serialization.load_pem_private_key(
            key_data,
            password=None
        )