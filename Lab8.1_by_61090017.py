import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class simple_drawing_window(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.setWindowTitle("Simple Drawing")
		self.rabbit = QPixmap("images/rabbit.png")
	
	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		
		p.setPen(QColor(0,0,0))
		p.setBrush(QColor(0,255,0))
		p.drawPolygon(
			[QPoint(100,100), QPoint(100,110), 
			QPoint(130, 100), QPoint(100,150),]
		)
		
		p.setPen(QColor(255,0,0))
		p.setBrush(QColor(255,0,0))
		p.drawPie(50,150,100,100,0,180 * 32)
		
		p.drawPixmap(QRect(200,100,320,320), self.rabbit)
		p.end()

def main():
	app = QApplication(sys.argv)

	w = simple_drawing_window()
	w.show()

	return app.exec_()

if __name__ == "__main__":
	sys.exit(main())