from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import ui_data, ui_lang

class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.setMaximumHeight(50)
        
        self.setUI()


    def setUI(self):
        h = QHBoxLayout()
        
        
        self.new_file = QPushButton()
        self.new_file.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.open_file = QPushButton()
        self.open_file.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.save_file = QPushButton()
        self.save_file.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.color_palette = QPushButton()
        self.color_palette.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.settings = QPushButton()
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        
        h.addWidget(self.new_file)
        h.addWidget(self.open_file)
        h.addWidget(self.save_file)
        
        h.addStretch()
        
        h.addWidget(self.color_palette)
        h.addWidget(self.settings)
        
        self.setUI_dl()
        
        self.setLayout(h)
    
    def setUI_dl(self):
        ud = ui_data.menu_buttons_icons
        ul = ui_lang.menu_buttons_text
        
        self.new_file.setIcon(QIcon(ud["new-file"]))
        self.new_file.setText(ul["new-file"])
        
        self.open_file.setIcon(QIcon(ud["open-file"]))
        self.open_file.setText(ul["open-file"])
        
        self.save_file.setIcon(QIcon(ud["save-file"]))
        self.save_file.setText(ul["save-file"])
        
        self.color_palette.setIcon(QIcon(ud["color-palette"]))
        self.color_palette.setText(ul["color-palette"])
        
        self.settings.setIcon(QIcon(ud["settings"]))
        self.settings.setText(ul["settings"])


class Menu2():

    def __init__(self, me):
        self.me = me
        
        self.setUI()      

    def setUI(self):
        menu = QToolBar()
        self.me.addToolBar(Qt.LeftToolBarArea, menu)
        menu.setMovable(True)
        
        self.new_file = QAction(self.me)
        
        self.open_file = QAction(self.me)
        
        self.save_file = QAction(self.me)
        
        self.color_palette = QAction(self.me)
        
        self.settings = QAction(self.me)
        
        menu.addAction(self.new_file)
        menu.addAction(self.open_file)
        menu.addAction(self.save_file)
        menu.addSeparator()
        menu.addAction(self.color_palette)
        menu.addAction(self.settings)
        
        self.setUI_dl()
        
    
    def setUI_dl(self):
        ud = ui_data.menu_buttons_icons
        ul = ui_lang.menu_buttons_text
        
        self.new_file.setIcon(QIcon(ud["new-file"]))
        self.new_file.setText(ul["new-file"])
        
        self.open_file.setIcon(QIcon(ud["open-file"]))
        self.open_file.setText(ul["open-file"])
        
        self.save_file.setIcon(QIcon(ud["save-file"]))
        self.save_file.setText(ul["save-file"])
        
        self.color_palette.setIcon(QIcon(ud["color-palette"]))
        self.color_palette.setText(ul["color-palette"])
        
        self.settings.setIcon(QIcon(ud["settings"]))
        self.settings.setText(ul["settings"])

