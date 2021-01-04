import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Управление НЛО')
        self.pixmap = QPixmap('UFO.png').scaled(150, 150)
        self.image = QLabel(self)
        self.image.resize(150, 150)
        self.x = 0
        self.y = 0
        self.image.move(self.x, self.y)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.y = (self.y + 50) % 500
        elif event.key() == Qt.Key_Up:
            self.y = (self.y + 450) % 500
        elif event.key() == Qt.Key_Right:
            self.x = (self.x + 50) % 500
        elif event.key() == Qt.Key_Left:
            self.x = (self.x + 450) % 500
        self.image.move(self.x, self.y)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())