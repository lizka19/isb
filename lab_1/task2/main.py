import sys
sys.path.append(r'C:\Users\lizak\PycharmProjects\isb\lab_1')
from workfiles import *
from frequence_analysis import *
import json


with open('consts.json', 'r', encoding='utf-8') as f:
    const = json.load(f)
RUSSIAN_FREQ = const['RUSSIAN_FREQ']
RUS_FREQ_JSON = const['RUS_FREQ_JSON']
ENCRYPTED_TEXT_TXT = const['ENCRYPTED_TEXT_TXT']
ENCRYPTED_FREQ_JSON = const['ENCRYPTED_FREQ_JSON']
KEY_JSON = const['KEY_JSON']
DECRYPTED_TEXT_TXT = const['DECRYPTED_TEXT_TXT']


def main():

    save_frequence_to_json(RUS_FREQ_JSON, RUSSIAN_FREQ)

    encrypted_text = read_text_file(ENCRYPTED_TEXT_TXT)

    text_freq = calculate_frequence(encrypted_text)

    save_frequence_to_json(ENCRYPTED_FREQ_JSON, text_freq)

    rus_dict = load_frequence_from_json(RUS_FREQ_JSON)
    encrypt_dict = load_frequence_from_json(ENCRYPTED_FREQ_JSON)

    encrypt_rus_dict = create_mapping(encrypt_dict, rus_dict)

    key = load_frequence_from_json(KEY_JSON)

    decrypted_text = decrypt_text(encrypted_text, key)

    write_text_file(DECRYPTED_TEXT_TXT, decrypted_text)


if __name__ == '__main__':
    main()