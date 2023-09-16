from peewee import SqliteDatabase, Model, CharField, DateField

from database.hashing import hash_password, check_password

from paths import paths

# Путь к файлу базы данных
db_path = paths.database_file


# Создание объекта базы данных
db = SqliteDatabase(db_path)


# Определение модели пользователя
class User(Model):
    username = CharField(unique=True)
    password = CharField()
    full_name = CharField()  # Полное имя
    birthdate = DateField()  # Дата рождения
    birthplace = CharField()  # Место рождения
    phone_number = CharField()  # Номер телефона

    class Meta:
        database = db

    @staticmethod
    def register(username, password, full_name, birthdate, birthplace, phone_number):
        try:
            hashed_password = hash_password(password)  # Используем функцию для хеширования

            with db.atomic():
                User.create(
                    username=username,
                    password=hashed_password,
                    full_name=full_name,
                    birthdate=birthdate,
                    birthplace=birthplace,
                    phone_number=phone_number
                )

            return True  # Успешная регистрация
        except Exception as e:
            return False  # Ошибка регистрации

    @staticmethod
    def change_password(username, new_password):
        try:
            hashed_password = hash_password(new_password)  # Используем функцию для хеширования

            with db.atomic():
                user = User.get(User.username == username)
                user.password = hashed_password  # Обновляем пароль
                user.save()

            return True  # Успешное изменение пароля
        except Exception as e:
            return False  # Ошибка изменения пароля

    @staticmethod
    def authenticate(username, password):
        try:
            user = User.get(User.username == username)
            if check_password(password, user.password):  # Используем функцию для проверки пароля
                return user
        except User.DoesNotExist:
            pass

        return None

    @staticmethod
    def clear_database():
        try:
            with db.atomic():
                User.delete().execute()
            print("Все данные из базы данных удалены.")
        except Exception as e:
            print("Ошибка при удалении данных из базы данных.")

    @staticmethod
    def get_all_users():
        try:
            users = User.select()
            for user in users:
                print(f"Логин: {user.username}, Пароль (хэш): {user.password}")
        except Exception as e:
            print("Ошибка при получении пользователей из базы данных.")


# Функция для инициализации базы данных и таблицы пользователей
def initialize_database():
    db.connect()
    db.create_tables([User], safe=True)
