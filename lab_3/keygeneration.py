import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

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

                if key_length < 32 or key_length > 448 or key_length % 8 != 0:
                    print("Blowfish key length must be between 32 and 448 bits, in 8-bit steps.")

                else:
                    return key_length

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

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )


    @staticmethod
    def serialize_public_key(public_key: rsa.RSAPublicKey, filename: str) -> None:
        """
        Сериализует и сохраняет публичный RSA ключ.

        :param public_key: Публичный ключ для сохранения.
        :param filename: Путь для сохранения ключа.
        :return: None
        """

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "wb") as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )


    @staticmethod
    def load_private_key(path: str) -> RSAPrivateKey:
        """
        Загружает приватный RSA ключ из файла.

        :param path: Путь к файлу с приватным ключом.
        :return: Загруженный приватный ключ.
        """

        with open(path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )
        return private_key


    @staticmethod
    def load_encrypted_symmetric_key(path: str) -> bytes:
        """
        Загружает зашифрованный симметричный ключ из файла.

        :param path: Путь к файлу с зашифрованным ключом.
        :return: Зашифрованный симметричный ключ.
        """

        with open(path, "rb") as f:
            return f.read()
