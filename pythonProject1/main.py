import sys
import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from qq import Ui_Form as MainMenu
from qqq import Ui_Form as AddForm
from untitled import Ui_Form as WelcomeForm
from ww import Ui_Form as CalculateForm


class MainApplication:
    def __init__(self):
        # Создаем приложение
        self.app = QApplication(sys.argv)

        # Инициализация окон
        self.main_menu_widget = QWidget()
        self.add_form_widget = QWidget()
        self.welcome_form_widget = QWidget()
        self.calculate_form_widget = QWidget()

        # Настройка окон
        self.main_menu = MainMenu()
        self.main_menu.setupUi(self.main_menu_widget)
        self.main_menu_widget.resize(600, 400)  # Устанавливаем новый размер главного окна

        self.add_form = AddForm()
        self.add_form.setupUi(self.add_form_widget)

        self.welcome_form = WelcomeForm()
        self.welcome_form.setupUi(self.welcome_form_widget)

        self.calculate_form = CalculateForm()
        self.calculate_form.setupUi(self.calculate_form_widget)

        # Подключение базы данных
        self.db_connection = self.connect_to_database()
        self.db_cursor = self.db_connection.cursor()

        # Убедимся, что таблицы созданы
        self.setup_database()

        # Подключение кнопок к действиям
        self.setup_connections()

    def connect_to_database(self):
        """Устанавливает соединение с базой данных MySQL."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                port="3306",
                database="staff_schedule"
            )
            if connection.is_connected():
                print("Успешно подключено к базе данных MySQL")
            return connection
        except Error as e:
            QMessageBox.critical(None, "Ошибка подключения", f"Не удалось подключиться к базе данных: {e}")
            sys.exit()

    def setup_database(self):
        """Создает таблицы, если их нет."""
        create_departments_query = """
        CREATE TABLE IF NOT EXISTS Departments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            type VARCHAR(100),
            hazard_bonus_percent FLOAT NOT NULL
        )
        """
        create_positions_query = """
        CREATE TABLE IF NOT EXISTS Positions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            salary FLOAT NOT NULL,
            overtime_bonus_percent FLOAT NOT NULL,
            department_id INT,
            FOREIGN KEY (department_id) REFERENCES Departments(id)
        )
        """
        self.db_cursor.execute(create_departments_query)
        self.db_cursor.execute(create_positions_query)
        self.db_connection.commit()

    def setup_connections(self):
        # Кнопки в WelcomeForm
        self.welcome_form.pushButton.clicked.connect(self.show_main_menu)  # Вход
        self.welcome_form.pushButton_2.clicked.connect(self.exit_app)  # Выход

        # Кнопки в MainMenu
        self.main_menu.pushButton.clicked.connect(self.show_add_form)  # Добавить
        self.main_menu.pushButton_2.clicked.connect(self.show_calculate_form)  # Рассчитать
        self.main_menu.pushButton_3.clicked.connect(self.show_welcome_form)  # Назад

        # Кнопки в AddForm
        self.add_form.pushButton.clicked.connect(self.show_main_menu)  # Назад
        self.add_form.pushButton_2.clicked.connect(self.add_data)  # Добавить данные

        # Кнопки в CalculateForm
        self.calculate_form.pushButton.clicked.connect(self.show_main_menu)  # Назад
        self.calculate_form.pushButton_2.clicked.connect(self.calculate_data)  # Рассчитать

    def show_main_menu(self):
        self.main_menu_widget.show()
        self.add_form_widget.hide()
        self.welcome_form_widget.hide()
        self.calculate_form_widget.hide()

    def show_add_form(self):
        self.main_menu_widget.hide()
        self.add_form_widget.show()

    def show_calculate_form(self):
        self.main_menu_widget.hide()
        self.calculate_form_widget.show()

    def show_welcome_form(self):
        self.main_menu_widget.hide()
        self.welcome_form_widget.show()

    def add_data(self):
        """Добавление данных в базу."""
        department_name = self.add_form.lineEdit.text()
        department_type = self.add_form.lineEdit_2.text()
        try:
            hazard_bonus_percent = float(self.add_form.lineEdit_3.text())
        except ValueError:
            QMessageBox.warning(self.add_form_widget, "Ошибка", "Введите числовое значение для процента надбавки.")
            return

        if not department_name:
            QMessageBox.warning(self.add_form_widget, "Ошибка", "Введите название отдела.")
            return

        try:
            self.db_cursor.execute("""
            INSERT INTO Departments (name, type, hazard_bonus_percent)
            VALUES (%s, %s, %s)
            """, (department_name, department_type, hazard_bonus_percent))
            self.db_connection.commit()
            QMessageBox.information(self.add_form_widget, "Успех", "Данные добавлены!")
        except Error as e:
            QMessageBox.critical(self.add_form_widget, "Ошибка", f"Не удалось добавить данные: {e}")

    def calculate_data(self):
        """Расчет данных из базы."""
        position_name = self.calculate_form.comboBox.currentText()

        query = """
        SELECT Positions.name, Positions.salary, Positions.overtime_bonus_percent, Departments.hazard_bonus_percent
        FROM Positions
        INNER JOIN Departments ON Positions.department_id = Departments.id
        WHERE Positions.name = %s
        """
        self.db_cursor.execute(query, (position_name,))
        results = self.db_cursor.fetchall()

        if not results:
            QMessageBox.information(self.calculate_form_widget, "Информация", "Нет данных для выбранной должности.")
            return

        message = "Результаты расчета:\n"
        for row in results:
            name, salary, overtime_bonus, hazard_bonus = row
            total_salary = salary + salary * (overtime_bonus / 100) + salary * (hazard_bonus / 100)
            message += f"{name}: {total_salary:.2f} руб.\n"

        QMessageBox.information(self.calculate_form_widget, "Расчет", message)

    def exit_app(self):
        self.db_connection.close()
        sys.exit()

    def run(self):
        # Показать окно приветствия
        self.welcome_form_widget.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = MainApplication()
    app.run()
