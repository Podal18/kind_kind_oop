import sqlite3

class Database:
    def __init__(self, db_path):
        """Инициализация соединения с базой данных."""
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def fetch_all(self, query):
        """Выполнение запроса и возврат всех результатов."""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """Закрытие соединения."""
        self.connection.close()


class Worker:
    def __init__(self, db_path):
        """Инициализация класса Worker с доступом к базе данных."""
        self.db = Database(db_path)

    def get_all_workers(self):
        """Получение всех работников из таблицы."""
        query = "SELECT * FROM worker"
        return self.db.fetch_all(query)

    def close(self):
        """Закрытие соединения с базой данных."""
        self.db.close()


if __name__ == "__main__":
    db_path = 'C:\\sqlite3\\ydb.db'
    worker_manager = Worker(db_path)

    # Получение всех работников и вывод их на экран
    workers = worker_manager.get_all_workers()
    for worker in workers:
        print(worker)

    worker_manager.close()
