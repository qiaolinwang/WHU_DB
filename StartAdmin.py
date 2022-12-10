from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5
import os
import sys
from Admin import Ui_Admin


class AdminGUI(QWidget, Ui_Admin):
    def __init__(self, parent=None):
        super(AdminGUI, self).__init__(parent)

        self.setupUi(self)

        #实现按下按钮跳转窗口的功能
        self.pushButton_8.clicked.connect(self.display) #添加图书
        self.pushButton_9.clicked.connect(self.display) #书刊查找
        self.pushButton_18.clicked.connect(self.display) #修改图书信息
        self.pushButton_19.clicked.connect(self.display) #浏览图书信息
        self.pushButton_21.clicked.connect(self.display) #查看读者信息
        self.pushButton_20.clicked.connect(self.exit) #注销账号
        self.Stack = self.stackedWidget

        self.Confirm_3.setEnabled(False) #添加图书初始时禁用
        self.Cancel_3.clicked.connect(self.display)
        self.Confirm_2.setEnabled(False) #书刊查找初始时禁用
        self.Cancel_2.clicked.connect(self.display)
        self.Confirm_4.setEnabled(False) #查找并修改初始时禁用
        self.Cancel_4.clicked.connect(self.display)

    def display(self):
        sender = self.sender()
        if sender.text() == "添加图书":
            self.Stack.setCurrentIndex(1)
        elif sender.text() == "书刊查找":
            self.Stack.setCurrentIndex(2)
        elif sender.text() == "修改图书信息":
            self.Stack.setCurrentIndex(3)
        elif sender.text() == "浏览图书信息":
            self.Stack.setCurrentIndex(4)
        elif sender.text() == "查看读者信息":
            self.Stack.setCurrentIndex(5)
        elif sender.text() == "取消":
            self.Stack.setCurrentIndex(0)

    def exit(self):
        reply = QMessageBox.question(self,
                                     '询问',
                                     "确定要注销账号吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass


    def closeEvent(self, e):
        reply = QMessageBox.question(self,
                                     '询问',
                                     "确定要退出管理员端吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            e.accept()
            sys.exit(0)
        else:
            e.ignore()


app = QApplication([])
stats = AdminGUI()
stats.show()
sys.exit(app.exec())
