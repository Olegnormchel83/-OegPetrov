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

CONTACTS = 'Contacts.txt'


def print_contacts(file_name):
    line_number = 1
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()  
        print(" |  №  |     Имя        Телефон   ")
        if len(all_cont) != 0:
            for line in all_cont:
                print(" | ", line_number, " | ", line.strip(), end = '\n\n') 
                line_number += 1
        else:
            print('Список контактов пустой')    
    
def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 89659679681): ')
    cont_info = input()
    return cont_info

def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:    
        file.writelines(all_cont)
        
def copy_contact(file_name, new_file_name):
    print("Список контактов: ")
    print_contacts(CONTACTS)
    print("Выберите строку, которую хотите перенсти в другой файл: ")
    copy_line_num = int(input())
    copy_line = ' '
    
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        for i in range(len(all_cont)):
            if i == copy_line_num - 1:
                copy_line = all_cont[i]
            
    print(f"Выбрана строка {copy_line_num} {copy_line}")
    
    with open(new_file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    all_cont.append('\n' + copy_line)

    with open(new_file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)
    print(f"Выбранная строка скопирована в Copied_contacts!")    
    