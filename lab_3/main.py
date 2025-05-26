import argparse

from keygeneration import SymmetricKey, AsymmetricKey
from encryption import Encryptor
from decryption import Decryptor
from file_work import FileHandler


def genereate_keys(settings: dict):
    """
    Генерирует симметричные и асимметричные ключи,
    шифрует симметричный ключ и сохраняет все ключи.

    :param settings: Словарь с путями к файлам
    :return: None
    """

    print("====Режим генерации ключей====")

    key_length = SymmetricKey.get_key_length()
    sym_key = SymmetricKey.generate_symmetric_key(key_length)
    print("Симметричный ключ успешно сгененрирован.")

    private_key, public_key = AsymmetricKey.generate_assymmetric_key()
    print("Асимметричная пара ключей успешно сгенерирована.")

    AsymmetricKey.serialize_private_key(private_key, settings['private_key'])
    AsymmetricKey.serialize_public_key(public_key, settings['public_key'])

    encrypted_symmetric_key = Encryptor.encrypt_symmetric_key(sym_key, public_key)
    FileHandler.save_encrypted_symmetric_key(encrypted_symmetric_key,
                                              settings['encrypted_symmetric_key'])

    print("Ключи успешно сгенерированы!")

def encrypt_mode(settings: dict):
    """
    Дешифрует симметричный ключ с помощью приватного ключа,
    шифрует текст алгоритмом Blowfish и сохраняет результат.
    """
    print("====Режим шифрования====")

    encrypted_symmetric_key = FileHandler.read_file(settings['encrypted_symmetric_key'])  # Изменено
    private_key = AsymmetricKey.load_private_key(settings['private_key'])
    symmetric_key = Encryptor.decrypt_symmetric_key(encrypted_symmetric_key, private_key)

    text = FileHandler.read_file(settings['plaintext'])
    encrypted_text = Encryptor.encrypt_text(text, symmetric_key)

    FileHandler.write_to_file(settings['encrypted_text'], encrypted_text)
    print("Текст был успешно зашифрован и сохранен в файл!")


def decrypt_mode(settings: dict):
    """
    Дешифрует симметричный ключ с помощью RSA
    и дешифрует текст алгоритмом Blowfish.
    """
    print("====Режим дешифрования====")

    encrypted_symmetric_key = FileHandler.read_file(settings['encrypted_symmetric_key'])  # Изменено
    private_key = AsymmetricKey.load_private_key(settings['private_key'])

    symmetric_key = Encryptor.decrypt_symmetric_key(encrypted_symmetric_key, private_key)
    encrypted_text = FileHandler.read_file(settings['encrypted_text'])

    decrypted_text = Decryptor.decrypt_text(encrypted_text, symmetric_key)
    FileHandler.write_to_file(settings['decrypted_text'], decrypted_text)
    print("Текст был успешно расшифрован и сохранен в файл!")


def main():

    parser = argparse.ArgumentParser(description="ГИБРИДНАЯ КРИПТОСИСТЕМА")
    parser.add_argument('-s', '--settings', default='settings.json',
                        help='Путь к JSON-файлу, содержащий настройки')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Режим генерации ключей', action='store_true')
    group.add_argument('-enc', '--encryption', help='Режим шифрования', action='store_true')
    group.add_argument('-dec', '--decryption', help='Режим дешифрования', action='store_true')

    args = parser.parse_args()

    settings = FileHandler.load_settings(args.settings)

    match True:
        case args.generation:
            genereate_keys(settings)
        case args.encryption:
            encrypt_mode(settings)
        case args.decryption:
            decrypt_mode(settings)



if __name__ == "__main__":
    main()