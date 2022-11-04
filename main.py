import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_Ellipse(qp)
        qp.end()

    def paint(self):
        self.repaint()

    def draw_Ellipse(self, qp):
        self.x = randint(0, 500)
        self.y = randint(0, 500)
        self.size = randint(0, 250)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.x, self.y, self.size, self.size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())