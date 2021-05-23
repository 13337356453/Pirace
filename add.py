# -*- encoding = utf-8 -*-
# author : manlu
import re

from PyQt5.QtWidgets import QWidget, QMessageBox

from PirController import PirController
from windows.Add import Ui_AddForm


class Add(QWidget,Ui_AddForm):
    pattern=re.compile(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?')
    url=''
    uname=''
    pwd=''
    def __init__(self,parent=None):
        super(Add,self).__init__()
        self.parent=parent
        self.setupUi(self)
        self.bind()
    def bind(self):
        self.cancleBtn.clicked.connect(lambda :self.destroy())
        self.submitBtn.clicked.connect(self.check)
    def check(self):
        url = self.url_field.text().strip()
        uname = self.uname_field.text().strip()
        pwd = self.pwd_field.text().strip()
        if url != "" and uname != "" and pwd != "":
            if re.match(self.pattern, url) != None:
                self.url=url
                self.uname=uname
                self.pwd=pwd
                self.add()
                QMessageBox.information(self,"成功","添加成功")
                self.destroy()
            else:
                QMessageBox.critical(self, "警告", "不正确的链接地址")
                self.url_field.setText("")
        else:
            QMessageBox.critical(self, "警告", "请输入URL，UserName，Password")

    def add(self):
        pc = PirController()
        time = pc.write(self.url, self.uname, self.pwd)
        self.parent.URLList.addItem("%s | %s | %s | 添加时间：%s" % (self.url, self.uname, self.pwd, time))