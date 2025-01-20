import sys
from dataclasses import dataclass
from turtledemo.clock import setup
import pymysql
from pymysql import MySQLError
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from mysql.connector import connect

from untitled import Ui_Form as MainMenu
from qq import Ui_Form as WelcomeMani

class WW:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.menu = QWidget()
        self.wlcm = QWidget()


        self.menu_widget = MainMenu()
        self.menu_widget.setupUi(self.menu)
        self.menu.resize(500, 500)

        self.welcome_witget = WelcomeMani()
        self.welcome_witget.setupUi(self.wlcm)

        self.realiz()

        self.db_connection = self.df_cnct()
        self.db_cursor = self.db_connection.cursor()

    def df_cnct(self):
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="root",  # Убедитесь, что добавлен пароль
                database="staff_schedule",
                charset="utf8mb4"
            )

            print("norm")
            return connection
        except MySQLError as e:
            print(e)
            sys.exit()

    def realiz(self):
        self.welcome_witget.pushButton.clicked.connect(self.z)
        self.welcome_witget.pushButton_2.clicked.connect(self.vhd)

    def z(self):
        self.menu.show()

    def vhd(self):
        self.db_connection.close()
        sys.exit()

    def run(self):
        self.wlcm.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = WW()
    app.run()
