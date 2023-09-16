from paths import paths
from database.database import initialize_database


def create_info_file():
    info_file = paths.info_file

    try:
        with open(info_file, 'w') as file:
            file.write(
                "Аутентификация: Процесс проверки подлинности пользователя.\n"
                "Идентификация: Процесс определения личности пользователя.\n"
                "Авторизация: Процесс предоставления доступа после успешной аутентификации.\n"
                "Пароль: Секретная комбинация символов для доступа.\n"
                "Шифрование: Процесс защиты данных от несанкционированного доступа.\n"
            )
        return True  # Успешное создание файла
    except Exception as e:
        return False  # Ошибка создания файла


def read_info_file():
    info_file = paths.info_file
    try:
        with open(info_file, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return None  # Ошибка чтения файла


def create_database_file():
    try:
        initialize_database()
        return True
    except Exception as e:
        return False


def create_data_directory():
    data_dir = paths.data_dir
    if not data_dir.exists():
        data_dir.mkdir()

    # Вызываем функцию для создания файла 'text.txt'
    if not create_info_file():
        print("Ошибка при создании файла 'text.txt'")

    # Создаем файл 'database.db' внутри папки data, если его не существует
    if not create_database_file():
        print("Ошибка при создании файла 'database.db'")