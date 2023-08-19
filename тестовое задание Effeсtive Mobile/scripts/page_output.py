import json


def get_contacts_page(page_number: int) -> list[dict]:
    '''
    ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ КОНТАКТОВ С ОПРЕДЕЛЁННОЙ СТРАНИЦЫ СПРАВОЧНИКА
    
    Возвращает contacts_to_output, список со словарями подходящих контактов 
    '''
    CONTACTS_PER_PAGE: int = 10 # константа, сколько контактов может быть на странице
    index: int = page_number * CONTACTS_PER_PAGE # индекс для нахождения страницы
    contacts_to_output = [] # список контактов для вывода в дальнейшем

    with open("data/contacts.json", "r", encoding="UTF-8") as contacts_json: # открываем файл JSON
        contacts = json.load(contacts_json)

    contacts_for_page: dict = contacts["contacts"] # раскрываем словарь

    for _, suitable_contacts in enumerate(contacts_for_page[index-10:index]): # проходимся по нужным контактам
        contacts_to_output.append(suitable_contacts) # записываем нужные контакты в словарь

    return contacts_to_output
