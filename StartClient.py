import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Frontend.SuperAD import Ui_SuperAD
from Frontend.Reader import Ui_Reader
from Frontend.LoginAdmin import Ui_LoginAdmin
from Frontend.LoginReader import Ui_LoginReader
from Frontend.LoginSuper import Ui_LoginSuper
from Frontend.Admin import Ui_Admin
from Frontend.MainWin import Ui_MainWin
from Frontend.Register import Ui_Register

# 读者界面
class ReaderIn(Ui_Reader):
    def __init__(self, parent=None):
        super(ReaderIn, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.commandLinkButton.clicked.connect(self.display)  # 书刊查找界面
        self.commandLinkButton_5.clicked.connect(self.display)  # 借书还书界面
        self.commandLinkButton_6.clicked.connect(self.display)  # 读者信息修改界面
        self.commandLinkButton_7.clicked.connect(self.close)

    def display(self):
        sender = self.sender()
        if sender.text() == "书刊查找":
            self.stackedWidget.setCurrentIndex(1)
        elif sender.text() == "借书/还书":
            self.stackedWidget.setCurrentIndex(2)
        elif sender.text() == "读者信息修改":
            self.stackedWidget.setCurrentIndex(0)


# 超管界面
class SupAD(Ui_SuperAD):
    def __init__(self, parent=None):
        super(SupAD, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.queryAD.clicked.connect(self.display)  # 查询管理员界面
        self.addAD.clicked.connect(self.display)  # 增加管理员界面
        self.deleteAD.clicked.connect(self.display)  # 删除管理员界面

    def display(self):
        sender = self.sender()
        if sender.text() == "管理员查询":
            self.stackedWidget.setCurrentIndex(0)
        elif sender.text() == "增加管理员":
            self.stackedWidget.setCurrentIndex(1)
        elif sender.text() == "删除管理员":
            self.stackedWidget.setCurrentIndex(2)


class AdminGUI(QWidget, Ui_Admin):
    def __init__(self, parent=None):
        super(AdminGUI, self).__init__(parent)

        self.setupUi(self)

        # 实现按下按钮跳转窗口的功能
        self.pushButton_8.clicked.connect(self.display)  # 添加图书
        self.pushButton_9.clicked.connect(self.display)  # 书刊查找
        self.pushButton_18.clicked.connect(self.display)  # 修改图书信息
        self.pushButton_19.clicked.connect(self.display)  # 浏览图书信息
        self.pushButton_21.clicked.connect(self.display)  # 查看读者信息
        self.pushButton_20.clicked.connect(self.close)  # 注销账号
        self.Stack = self.stackedWidget

        self.Confirm_3.setEnabled(False)  # 添加图书初始时禁用
        self.Cancel_3.clicked.connect(self.display)
        self.Confirm_2.setEnabled(False)  # 书刊查找初始时禁用
        self.Cancel_2.clicked.connect(self.display)
        self.Confirm_4.setEnabled(False)  # 查找并修改初始时禁用
        self.Cancel_4.clicked.connect(self.display)


        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_7.setReadOnly(True)


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


class MainWin(QWidget, Ui_MainWin):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        self.setupUi(self)

        self.pushButton_7.clicked.connect(self.displayReader)  # 选择登录读者
        self.pushButton_6.clicked.connect(self.displayAdmin)
        self.pushButton_5.clicked.connect(self.displaySuper)
        self.pushButton_4.clicked.connect(self.close)
        self.Admin = AdminGUI()
        self.LoginAdmin = LoginAdmin()
        self.LoginReader = LoginReader()
        self.LoginSuper = LoginSuper()
        self.Super = SupAD()
        self.Reader = ReaderIn()
        self.Register = Register()
        self.LoginAdmin.pushButton.clicked.connect(self.EnterAdmin)
        self.LoginSuper.pushButton.clicked.connect(self.EnterSuper)
        self.LoginReader.pushButton.clicked.connect(self.EnterReader)
        self.LoginReader.pushButton_3.clicked.connect(self.displayRegister)


    def displayReader(self):
        self.LoginReader.show()

    def displayAdmin(self):
        self.LoginAdmin.show()

    def displaySuper(self):
        self.LoginSuper.show()

    def EnterAdmin(self):

        userName = self.LoginAdmin.lineEdit.text()  # 获取用户名
        password = self.LoginAdmin.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginAdmin, 'warning', '请补全用户名或密码！')
        elif userName == 'Admin' and password == '123':
            self.Admin.lineEdit_16.setText(userName)
            self.Admin.lineEdit_17.setText(password)
            self.Admin.lineEdit_14.setText(userName)
            self.Admin.lineEdit_15.setText(password)
            self.Admin.lineEdit_12.setText(userName)
            self.Admin.lineEdit_13.setText(password)
            self.Admin.lineEdit_18.setText(userName)
            self.Admin.lineEdit_19.setText(password)
            self.Admin.lineEdit_8.setText(userName)
            self.Admin.lineEdit_6.setText(password)
            self.Admin.lineEdit_9.setText(userName)
            self.Admin.lineEdit_7.setText(password)
            self.Admin.show()
            self.LoginAdmin.close()
        else:
            QMessageBox.warning(self.LoginAdmin, 'warning', '未找到该管理员！')


    def EnterSuper(self):

        userName = self.LoginSuper.lineEdit.text()  # 获取用户名
        password = self.LoginSuper.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginSuper, 'warning', '请补全用户名或密码！')
        elif userName == 'Super' and password == '123':
                self.Super.show()
                self.LoginSuper.close()
        else:
            QMessageBox.warning(self.LoginSuper, 'warning', '未找到该管理员！')



    def EnterReader(self):

        userName = self.LoginReader.lineEdit.text()  # 获取用户名
        password = self.LoginReader.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginReader, 'warning', '请补全用户名或密码！')
        elif userName == 'Reader' and password == '123':
                self.Reader.show()
                self.LoginReader.close()
        else:
            QMessageBox.warning(self.LoginReader, 'warning', '未找到读者，请注册！')

    def displayRegister(self, type):
        self.Register.show()








class LoginAdmin(QWidget, Ui_LoginAdmin):
    def __init__(self, parent=None):
        super(LoginAdmin, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


class LoginReader(QWidget, Ui_LoginReader):
    def __init__(self, parent=None):
        super(LoginReader, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


class LoginSuper(QWidget, Ui_LoginSuper):
    def __init__(self, parent=None):
        super(LoginSuper, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


class Register(QWidget, Ui_Register):
    def __init__(self, parent=None):
        super(Register, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


if __name__ == "__main__":
    app = QApplication([])
    stats = MainWin()
    stats.show()
    sys.exit(app.exec())
