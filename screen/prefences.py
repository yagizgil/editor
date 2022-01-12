from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os 

import ui_data
import ui_lang

class ExtPref(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(80,80)
        self.setObjectName("preffr")
        v = QVBoxLayout()
        
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setObjectName("preflogo")
        
        self.logo.resize(50,50)
        
        self.lbl = QLabel("python")
        self.lbl.setObjectName("preflbl")
        self.lbl.setAlignment(Qt.AlignCenter)
        
        v.addWidget(self.logo)
        v.addWidget(self.lbl)
        
        self.setLayout(v)
        
    def setFile(self,file):
        ud = ui_data.file_icons
        ul = ui_lang.screen_project_text
        
        ext = os.path.split(file)[1].split(".")[1]
        if ext == "py":
            pix = QPixmap(ud["python-logo"])
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("python")
        
        elif ext == "css":
            pix = QPixmap(ud["css-logo"])
            pix = pix.scaled(QSize(29,29))
            self.logo.setPixmap(pix)
            self.lbl.setText("css")
            
        elif ext == "html":
            pix = QPixmap(ud["html-logo"])
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("html")
        
        elif ext == "c":
            pix = QPixmap(ud["c-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("c")
        
        elif ext == "cpp":
            pix = QPixmap(ud["cpp-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("c++")
        
        elif ext == "cs":
            pix = QPixmap(ud["cs-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("c-sharp")
        
        elif ext == "h":
            pix = QPixmap(ud["h-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("header")
        
        elif ext == "exe":
            pix = QPixmap(ud["exe-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("executable")
            
        elif ext == "java" or ext == "jar":
            pix = QPixmap(ud["java-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.open.setVisible(False)
        
        elif ext in ["db","sql","dbs"]:
            pix = QPixmap(ud["database-logo"])
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("database")
            
        elif ext == "json":
            pix = QPixmap(ud["json-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("json")
        
        elif ext == "xml":
            pix = QPixmap(ud["xml-logo"])
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("xml")
        
        elif ext == "txt":
            pix = QPixmap(ud["txt-logo"])
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("text")
        
        elif ext in ["png","jpg","gif","tiff"]:
            pix = QPixmap(ud["image-logo"])
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText(ul["p-image"])
        
        else:
            pix = QPixmap(ud["script-logo"])
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText(ul["p-private"])
            
        
class SizePref(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(80,80)
        self.setObjectName("preffr")
        v = QVBoxLayout()
        
        self.size = QLabel()
        self.size.setAlignment(Qt.AlignCenter)
        self.size.setObjectName("sizelbl")

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        
        v.addWidget(self.size)
        v.addWidget(self.lbl)
        
        self.setLayout(v)
    
    
    def setFile(self,file):
        s = ConvertSize(os.path.getsize(file))
        s = s.get()
        
        try:
            self.size.setText(str(s[0])[0:5])
        except:
            self.size.setText(str(s[0]))
            
        self.lbl.setText(s[1])


class ConvertSize():
    l = list()
    def __init__(self,b):
        self.l.clear()
        if b < 1024:
            self.l.append(b)
            self.l.append('b')

        elif b >= 1024 and b < 1048576:
            self.l.append(b/1024)
            self.l.append('kb')
        
        elif b >= 1048576 and b < 1073741824:
            self.l.append(b/1024/1024)
            self.l.append('mb')
            
        elif b >= 1073741824 and b < 1099511627776:
            self.l.append(b/1024/1024/1024)
            self.l.append('gb')

    def get(self):
        return self.l


