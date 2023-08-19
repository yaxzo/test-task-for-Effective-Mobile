import json


def add_contact(contact_info: list[str | int | None]) -> bool:
    '''
    ФУНКЦИЯ ДЛЯ ДОБАВЛЕНИЯ КОНТАКТА В СПРАВОЧНИК

    Сначала собираем все данные в словарь,
    после чего добавляем новые данные уже в существующий JSON файл.

    Возвращает True, как флаг о том, что контакт создан и мы можем продолжить работу
    '''
    with open("data/contacts.json", "r", encoding="UTF-8") as contacts_file: # открываем файл для получения данных
        contacts = json.load(contacts_file) # получаем все данные из файла

        new_contact_info: dict = { # собираем информацию о контакте
                "surname": contact_info[0],
                "name": contact_info[1],
                # если фамилии нет, то ставиться прочерк
                "patronymic": "-" if contact_info[2] == None else contact_info[2],
                "organization": contact_info[3],
                "personal phone number": contact_info[4],
                # если рабочий номер не указан, то рабочим номером становиться личный номер
                "work phone number": contact_info[4] if contact_info[5] is None else contact_info[5],
            }

        contacts["contacts"].append(new_contact_info) # записываем новые данные

        with open("data/contacts.json", "w", encoding="UTF-8") as contacts_json: # открываем файл на запись
            json.dump(contacts, contacts_json, ensure_ascii=False, indent=2) # добавляем новые данные
    
    contacts_file.close()
    contacts_json.close()

    return True
