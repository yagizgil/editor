from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import screen.project as sp
import screen.editor as se
import screen.tools as st

import ui_lang


class Screen(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setUI()
        
    def setUI(self):
        self.project_area = sp.ProjectArea()
        self.editor_area = se.EditorArea()
        self.tools_area = st.ToolsArea()
        
        pa = QDockWidget("Proje",self)
        ta = QDockWidget("Araçlar",self)
        
        pa.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        ta.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        
        pa.setWidget(self.project_area)
        ta.setWidget(self.tools_area)
        
        self.addDockWidget(Qt.RightDockWidgetArea,pa)
        self.tabifyDockWidget(pa,ta)
        
        self.setDockOptions(self.GroupedDragging | self.AllowTabbedDocks | self.AllowNestedDocks | self.AnimatedDocks)
        #self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)
        self.setCentralWidget(self.editor_area)
        
        

class DockWidget(QDockWidget):
    def __init__(self, title):
        super().__init__(title)
        
        self.dockLocationChanged.connect(self.on_dockLocationChanged)

    def on_dockLocationChanged(self):
        main: QMainWindow = self.parent()
        all_dock_widgets = main.findChildren(QDockWidget)

        for dock_widget in all_dock_widgets:
            sibling_tabs = main.tabifiedDockWidgets(dock_widget)
            # If you pull a tab out of a group the other tabs still see it as a sibling while dragging...
            sibling_tabs = [s for s in sibling_tabs if not s.isFloating()]

            if len(sibling_tabs) != 0:
                # Hide title bar
                dock_widget.setTitleBarWidget(QWidget())
            else:
                # Re-enable title bar
                dock_widget.setTitleBarWidget(None)

    def minimumSizeHint(self) -> QSize:
        return QSize(100, 100)