import sys
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit, QRadioButton, QCheckBox, QLabel, \
    QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from random import randint

class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.count = 0
        self.run()

    def run(self):
        self.pushButton.clicked.connect(self.work)

    def work(self, value):
        self.update()    

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.count != 0:
            self.circles(qp)
        qp.end()
        self.count = 1


    def circles(self, qp):
        qp.setBrush(QColor("yellow"))
        qp.setPen(QColor("yellow"))
        x = randint(0, self.width())
        y = randint(0, self.height())
        size = randint(0, self.height() // 2)
        qp.drawEllipse(x, y, size, size)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())