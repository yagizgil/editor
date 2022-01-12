from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import screen.syntax as syn

class EditorArea(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        self.setUI()
        
    def setUI(self):
        """v = QVBoxLayout()
        h = QHBoxLayout()
        
        self.tab = QTabWidget()
        self.tab.setTabsClosable(True)
        self.tab.setMovable(True)
        
        self.tab.addTab(FileTab(),"deneme")
        self.tab.addTab(FileTab(),"deneme2")
        self.tab.addTab(FileTab(),"deneme3")
        self.tab.addTab(FileTab(),"deneme4")
        self.tab.addTab(FileTab(),"deneme5")
        self.tab.addTab(FileTab(),"deneme6")
        self.tab.addTab(FileTab(),"deneme7")
        self.tab.addTab(FileTab(),"deneme8")
        self.tab.addTab(FileTab(),"deneme9")
        self.tab.addTab(FileTab(),"deneme10")
        
        h.addWidget(self.tab)
        v.addLayout(h)
        self.setLayout(v)"""
        
        self.addDockWidget(Qt.LeftDockWidgetArea,FileTab("denem1"))
        FileTab("denem2")
        FileTab("denem3")
        FileTab("denem4")
        FileTab("denem5")
        FileTab("denem6")
        
        for i in range(len(FileTab.dock_list)):
            if i != 0:
                self.tabifyDockWidget(FileTab.dock_list[0], FileTab.dock_list[i])
        
        
        self.setDockOptions(self.GroupedDragging | self.AllowTabbedDocks | self.AllowNestedDocks | self.AnimatedDocks)
        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)


class FileTab(QDockWidget):
    dock_list = list()
    def __init__(self,title):
        super().__init__(title)
        self.dock_list.append(self)
        
        self.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)
        self.dockLocationChanged.connect(self.on_dockLocationChanged)
        
        self.setStyleSheet("QDockWidget::title {border-style: none;}")
        
        self.setUI()
        
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        #newAct = contextMenu.addAction("New")
        #openAct = contextMenu.addAction("Open")
        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            self.close()

    def on_dockLocationChanged(self):
        main: QMainWindow = self.parent()
        all_dock_widgets = main.findChildren(QDockWidget)

        for dock_widget in all_dock_widgets:
            sibling_tabs = main.tabifiedDockWidgets(dock_widget)
            # If you pull a tab out of a group the other tabs still see it as a sibling while dragging...
            sibling_tabs = [s for s in sibling_tabs if not s.isFloating()]
            
            if len(sibling_tabs) == 0:
                dock_widget.setTitleBarWidget(None)
            else:
                dock_widget.setTitleBarWidget(QWidget())

    def minimumSizeHint(self) -> QSize:
        return QSize(100, 100)
    
    def setUI(self):
        w = QMainWindow()
        
        self.txt_edit = CodsEdit("Tüm Kod", "text-edit")
        self.list_edit = CodsEdit("Sınıflandırılmış", "list-edit")
        
        w.addDockWidget(Qt.LeftDockWidgetArea, self.txt_edit)
        w.tabifyDockWidget(self.txt_edit, self.list_edit)
        
        w.setDockOptions(w.GroupedDragging | w.AllowTabbedDocks | w.AllowNestedDocks | w.AnimatedDocks | w.VerticalTabs)
        w.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.South)
        
        self.setWidget(w)
        
        self.txt_edit.setTitleBarWidget(QWidget()) #program açıldığında dokwidgetların barları gözüküyordu
        self.list_edit.setTitleBarWidget(QWidget()) #işe yaramıyor
        
        





class CodsEdit(QDockWidget):
    def __init__(self, title, type_edit):
        super().__init__(title)
        self.type_edit = type_edit
        
        self.setFeatures(QDockWidget.DockWidgetMovable)
        self.dockLocationChanged.connect(self.on_dockLocationChanged)
        
        self.setUI()

    def on_dockLocationChanged(self):
        main: QMainWindow = self.parent()
        all_dock_widgets = main.findChildren(QDockWidget)

        for dock_widget in all_dock_widgets:
            sibling_tabs = main.tabifiedDockWidgets(dock_widget)
            # If you pull a tab out of a group the other tabs still see it as a sibling while dragging...
            sibling_tabs = [s for s in sibling_tabs if not s.isFloating()]
            
            if len(sibling_tabs) == 0:
                dock_widget.setTitleBarWidget(None)
            else:
                dock_widget.setTitleBarWidget(QWidget())

    def minimumSizeHint(self) -> QSize:
        return QSize(100, 100)
    
    def setUI(self):
        if self.type_edit == "text-edit":
            self.w = TextEdit()
        
        if self.type_edit == "list-edit":
            self.w = ListEdit()
        
        self.setWidget(self.w)
        



class LineNumberArea(QWidget):
 
 
    def __init__(self, editor):
        super().__init__(editor)
        self.myeditor = editor
 
 
    def sizeHint(self):
        return Qsize(self.editor.lineNumberAreaWidth(), 0)
 
 
    def paintEvent(self, event):
        self.myeditor.lineNumberAreaPaintEvent(event)


class CodeEditor(QPlainTextEdit):
    def __init__(self, parent = None):
        super(CodeEditor,self).__init__(parent)
        self.highlight = syn.PythonHighlighter(self.document())
        
        self.lineNumberArea = LineNumberArea(self)
 
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        #self.cursorPositionChanged.connect(self.highlightCurrentLine)
        
        self.updateLineNumberAreaWidth(0)
 
 
    def lineNumberAreaWidth(self):
        digits = 1
        count = max(1, self.blockCount())
        while count >= 10:
            count /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        return space
 
 
    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)
 
 
    def updateLineNumberArea(self, rect, dy):
 
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(),
                       rect.height())
 
        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)
 
 
    def resizeEvent(self, event):
        super().resizeEvent(event)
 
        cr = self.contentsRect();
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(),
                    self.lineNumberAreaWidth(), cr.height()))
 
 
    def lineNumberAreaPaintEvent(self, event):
        mypainter = QPainter(self.lineNumberArea)
 
        mypainter.fillRect(event.rect(), Qt.lightGray)
 
        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
 
        # Just to make sure I use the right font
        height = self.fontMetrics().height()
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(blockNumber + 1)
                mypainter.setPen(Qt.black)
                mypainter.drawText(0, top, self.lineNumberArea.width(), height,
                 Qt.AlignCenter, number)
 
            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1
        
    def highlightCurrentLine(self):
        extraSelections = []
 
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
 
            lineColor = QColor(Qt.lightGray).lighter(185)
 
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)
 


class TextEdit(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        self.txt = CodeEditor()
        
        h.addWidget(self.txt)
        v.addLayout(h)
        self.setLayout(v)




class ListEdit(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        self.txt = QTextEdit()
        
        h.addWidget(self.txt)
        v.addLayout(h)
        self.setLayout(v)