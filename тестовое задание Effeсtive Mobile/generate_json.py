import random
import json


def generate_contacts(num_contacts: int) -> list[dict]:
    contacts = []
    for _ in range(num_contacts): # генерируем нужное количество контактов для примера
        contact = {
            "surname": generate_surname(),
            "name": generate_name(),
            "patronymic": generate_patronymic(),
            "organization": generate_organization(),
            "personal phone number": generate_phone_number(),
            "work phone number": generate_work_phone_number()
        }
        contacts.append(contact)
    return contacts

def generate_surname() -> str: # генерируем фамилию
    surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов"]
    return random.choice(surnames)

def generate_name() -> str: # генерируем имя
    names = ["Иван", "Петр", "Алексей", "Сергей", "Андрей"]
    return random.choice(names)

def generate_patronymic() -> str: # генерируем отчество
    patronymics = ["Иванович", "Петрович", "Алексеевич", "Сергеевич", "Андреевич"]
    return random.choice(patronymics)

def generate_organization() -> str: # генерируем организацию
    organizations = ["ООО_Рога_и_Копыта", "ЗАО_Синергия", "ИП_Иванов", "Газпром", "Яндекс", "EffectiveMobile"]
    return random.choice(organizations)

def generate_phone_number() -> str: # генерируем личный номер телефона
    return "+7" + ''.join(random.choice("0123456789") for _ in range(10))

def generate_work_phone_number() -> str: #
    if random.random() < 0.5:
        return "+7" + ''.join(random.choice("0123456789") for _ in range(10))
    return generate_phone_number()

contacts = generate_contacts(25) # генерируем 25 контактов

with open("data/contacts.json", "w", encoding="UTF-8") as contacts_json:
    json.dump(contacts, contacts_json, ensure_ascii=False, indent=4) # дамп контактов в список
