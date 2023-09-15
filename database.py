from peewee import SqliteDatabase, Model, CharField, DateField
import bcrypt

# Путь к файлу базы данных
db_path = 'data/Users.db'

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
            # Хэширование пароля перед сохранением в базу данных
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            with db.atomic():
                User.create(
                    username=username,
                    password=hashed_password.decode('utf-8'),  # Сохраняем хэшированный пароль
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
            # Хэширование нового пароля
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

            with db.atomic():
                user = User.get(User.username == username)
                user.password = hashed_password.decode('utf-8')  # Обновляем пароль
                user.save()

            return True  # Успешное изменение пароля
        except Exception as e:
            return False  # Ошибка изменения пароля

    @staticmethod
    def authenticate(username, password):
        try:
            user = User.get(User.username == username)
            # Проверка хэшированного пароля
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return user  # Возвращаем объект пользователя при успешной аутентификации
        except User.DoesNotExist:
            pass  # Пользователь не найден

        return None  # Неудачная аутентификация

# Функция для инициализации базы данных и таблицы пользователей
def initialize_database():
    db.connect()
    db.create_tables([User], safe=True)