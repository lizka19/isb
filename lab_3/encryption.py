from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


class Encryptor:


    @staticmethod
    def encrypt_symmetric_key(sym_key: bytes, public_key) -> bytes:
        """
        Шифрует симметричный ключ с использованием RSA публичного ключа.

        :param sym_key: Симметричный ключ для шифрования в виде bytes
        :param public_key: Публичный RSA ключ
        :return: Зашифрованный симметричный ключ в виде bytes
        """

        encrypted_key = public_key.encrypt(
            sym_key,
            rsa_padding.OAEP(
                mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encrypted_key


    @staticmethod
    def decrypt_symmetric_key(encrypted_key: bytes, private_key: RSAPrivateKey) -> bytes:
        """
         Дешифрует симметричный ключ с использованием RSA приватного ключа.

        :param encrypted_key: Зашифрованный симметричный ключ в виде bytes
        :param private_key: Приватный RSA ключ
        :return: Расшифрованный симметричный ключ в виде bytes
        """

        return private_key.decrypt(
            encrypted_key,
            rsa_padding.OAEP(
                mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

