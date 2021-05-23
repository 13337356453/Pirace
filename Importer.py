# -*- encoding = utf-8 -*-
# author : manlu

import re

from PirController import PirController


class Importer(object):
    def __init__(self,name,parent=None,encoding='utf-8'):
        self.name=name
        self.encoding=encoding
        self.parent=parent
    def Import(self):
        houzhui=self.name.split('.')[-1]
        if houzhui=="html":
            self.import_html()
        else:
            self.import_pir()
    def import_html(self):
        f=open(self.name,'r',encoding=self.encoding)
        text=f.read()
        l=re.findall(r'<li class="bbs"|\'bbs\'><p>链接：<a href=.*?>(.*?)</a><br>账号：(.*?)<br>密码：(.*?)<br>添加时间：(.*?)</p></li>',text)
        if len(l)>0:
            pir=PirController()
            for i in l:
                self.parent.URLList.addItem("%s | %s | %s | 添加时间：%s" %i)
                pir.write(i[0],i[1],i[2],i[3])
        f.close()
    def import_pir(self):
        pattern = re.compile(r'(.*?) \| URL = (.*?) \| UserName = (.*?) \| PassWord = (.*?) \|')
        f=open(self.name,'r',encoding=self.encoding)
        lines=f.readlines()
        for line in lines:
            pir=PirController()
            try:
                t,u,n,p=re.findall(pattern,line)[0]
                self.parent.URLList.addItem("%s | %s | %s | 添加时间：%s"%(u,n,p,t))
                pir.write(u,n,p,t)
            except IndexError:
                pass
        f.close()