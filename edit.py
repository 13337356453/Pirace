# -*- encoding = utf-8 -*-
# author : manlu
import re

from PyQt5.QtWidgets import QWidget, QMessageBox

from PirController import PirController
from tools.GetTime import getTime
from windows.edit import Ui_EditWindow


class Edit(QWidget,Ui_EditWindow):
    url=''
    uname=''
    pwd=''
    pattern = re.compile(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?')
    def __init__(self,parent=None,text=''):
        super(Edit, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.text = text
        self.init()

    def init(self):
        url,uname,pwd=re.findall(r'(.*?) \| (.*?) \| (.*?) \|',self.text)[0]
        self.url_edit.setText(url)
        self.uname_edit.setText(uname)
        self.pwd_edit.setText(pwd)
        self.bind()
    def bind(self):
        self.cancleBtn.clicked.connect(lambda :self.destroy())
        self.editBtn.clicked.connect(self.edit)

    def edit(self):
        if (self.check()):
            time=getTime()
            new_text="%s | URL = %s | UserName = %s | PassWord = %s |"%(time,self.url,self.uname,self.pwd)
            pir=PirController()
            pir.modifyRow(self.text,new_text)
            self.parent.URLList.selectedItems()[0].setText("%s | %s | %s | 添加时间：%s" % (self.url, self.uname, self.pwd, time))
            QMessageBox.information(self,'成功','修改成功')
            self.destroy()

    def check(self):
        url = self.url_edit.text().strip()
        uname = self.uname_edit.text().strip()
        pwd = self.pwd_edit.text().strip()
        if url != "" and uname != "" and pwd != "":
            if re.match(self.pattern, url) != None:
                self.url=url
                self.uname=uname
                self.pwd=pwd
                return True
            else:
                QMessageBox.critical(self, "警告", "不正确的链接地址")
                self.url_edit.setText("")
        else:
            QMessageBox.critical(self, "警告", "请输入URL，UserName，Password")