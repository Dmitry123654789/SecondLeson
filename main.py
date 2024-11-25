import io
import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="draw">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>91</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class NoTSquare(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.flag = False
        self.color = QColor(255, 255, 0)
        self.draw.clicked.connect(self.drawed)

    def paintEvent(self, event):
        if not self.flag:
            return
        qp = QPainter(self)
        qp.begin(self)
        qp.setPen(self.color)
        qp.setBrush(self.color)
        r = randint(0, 200)
        qp.drawEllipse(randint(0, 500 - r), randint(0, 500 - r), r, r)
        qp.end()
        self.flag = False

    def drawed(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoTSquare()
    ex.show()
    sys.exit(app.exec())
