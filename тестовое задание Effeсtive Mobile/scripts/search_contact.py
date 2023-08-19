import json


def search_contact(search_context: list[str | int | None]) -> list:
    '''
    ФУНКЦИЯ ДЛЯ ПОИСКА КОНТАКТА ИСХОДЯ ИЗ КОНТЕКСТА ЗАПРОСА 

    Подробное описание работы функции описано в пояснительной записке
    Ссылка: https://github.com/yaxzo/test-task-for-Effective-Mobile/blob/main/пояснительная%20записка.md

    Возвращает False, если в списке нет контекста для поиска 
    Возвращает список contacts_info, в котором храняться все контакты, подходящие по критериям
    
    '''
    if search_context.count(None) == 7: # первый критерий отбора
        return [False] # если все значения в списке - None, то возвращаем False
    
    contacts_info = [] # список, в котором будет храниться информация о контакте

    context = set([x for x in search_context if x is not None]) # удаляем все None и делаем множество из списка

    with open("data/contacts.json", "r+", encoding="UTF-8") as contacts_file: # открываем файл для поиска
        contacts = json.load(contacts_file)

        for contact_id in range(len(contacts["contacts"])): # индекс контакта
            contacts["contacts"][contact_id]["id"] = contact_id # добавляем id в словарь, нужно для изменения и поиска контакта
            analyzed_contact = contacts["contacts"][contact_id] # получаем контакт, который анализируем сейчас 
                                                                            
            # делаем множество из значений словаря и оставляем словарь контакта, для красивого вывода в дальнейшем
            set_analyzed_contact = set(analyzed_contact.values())
            
            ''' Если пересечение == длине наших критериев БЕЗ None, то контакт похож на тот, что мы ищем '''
            if len(context.intersection(set_analyzed_contact)) == len(context):
                contacts_info.append(analyzed_contact)
    contacts_file.close()

    return contacts_info
