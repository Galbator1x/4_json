import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    filepath = input('Введите путь до файла: ')
    pretty_print_json(load_data(filepath))
