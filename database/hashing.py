import bcrypt


def hash_password(password):
    # Хеширование пароля
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def check_password(plain_password, hashed_password):
    # Проверка пароля
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
