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

