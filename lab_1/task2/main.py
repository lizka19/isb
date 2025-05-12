import sys

sys.path.append(r'C:\Users\lizak\PycharmProjects\isb\lab_1')

from workfiles import *
from frequence_analysis import *


def main():
    const = read_json_file('consts.json')

    write_json_file(const['RUS_FREQ_JSON'], const['RUSSIAN_FREQ'])

    encrypted_text = read_text_file(const['ENCRYPTED_TEXT_TXT'])
    text_freq = calculate_frequence(encrypted_text)
    write_json_file(const['ENCRYPTED_FREQ_JSON'], text_freq)

    rus_dict = read_json_file(const['RUS_FREQ_JSON'])
    encrypt_dict = read_json_file(const['ENCRYPTED_FREQ_JSON'])
    encrypt_rus_dict = create_mapping(encrypt_dict, rus_dict)

    key = read_json_file(const['KEY_JSON'])
    decrypted_text = decrypt_text(encrypted_text, key)
    write_text_file(const['DECRYPTED_TEXT_TXT'], decrypted_text)


if __name__ == '__main__':
    main()