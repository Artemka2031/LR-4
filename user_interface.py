import getpass
import re
from database.database import User
from file_operations import read_info_file

def is_valid_password(password):
    # Пароль должен иметь длину 5 символов и состоять только из цифр и знаков арифметических операций
    return bool(re.match(r'^[0-9\+\-\*/]{5}$', password))


def register_user():
    while True:
        username = input("Введите логин: ")
        password = getpass.getpass("Введите пароль: ")  # Скрытие пароля при вводе

        # Проверка пароля на соответствие требованиям
        if not is_valid_password(password):
            print("Ошибка регистрации. Пароль должен состоять из 5 символов, включая цифры и знаки арифметических "
                  "операций.")
            change_password = input("Хотите ввести новый пароль? (yes/no): ")
            if change_password.lower() == "yes":
                continue
            else:
                return

        full_name = input("Введите полное имя: ")
        birthdate = input("Введите дату рождения: ")
        birthplace = input("Введите место рождения: ")
        phone_number = input("Введите номер телефона: ")

        if User.register(username, password, full_name, birthdate, birthplace, phone_number):
            print("Регистрация успешна.")
            break  # Выход из цикла, если регистрация успешна
        else:
            print("Ошибка регистрации. Возможно, пользователь с таким логином уже существует.")


def login_user():
    username = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")

    user = User.authenticate(username, password)
    if user:
        print("Авторизация успешна.")
        show_menu(user)  # После успешной авторизации показываем меню
    else:
        print("Ошибка авторизации. Пожалуйста, проверьте логин и пароль.")


def main_menu():
    while True:
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")
        choice = input("Выберите действие: ")

        menu_options = {
            '1': register_user,
            '2': login_user,
            '3': exit_menu,
        }

        if choice in menu_options:
            menu_options[choice]()
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")


def show_menu(user):
    menu = {
        '1': open_file,
        '2': lambda: change_password(user),
        '3': logout,
        '4': exit_menu
    }

    while True:
        print("1. Открыть файл")
        print("2. Изменить пароль")
        print("3. Выйти из аккаунта")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice in menu:
            menu[choice]()
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")


def open_file():
    content = read_info_file()
    if content:
        print("Содержимое файла:")
        print(content)
    else:
        print("Ошибка при чтении файла.")


def has_repeating_characters(password):
    # Проверяем, есть ли повторяющиеся символы в пароле
    return len(password) == len(set(password))


def change_password(user):
    new_password = getpass.getpass("Введите новый пароль: ")

    # Проверяем новый пароль на наличие повторяющихся символов
    if not has_repeating_characters(new_password):
        print("Ошибка при изменении пароля. Пароль не должен содержать повторяющиеся символы.")
        return

    if User.change_password(user.username, new_password):
        print("Пароль успешно изменен.")
    else:
        print("Ошибка при изменении пароля.")


def logout():
    print("Выход из аккаунта.")
    main_menu()  # Возврат в главное меню после выхода из аккаунта


def exit_menu():
    print("Выход из меню.")
    exit()
