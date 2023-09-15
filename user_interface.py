import getpass
from database import User

def register_user():
    username = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")  # Скрытие пароля при вводе
    full_name = input("Введите полное имя: ")
    birthdate = input("Введите дату рождения: ")
    birthplace = input("Введите место рождения: ")
    phone_number = input("Введите номер телефона: ")

    if User.register(username, password, full_name, birthdate, birthplace, phone_number):
        print("Регистрация успешна.")
    else:
        print("Ошибка регистрации. Возможно, пользователь с таким логином уже существует.")

def login_user():
    username = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")

    user = User.authenticate(username, password)
    if user:
        print("Авторизация успешна.")
        # Здесь вы можете добавить логику для доступа к файлам и другим функциям после успешной авторизации
    else:
        print("Ошибка авторизации. Пожалуйста, проверьте логин и пароль.")
