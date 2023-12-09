"""
СЕМИНАР 8. РАБОТА С ФАЙЛАМИ
"""

"""
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from PYLes8files1 import print_contacts, add_contact, copy_contact, delete_contact

CONTACTS = 'Contacts.txt'
COPIED_CONTACTS = 'Copied_contacts.txt'

def interface():
    while True:    
        print('Выберете действие:\
            \n 1 - Добавить контакт \
            \n 2 - Вывести все контакты \
            \n 3 - Скопировать контакт \
            \n 4 - Удалить контакт  \
            \n 0 - Выйти')
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contact(CONTACTS)
            case 2:
                print_contacts(CONTACTS)  
            case 3:
                copy_contact(CONTACTS, COPIED_CONTACTS)
            case 4:
                delete_contact(CONTACTS)   
            
if __name__ == '__main__':
    interface()