# -*- encoding = utf-8 -*-
# author : manlu
import re

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QCursor, QDesktopServices
from PyQt5.QtWidgets import QMenu, QAction, QFileDialog

from Exporter import Exporter
from Importer import Importer
from PirController import PirController
from add import Add
from edit import Edit


class PiraceEvent(object):
    def __init__(self,parent):
        self.parent=parent

    def add(self):
        self.addWindow=Add(self.parent)
        self.addWindow.show()

    def edit(self):
        try:
            item=self.parent.URLList.selectedItems()[0]
            text=item.text()
            self.editWindow = Edit(self.parent,text)
            self.editWindow.show()
        except IndexError:
            pass

    def delete(self):
        try:
            item=self.parent.URLList.selectedItems()[0]
            row=self.parent.URLList.row(item)
            self.parent.URLList.takeItem(row)
            text = item.text()
            pir=PirController()
            pir.delRow(text)
        except IndexError:
            pass


    def import_file(self):
        file=QFileDialog.getOpenFileName(None,"导入文件","/","html文件(*.html);;pir文件(*.pir)")[0]
        if file.strip()!="":
            importer=Importer(file,self.parent)
            importer.Import()


    def export(self):
        name = QFileDialog.getSaveFileName(None, "导出文件", "/", "html文件(*.html);;All Files(*.*);;pir文件(*.pir)")[0]
        if name.strip()!="":
            count = self.parent.URLList.count()
            urls=[]
            for i in range(count):
                urls.append(self.parent.URLList.item(i).text())
            exporter=Exporter(name,urls)
            houzhui=name.split('.')[-1]
            if houzhui=="html":
                exporter.export_html()
            elif houzhui=='pir':
                exporter.export_pir()
            else:
                exporter.common_export()
    def rightMenu(self,pos):
        menu = QMenu(self.parent.URLList)
        menu.addAction(QAction('添加', menu))
        menu.addAction(QAction('编辑', menu))
        menu.addAction(QAction('删除', menu))
        menu.triggered.connect(self.menuEvent)
        menu.exec_(QCursor.pos())
    def menuEvent(self,act):
        event=act.text()
        if event=='添加':
            self.add()
        elif event=='删除':
            self.delete()
        else:
            self.edit()
    def openURL(self):
        if not self.parent.URLList.count() == 0:
            item = self.parent.URLList.selectedItems()[0]
            url = re.findall(r'(.*?) \|', item.text())[0]
            QDesktopServices.openUrl(QUrl(url))
        else:
            pass