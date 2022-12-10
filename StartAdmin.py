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
        self.pushButton_8.clicked.connect(self.display)
        self.pushButton_9.clicked.connect(self.display)

        self.pushButton_18.clicked.connect(self.display)
        self.pushButton_19.clicked.connect(self.display)
        self.pushButton_21.clicked.connect(self.display)
        self.pushButton_20.clicked.connect(self.close)
        self.Stack = self.stackedWidget


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



app = QApplication([])
stats = AdminGUI()
stats.show()
sys.exit(app.exec())