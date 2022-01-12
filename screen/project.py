from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from screen.prefences import *

import ui_data
import ui_lang


import os

class ProjectArea(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        self.setUI()
        
    def setUI(self):
        v = QVBoxLayout()
        
        #Aç butonu  Proje başlığı ve listeleme butonu
        header_layout_h = QHBoxLayout()
        
        self.open_folder = QPushButton()
        self.open_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_folder.setFixedSize(30,30)
        
        self.project_title = QLabel()
        self.project_title.setStyleSheet("QLabel{font-size: 20px;}")
        
        self.list_type = QPushButton()
        self.list_type.setCursor(QCursor(Qt.PointingHandCursor))
        self.list_type.setFixedSize(30,30)
        
        header_layout_h.addWidget(self.open_folder)
        header_layout_h.addStretch()
        header_layout_h.addWidget(self.project_title)
        header_layout_h.addStretch()
        header_layout_h.addWidget(self.list_type)
        
        v.addLayout(header_layout_h)
        
        #Hem treeview listeleme hemde ayrıntılı lisitelemeyi centralwidget ile ayırmak
        list_lauyout_h = QHBoxLayout()
        self.list_widgets = QMainWindow()
        
        self.list_tree = TreeWidget()
        
        self.list_widgets.setCentralWidget(self.list_tree)
        
        list_lauyout_h.addWidget(self.list_widgets)
        v.addLayout(list_lauyout_h)
        
        
        self.setLayout(v)
        self.setUI_dl()
        
    def setUI_dl(self):
        ud = ui_data.screen_project_icons
        ul = ui_lang.screen_project_text
        
        self.open_folder.setIcon(QIcon(ud["open-folder"]))
        self.list_type.setIcon(QIcon(ud["list-type"]))
        



class TreeWidget(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        self.setUI()
        
    def setUI(self):
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        sp = QSplitter(Qt.Vertical)
        
        self.filetree = FileTree(os.getcwd(),self)
        sp.addWidget(self.filetree)
        
        self.dizindetails = DizinFileDetails()
        sp.addWidget(self.dizindetails)
        
        self.dizindetails.setVisible(False)
        
        h.addWidget(sp)
        v.addLayout(h)
        
        self.setLayout(v)

#Treeview sınıfı        
class FileTree(QTreeView):
    
    def __init__(self, path, dizin):
        super().__init__()
        self.path = path
        self.dizin = dizin
        
        self.setUI()
    
    def setUI(self):
        self.filemodel = QFileSystemModel()
        self.filemodel.setRootPath(self.path)
        
        self.setModel(self.filemodel)
        self.setRootIndex(self.filemodel.index(self.path))
        
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
        
        self.setHeaderHidden(True)
        
        self.setAnimated(True)
        
        self.clicked.connect(self.getpath)

    def getpath(self, index):
        path = self.sender().model().filePath(index)
        
        if os.path.isfile(path):
            self.dizin.dizindetails.setFile(path)
        
        if os.path.isdir(path):
            self.dizin.dizindetails.setVisible(False)
        

class DizinFileDetails(QFrame):
    file = ""
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(258)
        
        self.setUI()
        
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        #---------------------header----------------
        header_h = QHBoxLayout()
        
        self.close = QPushButton("x")
        self.close.setStyleSheet("QPushButton {font-size: 20px;}")
        self.close.setMaximumWidth(50)
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.clicked.connect(self.__close)
        
        self.name = QLabel("main.py")
        
        header_h.addWidget(self.close)
        header_h.addWidget(self.name)
        #------------------header-------------
        v.addLayout(header_h)
        #--------------------------------------------------
        cizgi2 = QFrame()
        cizgi2.setFrameShape(QFrame.HLine)
        #--------------------------------------------------
        v.addWidget(cizgi2)
        #------------------------------özellikller----------
        pref_h = QHBoxLayout()
        
        self.prefext = ExtPref()
        self.prefsize = SizePref()
        
        pref_h.addStretch()
        pref_h.addWidget(self.prefext)
        pref_h.addWidget(self.prefsize)
        pref_h.addStretch()
        #---------------------------------özellikler--------
        v.addLayout(pref_h)
        #----------------------içindeki dosyalar---------------       
        sc_area = QScrollArea()
        sc_area.setWidgetResizable(True)
        sc_w = QWidget()
        self.sc_f = QFormLayout()
        
        
        sc_w.setLayout(self.sc_f)
        sc_area.setWidget(sc_w)
        #----------------------içindeki dosyalar---------------
        v.addWidget(sc_area)
        #--------------------------------------------------
        cizgi3 = QFrame()
        cizgi3.setFrameShape(QFrame.HLine)
        #--------------------------------------------------
        v.addWidget(cizgi3)
        #----------------alt bölum--------------------
        bmenu_h = QHBoxLayout()
        
        self.delet = QPushButton()
        self.delet.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.open = QPushButton()
        self.open.setCursor(QCursor(Qt.PointingHandCursor))
        
        bmenu_h.addWidget(self.delet)
        bmenu_h.addStretch()
        bmenu_h.addWidget(self.open)
        #---------------------------alt bolum-----------------
        v.addLayout(bmenu_h)
        
        mh.addLayout(v)
        self.setLayout(mh)
        
    def setFile(self,file):
        ud = ui_data.screen_project_icons
        ul = ui_lang.screen_project_text
        
        self.delet.setText(ul["delete"])
        self.delet.setIcon(QIcon(ud["delete"]))
        
        self.open.setText(ul["open"])
        self.open.setIcon(QIcon(ud["open"]))
        
        
        """self.file = file
        while self.sc_f.count():
            child = self.sc_f.takeAt(0)
            childWidget = child.widget()
            if childWidget:
                childWidget.setParent(None)
                childWidget.deleteLater()"""
        
        self.prefext.setFile(file)
        self.prefsize.setFile(file)
        
        self.name.setText(os.path.split(file)[1])
        self.setVisible(True)
        
    
    
    def __close(self):
        print(self.size())
        self.setVisible(False)
        
    
    def setUI_dl(self):
        pass
    