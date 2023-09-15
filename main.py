from database import User, initialize_database
import getpass

def main():
    initialize_database()

    while True:
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

def register_user():
    username = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")  # Скрытие пароля ввода
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

if __name__ == "__main__":
    main()