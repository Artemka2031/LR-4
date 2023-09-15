def create_info_file():
    try:
        with open('data/text.txt', 'w') as file:
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
    try:
        with open('data/text.txt', 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return None  # Ошибка чтения файла
