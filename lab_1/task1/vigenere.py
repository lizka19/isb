from const import ALPHABET

def is_valid_char(char: str) -> bool:
    
    return char.lower() in ALPHABET

def get_key_symbol(key: str, index: int) -> str:
    
    if not key:
        raise ValueError("Key can't be empty!")
    return key[index % len(key)]

def get_encrypted_symbol(old_symbol: str, key_symbol: str) -> str:

    if not old_symbol.isalpha() or not is_valid_char(old_symbol) or not is_valid_char(key_symbol):
        return old_symbol

    try:
        current_idx = ALPHABET.index(old_symbol.lower())
        key_idx = ALPHABET.index(key_symbol.lower())
    except ValueError:
        return old_symbol

    encrypt_idx = (current_idx + key_idx) % len(ALPHABET)

    return ALPHABET[encrypt_idx].upper() if old_symbol.isupper() else ALPHABET[encrypt_idx]


def vigenere_cipher_encrypt(input_text: str, key: str) -> str:
    
    if not input_text:
        raise ValueError("Input text can't be empty")
    if not key:
        raise ValueError("Key can't be empty")


    clean_key = ''.join(c for c in key if is_valid_char(c))
    if not clean_key:
        raise ValueError("Key must contain at least one valid character from the alphabet")

    encrypted_text = []
    for i in range(len(input_text)):
        text_symbol = input_text[i]
        key_symbol = get_key_symbol(clean_key, i)
        encrypted_text.append(get_encrypted_symbol(text_symbol, key_symbol))

    return ''.join(encrypted_text)


def get_decrypted_symbol(encrypted_symbol: str, key_sym: str) -> str:
    if not encrypted_symbol.isalpha() or not is_valid_char(encrypted_symbol) or not is_valid_char(key_sym):
        return encrypted_symbol

    try:
        encrypted_idx = ALPHABET.index(encrypted_symbol.lower())
        key_idx = ALPHABET.index(key_sym.lower())
    except ValueError:
        return encrypted_symbol

    decrypted_idx = (encrypted_idx - key_idx) % len(ALPHABET)
    return ALPHABET[decrypted_idx].upper() if encrypted_symbol.isupper() else ALPHABET[decrypted_idx]


def vigenere_cipher_decrypt(encrypted_text: str, key: str) -> str:
    if not encrypted_text:
        raise ValueError("Encrypted text can't be empty")
    if not key:
        raise ValueError("Key can't be empty")

    clean_key = ''.join(c for c in key if is_valid_char(c))
    if not clean_key:
        raise ValueError("Key must contain at least one valid character from the alphabet")

    decrypted_text = []
    for i in range(len(encrypted_text)):
        encrypted_symbol = encrypted_text[i]
        key_symbol = get_key_symbol(clean_key, i)
        decrypted_text.append(get_decrypted_symbol(encrypted_symbol, key_symbol))

    return ''.join(decrypted_text)