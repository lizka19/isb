import json
from typing import Optional


class FileHandler:
    @staticmethod
    def save_encrypted_symmetric_key(encrypted_key: bytes, path: str) -> None:
        """
        Сохраняет зашифрованный симметричный ключ в файл.

        :param encrypted_key: Зашифрованный симметричный ключ в бинарном формате.
        :param path: Путь для сохранения файла.
        :return: None
        """
        try:
            with open(path, "wb") as file:
                file.write(encrypted_key)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Указанный путь не существует: {path}") from e
        except PermissionError as e:
            raise PermissionError(f"Нет прав на запись в указанное место: {path}") from e
        except IOError as e:
            raise IOError(f"Ошибка ввода/вывода при сохранении ключа: {str(e)}") from e

    @staticmethod
    def read_file(filename: str) -> bytes:
        """
        Читает данные из файла.

        :param filename: Путь к файлу для чтения.
        :return: Содержимое файла в бинарном формате.
        """
        try:
            with open(filename, "rb") as file:
                return file.read()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл не найден: {filename}") from e
        except PermissionError as e:
            raise PermissionError(f"Нет прав на чтение файла: {filename}") from e
        except IOError as e:
            raise IOError(f"Ошибка ввода/вывода при чтении файла: {str(e)}") from e

    @staticmethod
    def write_to_file(filename: str, data: bytes) -> None:
        """
        Записывает данные в файл.

        :param filename: Путь к файлу для записи.
        :param data: Данные для записи в бинарном формате.
        :return: None
        """
        try:
            with open(filename, 'wb') as f:
                f.write(data)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Указанный путь не существует: {filename}") from e
        except PermissionError as e:
            raise PermissionError(f"Нет прав на запись в файл: {filename}") from e
        except IOError as e:
            raise IOError(f"Ошибка ввода/вывода при записи в файл: {str(e)}") from e

    @staticmethod
    def load_settings(filename: str) -> Optional[dict]:
        """
        Загружает настройки из JSON-файла.

        :param filename: Путь к JSON-файлу с настройками.
        :return: Словарь с настройками или None в случае ошибки.
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл настроек не найден: {filename}") from e
        except PermissionError as e:
            raise PermissionError(f"Нет прав на чтение файла настроек: {filename}") from e
        except IOError as e:
            raise IOError(f"Ошибка ввода/вывода при чтении настроек: {str(e)}") from e