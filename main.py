import sys
from random import randint
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QColor, QPen, QPainter
from PyQt6.QtCore import QPointF


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.flag = False
        self.show()
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.radius = randint(10, int(min([self.size().width(), self.size().height()]) / 2))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            cordsX = sorted([self.radius, self.size().width() - self.radius])
            cordsY = sorted([self.radius, self.size().height() - self.radius])
            pen = QPen(QColor(255, 255, 0))
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