import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from SuperAD import Ui_SuperAD
from Reader import Ui_Reader
from Login import Ui_login
import qdarkstyle


#读者界面
class ReaderIn(Ui_Reader):
    def __init__(self, parent=None):
        super(ReaderIn, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.commandLinkButton.clicked.connect(self.display)    #书刊查找界面
        self.commandLinkButton_5.clicked.connect(self.display)  #借书还书界面
        self.commandLinkButton_6.clicked.connect(self.display)  #读者信息修改界面

    def display(self):
        sender = self.sender()
        if sender.text() == "书刊查找":
            self.stackedWidget.setCurrentIndex(1)
        elif sender.text() == "借书/还书":
            self.stackedWidget.setCurrentIndex(2)
        elif sender.text() == "读者信息修改":
            self.stackedWidget.setCurrentIndex(0)


#超管界面
class SupAD(Ui_SuperAD):
    def __init__(self, parent=None):
        super(SupAD, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.queryAD.clicked.connect(self.display)  #查询管理员界面
        self.addAD.clicked.connect(self.display)    #增加管理员界面
        self.deleteAD.clicked.connect(self.display) #删除管理员界面

    def display(self):
        sender = self.sender()
        if sender.text() == "管理员查询":
            self.stackedWidget.setCurrentIndex(0)
        elif sender.text() == "增加管理员":
            self.stackedWidget.setCurrentIndex(1)
        elif sender.text() == "删除管理员":
            self.stackedWidget.setCurrentIndex(2)


#主界面
class mainLogin(Ui_login):
    def __init__(self, parent=None):
        super(mainLogin, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.pushButton_2.clicked.connect(self.login)    #登录按钮，连接登录函数


        #为主界面实例化对象
        self.reader=ReaderIn()
        self.supAD=SupAD()

    def login(self):
        '''
        该函数获取输入框用户名和密码，与数据库中用户进行对比，若匹配成功则进入用户界面
        '''
        userName = self.lineEdit.text() #获取用户名
        password = self.lineEdit_2.text()#获取密码

        #这里为了看效果 直接与123进行对比 需要后端连接数据库
        if userName == 'reader' and password == '123':
            self.reader.show()
        elif userName == 'supAD' and password == '123':
            self.supAD.show()










App = QtWidgets.QApplication([])
#App.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
ex =mainLogin()
ex.show()
sys.exit(App.exec_())
