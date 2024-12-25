from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(376, 226)
        Form.setStyleSheet(u"color: rgb(255, 170, 255);\n"
"font: 6pt \"MS Shell Dlg 2\";\n"
"font: 11pt \"Sans Serif Collection\";\n"
"text-decoration: underline;\n"
"background-color: rgb(149, 87, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 160, 111, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 160, 111, 31))
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 20, 141, 21))
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(170, 60, 141, 21))
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(170, 100, 141, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 81, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 131, 31))
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 90, 131, 31))
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setWordWrap(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u043d\u0430\u0434\u0431\u0430\u0432\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u0434\u043d\u044b\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
    # retranslateUi

