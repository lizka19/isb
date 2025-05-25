import json


class FileHandler:

    @staticmethod
    def save_encrypted_symmetric_key(encrypted_key: bytes, path: str) -> None:
        """
        Сохраняет зашифрованный симметричный ключ в файл.

        :param encrypted_key: Зашифрованный симметричный ключ в бинарном формате.
        :param path: Путь для сохранения файла.
        :return: None
        """

        with open(path, "wb") as file:
            file.write(encrypted_key)


    @staticmethod
    def read_file(filename: str) -> bytes:
        """
        Читает данные из файла.

        :param filename: Путь к файлу для чтения.
        :return: Содержимое файла в бинарном формате.
        """

        with open(filename, "rb") as file:
            return file.read()


    def write_to_file(filename: str, data: bytes) -> None:
        """
         Записывает данные в файл.

        :param filename: Путь к файлу для записи.
        :param data: Данные для записи в бинарном формате.
        :return: None
        """

        with open(filename, 'wb') as f:
            f.write(data)


    @staticmethod
    def load_settings(filename: str) -> dict:
        """
        Загружает настройки из JSON-файла.

        :param filename: Путь к JSON-файлу с настройками.
        :return: Словарь с настройками.
        """

        with open(filename, 'r') as f:
            return json.load(f)
