import json


def create_json_file() -> bool:
    '''
    ФУНКЦИЯ ДЛЯ СОЗДАНИЯ ПУСТОГО JSON ФАЙЛА, ЕСЛИ ЕГО НЕТ В ПАПКЕ И СОЗДАНИЕ ПАПКИ, ЕСЛИ ЕЁ НЕТ

    Добавляет в JSON файл "тело", что бы не вызывалась ошибка,
    потому что с вообще пустым JSON файлом работать невозможно.

    Возвращает True, как флаг о том, что мы создали папку с файлом или файл и можем продолжить работу
    '''
    try:
        file_body: dict = {"contacts": []}

        with open("data/contacts.json", "w") as create_file: # открываем файл для чтения
            # создаём JSON файл, это нужно что бы работать с ним в дальнейшем
            json.dump(file_body, create_file, indent=2)
        create_file.close()
    except FileNotFoundError: # если папки не существует, то создаём её и снова вызываем функцию с созданием файла
        import os
        os.mkdir("data")
        create_json_file()

    return True
