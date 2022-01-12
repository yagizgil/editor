from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from qt_material import apply_stylesheet

import menu as m
import screen as s


class Window(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setUI()

    def setUI(self):
        w = QWidget()
        v = QVBoxLayout()
        
        self.menu_bar = m.Menu2(self)
        self.screen = s.Screen()
        
        #v.addWidget(self.menu_bar)
        v.addWidget(self.screen)
        
        w.setLayout(v)
        self.setCentralWidget(w)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    w = Window(app)
    w.show()
    sys.exit(app.exec())
