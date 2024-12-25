from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setMinimumSize(QSize(413, 320))
        Form.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        Form.setStyleSheet(u"color: rgb(255, 170, 255);\n"
"font: 11pt \"Sans Serif Collection\";\n"
"text-decoration: underline;\n"
"background-color: rgb(149, 87, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 150, 141, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 80, 141, 31))
        self.label.setTextFormat(Qt.AutoText)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 220, 141, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

