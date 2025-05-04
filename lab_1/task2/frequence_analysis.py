import json

def save_frequence_to_json(filename: str, d: dict) -> None:

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(d, file, ensure_ascii=False)


def load_frequence_from_json(filename: str) -> dict:

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:

        print(f"File '{filename}' not found.")
        raise


def calculate_frequence(text: str) -> dict:
    if not text:
        raise ValueError("Input text can't be empty.")

    symbol_counts = {}

    for symbol in text:

        if symbol in symbol_counts:

            symbol_counts[symbol] += 1

        else:

            symbol_counts[symbol] = 1

    symbols_count = sum(symbol_counts.values())

    symbol_frequence = {}

    for char, count in symbol_counts.items():

        frequence = round(count / symbols_count, 6)

        symbol_frequence[char] = frequence

    sorted_frequence_list = sorted(symbol_frequence.items(), key=lambda item: item[1], reverse=True)

    sorted_freq = dict(sorted_frequence_list)

    return sorted_freq


def create_mapping(encrypt_frequence: dict, rus_frequence: dict) -> dict:

    if not encrypt_frequence or not rus_frequence:
        raise ValueError("Input dictionaries cannot be empty.")

    encrypt_rus_dict = {}

    encrypt_frequence_list = list(encrypt_frequence.items())
    rus_frequence_list = list(rus_frequence.items())

    for i in range(min(len(rus_frequence), len(encrypt_frequence))):

        encrypt_rus_dict[encrypt_frequence_list[i][0]] = rus_frequence_list[i][0]

    return encrypt_rus_dict


def decrypted_text(encrypted_text: str, d: dict) -> str:
    if not encrypted_text:
        raise ValueError("Encrypted text can't be empty.")

    if not d:
        raise ValueError("Dictionary cannot be empty.")

    decrypted_text = []

    for symb in encrypted_text:

        if symb in d:

            decrypted_text.append(d[symb])

        else:

            decrypted_text.append(symb)

    return ''.join(decrypted_text)

