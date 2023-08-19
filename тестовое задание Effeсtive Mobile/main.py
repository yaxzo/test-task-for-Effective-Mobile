import argparse
import os.path
from json.decoder import JSONDecodeError

from pprint import pprint

import colorama

from scripts.create_json_file import create_json_file
from scripts.add_contact import add_contact
from scripts.search_contact import search_contact
from scripts.edit_contact import edit_contact_info
from scripts.page_output import get_contacts_page


colorama.init() # инициализация colorama, для цветной командной строки

''' ОБЪЯВЛЕНИЕ КОНСТАНТ '''
DEFAULT_FILE_PATH = "data/contacts.json" # путь к файлу по умолчанию


''' СОЗДАНИЕ ОБЪЕКТА ПАРСЕРА И ДОБАВЛЕНИЕ АРГУМЕНТОВ '''
# создаём парсер аргументов командной строки
argparser: object = argparse.ArgumentParser()

# добавляем аргументы
argparser.add_argument("-s", # аргумент для добавления фамилии
                       "--surname",
                       type=str,
                       dest="surname",
                       help="Добавляет фамилию контакта. "
                       "Обязательной аргумент.",)

argparser.add_argument("-n", # аргумент для добавления имени
                       "--name",
                       type=str,
                       dest="name",
                       help="Добавляет имя контакта. "
                       "Обязательный аргумент.",)

argparser.add_argument("-p", # аргумент для добавления отчества
                       "--patronymic",
                       type=str,
                       default=None,
                       dest="patronymic",
                       help="Добавляет отчество контакта. "
                       "Необязательный аргумент.",)

argparser.add_argument("-o", # аргумент для добавления организации
                       "--organization",
                       type=str,
                       dest="organization",
                       help="Добавляет значение организации контакта. "
                       "Обязательный аргумент.",) 


argparser.add_argument("-ppn", # аргумент для добавления личного номера
                       "--personalphone",
                       type=str,
                       dest="personal_phone_number",
                       help="Добавляет личный (сотовый) номер телефона контакта. "
                       "Обязателный аргумент.",)

argparser.add_argument("-wpn", # аргумент для добавления рабочего номера
                       "--workphone",
                       type=str,
                       dest="work_phone_number",
                       default=None,
                       help="Добавляет значение рабочего номера контакта. "
                       "По умолчанию - личный номер телефона.",)

argparser.add_argument("-i", # аргумент id для изменения/поиска контакта
                       "--id",
                       type=int,
                       dest="id",
                       help="Параметр id контакта. Используется только для поиска или изменения контакта",)

argparser.add_argument("-pg", # аргумент для вывода определённой страницы списка контактов
                       "--page",
                       dest="page",
                       type=int,
                       help='Открывает определённую "страницу" списка контактов.',)

argparser.add_argument("-a", # аргумент-флаг для создания контакта
                       "--add",
                       action="store_true",
                       dest="add",
                       help="Необязательный аргумент, который указывает на то, что контакт записывают в справочник.",)

argparser.add_argument("-sc", # аргумент-флаг для поиска контакта
                       "--search",
                       action="store_true",
                       dest="search_contact",
                       help="Аргумент, который указывает на то, что контакта ищут по критериям. ",)

argparser.add_argument("-ec", # аргумент-флаг для изменения контакта
                       "--edit",
                       action="store_true",
                       dest="edit_contact",
                       help="Аргумент, который указывает на то, что контакт изменяют.",)


args = argparser.parse_args() # парсим аргументы из командной строки


''' ОСНОВНАЯ РАБОТА ПРОГРАММЫ '''

def check_file_exists(file_path: str) -> bool:
    # проверяем сущетсвует ли данный файл
    return os.path.exists(file_path)


def get_data_from_parser() -> list: # создаём список с информацией из парсера
    return [ # создание списка с данными контакта
            args.surname,
            args.name,
            args.patronymic,
            args.organization,
            args.personal_phone_number,
            args.work_phone_number,
            args.id,
        ]


