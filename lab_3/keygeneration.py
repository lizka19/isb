import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

class SymmetricKey:

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

