import json
import argparse
from argparse import Namespace
import sys
from vigenere import *


def parser() -> Namespace:
    """
    Парсер аргументов командной строки
    :return: Распарсенные аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_text', type=str, help='Имя файла с исходным текстом')
    parser.add_argument('output_text', type=str, help='Имя файла для сохранения результата')
    parser.add_argument('key', type=str, help='JSON-файл с ключом шифрования')
    return parser.parse_args()


def read_key_from_json(filename: str) -> str:
    """
    Чтение ключа из JSON-файла
    :param filename: Путь к JSON-файлу с ключом
    :return: Ключ шифрования
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, str):
                raise ValueError("Ключ должен быть строкой")
            return data
    except FileNotFoundError:
        print(f"Файл ключа '{filename}' не найден.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка формата JSON в файле '{filename}'")
        sys.exit(1)


def read_text(filename: str) -> str:
    """
    Функция чтения текста из файла
    :param filename: Путь к файлу для чтения
    :return: Прочитанный текст
    """
    try:
        with open(filename, 'r', encoding='utf-8') as text:
            return text.read()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        sys.exit(1)


def write_encrypted_text(filename: str, text: str) -> None:
    """
    Функция записи текста в файл
    :param filename: Путь к файлу для записи
    :param text: Текст для сохранения
    :return: None
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Ошибка записи в файл '{filename}': {e}")
        sys.exit(1)


def main():
    args = parser()

    key = read_key_from_json(args.key)

    input_text = read_text(args.input_text)
    encrypted_text = vigenere_cipher_encrypt(input_text, key)

    write_encrypted_text(args.output_text, encrypted_text)


if __name__ == "__main__":
    main()