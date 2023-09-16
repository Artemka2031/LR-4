from pathlib import Path


class Paths:
    def __init__(self):
        self.data_dir = Path('data')
        self.info_file = self.data_dir / 'info.txt'
        self.database_file = self.data_dir / 'database.db'


# Создаем экземпляр класса Paths
paths = Paths()
