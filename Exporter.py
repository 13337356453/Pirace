# -*- encoding = utf-8 -*-
# author : manlu
import re

from PyQt5.QtWidgets import QMessageBox



class Exporter(object):
    def __init__(self,name,urls,encoding='utf-8',parent=None):
        self.name=name
        self.urls=urls
        self.encoding=encoding
        self.parent=parent
    def export_html(self):
        f=open(self.name,'w',encoding=self.encoding)
        f.write('''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>保存的后台</title><style>p {
        font-size:16px;font-weight:600;}a {color: black;text-decoration: none;}a:hover {color: red;text-decoration: 
        underline;}</style></head><body><h1>保存的后台</h1><ol id='bs'>''')
        for url in self.urls:
            u,n,p,t=re.findall(r'(.*?) \| (.*?) \| (.*?) \| (.*)',url)[0]
            t=t[5:].strip()
            f.write('''<li class='bbs'><p>链接：<a href='%s'>%s</a><br>账号：%s<br>密码：%s<br>添加时间：%s</p></li>'''%(u,u,n,p,t))
        f.write('''</ol></body></html>''')
        f.close()
        QMessageBox.information(self.parent, "成功", "文件保存成功\n保存路径：%s"%self.name)
    def export_pir(self):
        f=open(self.name,'w',encoding=self.encoding)
        for url in self.urls:
            u,n,p,t=re.findall(r'(.*?) \| (.*?) \| (.*?) \| (.*)',url)[0]
            t=t[5:].strip()
            f.write("%s | URL = %s | UserName = %s | PassWord = %s |\n" % (t, u, n, p))
        f.close()
        QMessageBox.information(self.parent, "成功", "文件保存成功\n保存路径：%s"%self.name)

    def common_export(self):
        f=open(self.name,'w',encoding=self.encoding)
        for url in self.urls:
            f.write(url+"\n")
        f.close()
        QMessageBox.information(self.parent, "成功", "文件保存成功\n保存路径：%s"%self.name)
