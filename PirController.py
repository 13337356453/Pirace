# -*- encoding = utf-8 -*-
# author : manlu
import os
import re

from tools.GetTime import getTime


class PirController(object):
    pattern=re.compile(r'(.*?) \| URL = (.*?) \| UserName = (.*?) \| PassWord = (.*?) \|')
    def __init__(self):
        self.encoding='utf-8'
        if not os.path.exists(self.getPath()):
            f=open(self.getPath(),'w',encoding=self.encoding)
            f.close()

    def getPath(self):
        return os.getcwd()+"/back.pir"
    def read(self):
        f = open(self.getPath(), 'r', encoding=self.encoding)
        text = f.read()
        f.close()
        return text
    def readlines(self):
        text = self.read()
        if text is not None:
            return text.splitlines()
    def readline(self,line):
        l=self.readlines()
        return l[line]
    def write(self,url,uname,pwd,t=None):
        f=open(self.getPath(),'a+',encoding=self.encoding)
        if t==None:
            time=getTime()
            f.write("%s | URL = %s | UserName = %s | PassWord = %s |\n"%(time,url,uname,pwd))
            f.close()
            return time
        else:
            f.write("%s | URL = %s | UserName = %s | PassWord = %s |\n" % (t, url, uname, pwd))
            f.close()
            return t

    def delRow(self,text):
        l = re.findall(r'(.*?) \| (.*?) \| (.*?) \| (.*)', text)[0]
        url = l[0]
        uname = l[1]
        pwd = l[2]
        time = l[3][5:].strip()
        s="%s | URL = %s | UserName = %s | PassWord = %s |"%(time,url,uname,pwd)
        lines=self.readlines()
        lines.remove(s)
        f=open(self.getPath(),'w',encoding=self.encoding)
        for line in lines:
            f.write(line+"\n")
        f.close()
    def modifyRow(self,old_text,new_text):
        l = re.findall(r'(.*?) \| (.*?) \| (.*?) \| (.*)', old_text)[0]
        url = l[0]
        uname = l[1]
        pwd = l[2]
        time = l[3][5:].strip()
        s = "%s | URL = %s | UserName = %s | PassWord = %s |" % (time, url, uname, pwd)
        lines=self.readlines()
        lines.remove(s)
        lines.append(new_text)
        f = open(self.getPath(), 'w', encoding=self.encoding)
        for line in lines:
            f.write(line + "\n")
        f.close()

    def getURL(self):
        lines=self.readlines()
        result=[]
        for line in lines:
            l=re.findall(self.pattern,line)
            result.append(l)
        return result
