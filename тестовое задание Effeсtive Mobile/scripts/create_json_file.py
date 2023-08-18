import json


def create_json_file() -> bool:
    file_body: dict = {"contacts": []}

    with open("data/contacts.json", "w") as create_file: # открываем файл для чтения
        # создаём JSON файл, это нужно что бы работать с ним в дальнейшем
        json.dump(file_body, create_file, indent=2)
    create_file.close()

    return True
