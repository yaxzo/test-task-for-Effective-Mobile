import json

import colorama


def edit_contact_info(info_to_change: list) -> bool:
    '''
    ФУНКЦИЯ ДЛЯ ИЗМЕНЕНИЯ КОНТАКТА

    Для изменения контакта надо обязательно передать id контакта,
    который можно узнать через поиск (-sc или --searchcontact флаг).

    Возвращаем True, если контакт изменён.
    Возвращаем False, если нет информации для изменения контакта.
    '''
    if info_to_change.count(None) == 7 or info_to_change[-1] == None: # если все поля пустые или нет id контакта
        return False
    
    with open("data/contacts.json", "r", encoding="UTF-8") as contacts_json: # открываем файл на чтение и запись
        contacts: dict = json.load(contacts_json) # получаем контакты

    try:
        with open("data/contacts.json", "w", encoding="UTF-8") as contacts_json:
            contact_id: int = info_to_change[-1] # получаем id изменяемого контакта

            editing_contact: dict = contacts["contacts"][contact_id] # получаем изменяемый контакт

            '''
            Понимаю, что это не самая лучшая реализация изменения контакта, но не знаю как сделать по-другому.
            Если значение для изменения != None, то заменяем значение, если == None, то оставляем всё как было.
            '''
            contacts["contacts"][contact_id]["surname"] = info_to_change[0] if info_to_change[0] != None \
                                                                                    else editing_contact["surname"]
            
            contacts["contacts"][contact_id]["name"] = info_to_change[1] if info_to_change[1] != None \
                                                                                    else editing_contact["name"]
            
            contacts["contacts"][contact_id]["patronymic"] = info_to_change[2] if info_to_change[2] != None \
                                                                                    else editing_contact["patronymic"]
            
            contacts["contacts"][contact_id]["organization"] = info_to_change[3] if info_to_change[3] != None \
                                                                                    else editing_contact["organization"]
            
            contacts["contacts"][contact_id]["personal phone number"] = info_to_change[4] if info_to_change[4] != None \
                                                                                    else editing_contact["personal phone number"]
            
            contacts["contacts"][contact_id]["work phone number"] = info_to_change[5] if info_to_change[5] != None \
                                                                                    else editing_contact["work phone number"]
            
            contacts_json.write(json.dumps(contacts, ensure_ascii=False, indent=2)) # записываем всю новую инф-ю в файл
        contacts_json.close()
    except IndexError: # если такого индекса не существует, то так и пишем.
        print(colorama.Fore.RED + "Нет контакта с таким id.")
        return False

    return True
