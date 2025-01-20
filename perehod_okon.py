import sys
from turtledemo.clock import setup

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from qq import Ui_Form as MainMenu
from untitled import Ui_Form as WelcomeForm
class MainApplication:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.menu = QWidget()
        self.welcome = QWidget()

        self.main_menu = MainMenu()
        self.main_menu.setupUi(self.menu)
        self.menu.resize(500, 500)

        self.wlc = WelcomeForm()
        self.wlc.setupUi(self.welcome)

        self.ass()

    def ass(self):
        self.wlc.pushButton.clicked.connect(self.z)
        self.wlc.pushButton_2.clicked.connect(self.vihod)

    def z(self):
        self.menu.show()

    def vihod(self):
        sys.exit()

    def run(self):
        self.welcome.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = MainApplication()
    app.run()
