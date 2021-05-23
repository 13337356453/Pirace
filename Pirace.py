# -*- encoding = utf-8 -*-
# author : manlu
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from PirController import PirController
from tools.GetTime import getTime
from tools.PiraceEvent import PiraceEvent
from windows.pirace import Ui_MainWindow


class Pirace(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Pirace,self).__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.Timer.setText(getTime())
        self.bind()
        self.readURL()

    def bind(self):
        self.controller=PiraceEvent(self)
        self.addBtn.clicked.connect(self.controller.add)
        self.delBtn.clicked.connect(self.controller.delete)
        self.editBtn.clicked.connect(self.controller.edit)
        self.importBtn.clicked.connect(self.controller.import_file)
        self.exportBtn.clicked.connect(self.controller.export)
        self.exitBtn.clicked.connect(lambda :sys.exit())
        #右击列表框事件
        self.URLList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.URLList.customContextMenuRequested.connect(self.controller.rightMenu)
        #双击列表框事件
        self.URLList.doubleClicked.connect(self.controller.openURL)

    def readURL(self):
        pir=PirController()
        l=pir.getURL()
        for i in l:
            try:
                self.URLList.addItem("%s | %s | %s | 添加时间：%s" % (i[0][1],i[0][2],i[0][3],i[0][0]))
            except IndexError:
                pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    pirace=Pirace()
    pirace.show()
    sys.exit(app.exec_())