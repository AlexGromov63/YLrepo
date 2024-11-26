import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QColor, QPen, QPainter
from PyQt6.QtCore import QPointF
from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 445)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 180, 201, 41))
        self.pushButton.setStyleSheet("background-color: #ffffff")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Create yellow circle"))


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.show()
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.radius = randint(10, int(min([self.size().width(), self.size().height()]) / 2))
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            cordsX = sorted([self.radius, self.size().width() - self.radius])
            cordsY = sorted([self.radius, self.size().height() - self.radius])
            pen = QPen(self.color)
            pain = QPainter(self)
            pain.setPen(pen)
            pain.drawEllipse(QPointF(randint(cordsX[0], cordsX[1]), 
                                     randint(cordsY[0], cordsY[1])), self.radius, self.radius)
        self.flag = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())