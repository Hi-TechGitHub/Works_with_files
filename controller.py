import main
from main import *
def controller():
    open_file = input("Открыть файл?: да, нет: ")
    if open_file == "да":
        main.open_phone_book()
    show_phone_book = input("Хотите увидеть тел. книгу?: да, нет: ")
    if show_phone_book == "да":
        main.show_phone_book()
    accept_add_contact = input("Добавить контакт?: да, нет: ")
    if accept_add_contact == "да":
        main.add_phone_book()
        main.save_phone_book()
    accept_edit_contact = input("Открыть хотите изменить контакт?: да, нет: ")
    if accept_edit_contact == "да":
        change_phone_book()
        save_phone_book()
    accept_search_contact = input("Хотите найти контакт?: да, нет: ")
    if accept_search_contact == "да":
        main.search_phone_book()
    accept_delete_contact = input("Хотите удалить контакт?: да, нет: ")
    if accept_delete_contact == "да":
        delete_phone_book()


controller()