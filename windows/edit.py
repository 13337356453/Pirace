# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditWindow(object):
    def setupUi(self, EditWindow):
        EditWindow.setObjectName("EditWindow")
        EditWindow.resize(444, 403)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        EditWindow.setFont(font)
        self.label = QtWidgets.QLabel(EditWindow)
        self.label.setGeometry(QtCore.QRect(50, 50, 61, 40))
        self.label.setObjectName("label")
        self.url_edit = QtWidgets.QLineEdit(EditWindow)
        self.url_edit.setGeometry(QtCore.QRect(119, 50, 281, 40))
        self.url_edit.setObjectName("url_edit")
        self.label_2 = QtWidgets.QLabel(EditWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 140, 40))
        self.label_2.setObjectName("label_2")
        self.uname_edit = QtWidgets.QLineEdit(EditWindow)
        self.uname_edit.setGeometry(QtCore.QRect(50, 170, 351, 40))
        self.uname_edit.setObjectName("uname_edit")
        self.label_3 = QtWidgets.QLabel(EditWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 229, 140, 40))
        self.label_3.setObjectName("label_3")
        self.pwd_edit = QtWidgets.QLineEdit(EditWindow)
        self.pwd_edit.setGeometry(QtCore.QRect(50, 278, 351, 40))
        self.pwd_edit.setObjectName("pwd_edit")
        self.editBtn = QtWidgets.QPushButton(EditWindow)
        self.editBtn.setGeometry(QtCore.QRect(50, 330, 91, 51))
        self.editBtn.setObjectName("editBtn")
        self.cancleBtn = QtWidgets.QPushButton(EditWindow)
        self.cancleBtn.setGeometry(QtCore.QRect(310, 330, 91, 51))
        self.cancleBtn.setObjectName("cancleBtn")

        self.retranslateUi(EditWindow)
        QtCore.QMetaObject.connectSlotsByName(EditWindow)

    def retranslateUi(self, EditWindow):
        _translate = QtCore.QCoreApplication.translate
        EditWindow.setWindowTitle(_translate("EditWindow", "编辑你的链接"))
        self.label.setText(_translate("EditWindow", "URL："))
        self.label_2.setText(_translate("EditWindow", "UserName："))
        self.label_3.setText(_translate("EditWindow", "PassWord："))
        self.editBtn.setText(_translate("EditWindow", "确认"))
        self.cancleBtn.setText(_translate("EditWindow", "取消"))