def calculate_frequence(text: str) -> dict:
    """
    Вычисляет частоту символов в тексте.
    :param text: Входной текст.
    :return: Словарь соответствия символов их частоте в тексте.
    """
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
    """
    Сопоставляет символы зашифрованного текста с русскими символами по частоте.
    :param encrypt_frequence: Словарь частот символов из зашифрованного текста.
    :param rus_frequence: Словарь ожидаемых частот русских символов.
    :return: Словарь соответствия зашифрованных символов русским символам.
    """
    if not encrypt_frequence or not rus_frequence:
        raise ValueError("Input dictionaries cannot be empty.")

    encrypt_rus_dict = {}

    encrypt_frequence_list = list(encrypt_frequence.items())
    rus_frequence_list = list(rus_frequence.items())

    for i in range(min(len(rus_frequence), len(encrypt_frequence))):

        encrypt_rus_dict[encrypt_frequence_list[i][0]] = rus_frequence_list[i][0]

    return encrypt_rus_dict


def decrypt_text(encrypted_text: str, d: dict) -> str:
    """
    Расшифровывает текст с использованием соответствия символов.
    :param encrypted_text: Зашифрованный текст.
    :param d: Словарь соответствия зашифрованных символов расшифрованным.
    :return: Расшифрованный текст.
    """
    if not encrypted_text:
        raise ValueError("Encrypted text can't be empty.")

    if not d:
        raise ValueError("Dictionary cannot be empty.")

    decrypted_text = []

    for symbol in encrypted_text:

        if symbol in d:
            decrypted_text.append(d[symbol])

        else:
            decrypted_text.append(symbol)

    return ''.join(decrypted_text)

