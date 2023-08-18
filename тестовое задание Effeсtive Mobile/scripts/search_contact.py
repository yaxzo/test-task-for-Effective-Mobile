import json


def search_contact(search_context: list) -> list:
    if search_context.count(None) == 7: # первый критерий отбора
        return [False] # если все значения в списке - None, то возвращаем False
    
    contacts_info = [] # список, в котором будет храниться информация о контакте

    context = set([x for x in search_context if x is not None]) # удаляем все None и делаем множество из списка

    with open("data/contacts.json", "r", encoding="UTF-8") as contacts_file: # открываем файл для поиска
        contacts = json.load(contacts_file)

        for contact_id in range(len(contacts["contacts"])): # индекс контакта
            analyzed_contact = set(contacts["contacts"][contact_id].values()) # получаем контакт, который анализируем сейчас 
                                                                              # и делаем множество из его значений

            ''' Если пересечение == длине наших критериев БЕЗ None, то контакт похож на тот, что мы ищем '''
            if len(context.intersection(analyzed_contact)) == len(context):
                contacts_info.append(analyzed_contact)

    return contacts_info
