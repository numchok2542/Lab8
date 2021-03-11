import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Simple Drawing')
        self.rabbit = QPixmap('images/Pekora.png')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(70, 100), QPoint(100, 110),
                        QPoint(130, 100), QPoint(100, 150)])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        #p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon(
            [QPoint(0, 85), QPoint(75, 75), QPoint(100, 10),
            QPoint(125, 75), QPoint(200, 85), QPoint(150, 125),
            QPoint(160, 190), QPoint(100, 150), QPoint(40, 190),
            QPoint(50, 125), QPoint(0, 85),]
        )

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