def main() -> None:
    ''' ФУНКЦИЯ РАБОТЫ ВСЕЙ ПРОГРАММЫЙ '''
    if not check_file_exists(DEFAULT_FILE_PATH):
        ''' ЕСЛИ ФАЙЛА НЕ СУЩЕСТВУЕТ, ТО СОЗДАЁМ ЕГО '''
        create_json_file()
        print(colorama.Fore.GREEN + "Файл с контактами был создан!")
    
    ''' РЕАЛИЗАЦИЯ РАБОТЫ С ДАННЫМИ ИЗ СТРОКИ '''

    ''' БЛОК ЛОГИКИ ДОБАВЛЕНИЯ КОНТАКТА '''
    if args.add: # если передан флаг add (-a или -add), создаём контакт.
        print(colorama.Fore.YELLOW + "Добавляю нового человека в контакты...")

        contact_data: list = get_data_from_parser() # передаём данные из парсера в виде списка.

        ''' если файл слетел или удалился, что бы не было ошибки - создаётся новый '''
        try: 
            if add_contact(contact_data):
                print(colorama.Fore.GREEN + "Контакт записан в справочник!")
        except JSONDecodeError:
            create_json_file()

            if add_contact(contact_data):
                print(colorama.Fore.GREEN + "Контакт записан в справочник!")

        ''' БЛОК ЛОГИКИ ПОИСКА КОНТАКТА '''

    elif args.search_contact: # если передан флаг search_contact (-sc или --searchcontact), ищем контакт.
        print(colorama.Fore.LIGHTYELLOW_EX + "Начинаю поиск контакта...")

        search_context_data: list = get_data_from_parser() # передаём данные из парсера в виде списка.
        contacts_we_looking_for = search_contact(search_context_data)

        try:
            if len(contacts_we_looking_for) > 1: # если контактов > 1, пишем во множественном числе.

                print(colorama.Fore.GREEN + "Найдены подходящие контакты...")
                print(colorama.Fore.GREEN + "Информация о контактах:")

                for i in range(len(contacts_we_looking_for)): # проходимся по каждому контакту.
                    contacts = contacts_we_looking_for[i]

                    print()
                    print(colorama.Fore.GREEN + f"{contacts['id']} {contacts['surname']} {contacts['name']} {contacts['patronymic']} {contacts['organization']} "
                        f"{contacts['personal phone number']} {contacts['work phone number']}")

            elif len(contacts_we_looking_for) == 1: # если контакт ровно 1, пишем в единственном.
                print(colorama.Fore.GREEN + "Подходящий контакт найден!")
                print(colorama.Fore.GREEN + "Информация о контакте:")

                contacts = contacts_we_looking_for[0] # получаем словарь.

                # красивый вывод.
                print()
                print(colorama.Fore.GREEN + f"ID: {contacts['id']}")
                print(colorama.Fore.GREEN + f"Фамилия: {contacts['surname']}")
                print(colorama.Fore.GREEN + f"Имя: {contacts['name']}")
                print(colorama.Fore.GREEN + f"Отчество: {contacts['patronymic']}")
                print(colorama.Fore.GREEN + f"Организация: {contacts['organization']}")
                print(colorama.Fore.GREEN + f"Личный номер телефона: {contacts['personal phone number']}")
                print(colorama.Fore.GREEN + f"Рабочий номер телефона: {contacts['work phone number']}")
            else: # если контактов нет, то так и пишем.
                print(colorama.Fore.RED + "Контакт не найден.")
        except JSONDecodeError:
            print(colorama.Fore.RED + "Ошибка. Файла с контактами не существует.")
            print(colorama.Fore.RED + "Контакт не найден.")

        ''' БЛОК ЛОГИКИ ИЗМЕНЕНИЯ КОНТАКТА '''
    elif args.edit_contact: # если передан флаг edit_contact (-ec или --editcontact), изменяем контакт.
        print(colorama.Fore.BLUE + "Информация для изменения получена...")
        contacts_info_to_change = get_data_from_parser()

        if edit_contact_info(contacts_info_to_change):
            print(colorama.Fore.GREEN + "Контакт успешно изменён!")
        else:
            print(colorama.Fore.RED + "Не удалось изменить контакт.")
            
        ''' БЛОК ЛОГИКИ ВЫВОДА СТРАНИЦЫ СПИСКА '''
    elif args.page:
        page = args.page

        contacts = get_contacts_page(page) # получаем контакты со страницы

        if contacts:
            for i, contact in enumerate(contacts, start=page*10-9): # проходимся по контактам
                print(colorama.Fore.GREEN + f"{i}. " f"{contact['surname']} {contact['name']} {contact['patronymic']} {contact['organization']} "
                        f"{contact['personal phone number']} {contact['work phone number']}") # красиво выводим


if __name__ == "__main__":
    main() # запускаем программу
