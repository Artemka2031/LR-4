from database import User, initialize_database
from user_interface import register_user, login_user


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

def drop_db():
    drop = User.drop_table()

    if drop:
        print("База данных  удалена")
    else:
        print("Ошибка при удалении базы данных")

def show_db():
    users = User.get_all_users()

    if users:
        print(users)
    else:
        print("Нет пользователей")


if __name__ == "__main__":
    main()