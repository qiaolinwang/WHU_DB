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
from Backend.WHU_DB import Database
import datetime
import time


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


# 管理员界面
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

        self.Cancel_3.clicked.connect(self.display)

        self.Cancel_2.clicked.connect(self.display)

        self.Cancel_4.clicked.connect(self.display)

        self.Cancel_5.clicked.connect(self.display)

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
        elif sender.text() == "修改/删除图书":
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
        self.WHU_DB = Database()
        self.LoginAdmin.pushButton.clicked.connect(self.EnterAdmin)
        self.LoginSuper.pushButton.clicked.connect(self.EnterSuper)
        self.LoginReader.pushButton.clicked.connect(self.EnterReader)
        self.LoginReader.pushButton_3.clicked.connect(self.displayRegister)
        self.Admin.Confirm_3.clicked.connect(self.add_book)
        self.Admin.pushButton_19.clicked.connect(self.browse_book)
        self.Admin.pushButton_21.clicked.connect(self.browse_reader)
        self.Admin.Confirm_2.clicked.connect(self.find_book)
        self.Admin.Confirm_4.clicked.connect(self.check_book)
        self.Admin.Confirm_5.clicked.connect(self.modify_book)
        self.Admin.Confirm_6.clicked.connect(self.delete_book)

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

    def browse_book(self):
        books = self.WHU_DB.show_book()
        print(books)
        if not len(books) == 0:
            try:
                self.Admin.tableWidget_4.clearContents()
                self.Admin.tableWidget_4.setRowCount(0)
                for line in books:
                    currentRowCount = self.Admin.tableWidget_4.rowCount()
                    self.Admin.tableWidget_4.insertRow(currentRowCount)
                    self.Admin.tableWidget_4.setItem(currentRowCount, 0, QTableWidgetItem(line['name']))
                    self.Admin.tableWidget_4.setItem(currentRowCount, 1, QTableWidgetItem(str(line['id'])))
                    self.Admin.tableWidget_4.setItem(currentRowCount, 2, QTableWidgetItem(line['author']))
                    self.Admin.tableWidget_4.setItem(currentRowCount, 3,
                                                     QTableWidgetItem(str(line['pubdate'].strftime('%Y-%m-%d'))))
                    self.Admin.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
                print("浏览图书成功")

            except Exception as e:
                print(e)

    def browse_reader(self):
        readers = self.WHU_DB.show_reader()
        print(readers)
        if not len(readers) == 0:
            try:
                self.Admin.tableWidget_3.clearContents()
                self.Admin.tableWidget_3.setRowCount(0)
                for line in readers:
                    currentRowCount = self.Admin.tableWidget_3.rowCount()
                    self.Admin.tableWidget_3.insertRow(currentRowCount)
                    self.Admin.tableWidget_3.setItem(currentRowCount, 0, QTableWidgetItem(line['stu_user']))
                    self.Admin.tableWidget_3.setItem(currentRowCount, 1, QTableWidgetItem(str(line['stu_password'])))
                    self.Admin.tableWidget_3.setItem(currentRowCount, 2, QTableWidgetItem(line['stu_name']))
                    self.Admin.tableWidget_3.setItem(currentRowCount, 3, QTableWidgetItem(str(line['stu_id'])))
                    self.Admin.tableWidget_3.setItem(currentRowCount, 4, QTableWidgetItem(line['stu_dep']))
                    self.Admin.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
                print("浏览图书成功")

            except Exception as e:
                print(e)

    def find_book(self):
        name = self.Admin.Name_2.text()  # 获取书名
        index = self.Admin.User_3.text()  # 获取索引号
        author = self.Admin.User_4.text()  # 获取作者
        pubdate = self.Admin.Port_2.text()  # 获取出版时间
        splitdate = pubdate.split('-')

        if len(name) == 0 and len(index) == 0 and len(author) == 0 and len(pubdate) == 0:
            QMessageBox.warning(self.Admin, 'warning', '请填写至少一项信息！')
            return
        else:
            if not len(index) == 0:
                if not index.isdigit():
                    QMessageBox.warning(self.Admin, 'warning', '索引号格式错误！')
                    return
            if len(index) == 0:
                index = -1
            if not len(pubdate) == 0:
                if not len(splitdate) == 3:
                    QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
                    return
                elif splitdate[0].isdigit() and splitdate[1].isdigit() and splitdate[2].isdigit():
                    if not int(splitdate[0]) in range(0, 2023) or not int(splitdate[1]) in range(1, 13) or not int(
                            splitdate[2]) in range(1, 32):
                        QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
                        return
                else:
                    QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
                    return
            try:
                searched_book = {'id': index, 'name': name, 'author': author, 'pubdate': pubdate}
                print(searched_book)

                results = self.WHU_DB.search_book(searched_book)
                if len(results) == 0:
                    QMessageBox.warning(self.Admin, 'warning', '未查找到符合结果，请检查输入信息是否正确！')
                else:
                    self.Admin.Name_2.clear()
                    self.Admin.User_3.clear()
                    self.Admin.User_4.clear()
                    self.Admin.Port_2.clear()
                    self.Admin.stackedWidget.setCurrentIndex(6)
                    self.Admin.tableWidget_5.clearContents()
                    self.Admin.tableWidget_5.setRowCount(0)
                    for line in results:
                        currentRowCount = self.Admin.tableWidget_5.rowCount()
                        self.Admin.tableWidget_5.insertRow(currentRowCount)
                        self.Admin.tableWidget_5.setItem(currentRowCount, 0, QTableWidgetItem(line[0]))
                        self.Admin.tableWidget_5.setItem(currentRowCount, 1, QTableWidgetItem(str(line[1])))
                        self.Admin.tableWidget_5.setItem(currentRowCount, 2, QTableWidgetItem(line[2]))
                        self.Admin.tableWidget_5.setItem(currentRowCount, 3,
                                                         QTableWidgetItem(str(line[3].strftime('%Y-%m-%d'))))
                        self.Admin.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
            except Exception as e:
                print(e)

    def add_book(self):
        name = self.Admin.Name_3.text()  # 获取书名
        index = self.Admin.User_5.text()  # 获取索引号
        author = self.Admin.User_6.text()  # 获取作者
        pubdate = self.Admin.Port_3.text()  # 获取出版时间
        splitdate = pubdate.split('-')

        if len(name) == 0 or len(index) == 0 or len(author) == 0 or len(pubdate) == 0:
            QMessageBox.warning(self.Admin, 'warning', '请补全图书信息！')
        else:
            if not index.isdigit():
                QMessageBox.warning(self.Admin, 'warning', '索引号格式错误！')
            elif not len(splitdate) == 3:
                QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
            elif splitdate[0].isdigit() and splitdate[1].isdigit() and splitdate[2].isdigit():
                if int(splitdate[0]) in range(0, 2023) and int(splitdate[1]) in range(1, 13) and int(
                        splitdate[2]) in range(1, 32):
                    new_book = {'id': index, 'name': name, 'author': author, 'pubdate': pubdate}
                    try:
                        self.WHU_DB.insert_book(new_book)
                        QMessageBox.information(self.Admin, '通知', '添加图书成功！')
                        self.Admin.Name_3.clear()
                        self.Admin.User_5.clear()
                        self.Admin.User_6.clear()
                        self.Admin.Port_3.clear()
                    except Exception as e:
                        print(e)
                else:
                    QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
            else:
                QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')

    def check_book(self):
        name = self.Admin.Name_4.text()  # 获取书名
        index = self.Admin.User_7.text()  # 获取索引号
        author = self.Admin.User_8.text()  # 获取作者
        pubdate = self.Admin.Port_4.text()  # 获取出版时间
        splitdate = pubdate.split('-')

        if len(index) == 0 and (len(name) == 0 or len(author) == 0 or len(pubdate) == 0):
            # 至少要输入索引号进行查找
            QMessageBox.warning(self.Admin, 'warning', '请补全图书信息！')
            return
        elif not len(index) == 0:
            if not len(index) == 0:
                if not index.isdigit():
                    QMessageBox.warning(self.Admin, 'warning', '索引号格式错误！')
                    return
            if not len(pubdate) == 0:
                if not len(splitdate) == 3:
                    QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
                    return
                elif splitdate[0].isdigit() and splitdate[1].isdigit() and splitdate[2].isdigit():
                    if not int(splitdate[0]) in range(0, 2023) or not int(splitdate[1]) in range(1, 13) or not int(
                            splitdate[2]) in range(1, 32):
                        QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
                        return
            try:
                searched_book = {'id': index, 'name': name, 'author': author, 'pubdate': pubdate}
                print(searched_book)
                results = self.WHU_DB.search_book(searched_book)
                if len(results) == 0:
                    QMessageBox.warning(self.Admin, 'warning', '未查找到符合结果，请检查输入信息是否正确！')
                else:
                    # 进入修改和删除页面
                    self.Admin.stackedWidget.setCurrentIndex(7)
                    self.Admin.lineEdit.setText(results[0][0])
                    self.Admin.lineEdit_2.setText(str(results[0][1]))
                    self.Admin.lineEdit_3.setText(results[0][2])
                    self.Admin.lineEdit_4.setText(str(results[0][3].strftime('%Y-%m-%d')))
                    self.Admin.User_9.setText(index)

            except Exception as e:
                print(e)

    def modify_book(self):
        name = self.Admin.Name_5.text()  # 获取书名
        index = self.Admin.User_9.text()  # 获取索引号
        author = self.Admin.User_10.text()  # 获取作者
        pubdate = self.Admin.Port_5.text()  # 获取出版时间
        splitdate = pubdate.split('-')
        oldname = self.Admin.lineEdit.text()
        oldauthor = self.Admin.lineEdit_3.text()
        oldpubdate = self.Admin.lineEdit_4.text()
        if name == oldname and author == oldauthor and pubdate == oldpubdate:
            QMessageBox.warning(self.Admin, 'warning', '请至少修改一项信息！')
            return
        if len(name) == 0 or len(author) == 0 or len(pubdate) == 0:
            QMessageBox.warning(self.Admin, 'warning', '请补全图书信息！')
            return
        else:
            if not len(splitdate) == 3:
                QMessageBox.warning(self.Admin, 'warning', '出版时间格式错误！')
                return
            elif splitdate[0].isdigit() and splitdate[1].isdigit() and splitdate[2].isdigit():
                if int(splitdate[0]) in range(0, 2023) and int(splitdate[1]) in range(1, 13) and int(
                        splitdate[2]) in range(1, 32):
                    modified_book = {'id': index, 'name': name, 'author': author, 'pubdate': pubdate}
                    reply = QMessageBox.question(self.Admin,
                                                 '询问',
                                                 "确定要修改该图书吗？",
                                                 QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        try:
                            self.WHU_DB.book_modify(modified_book)
                            self.Admin.lineEdit.clear()
                            self.Admin.lineEdit_2.clear()
                            self.Admin.lineEdit_3.clear()
                            self.Admin.lineEdit_4.clear()
                            self.Admin.Name_5.clear()
                            self.Admin.User_9.clear()
                            self.Admin.User_10.clear()
                            self.Admin.Port_5.clear()
                            QMessageBox.information(self.Admin, '通知', '修改图书成功！')
                            self.Admin.stackedWidget.setCurrentIndex(0)
                        except Exception as e:
                            print(e)
                    else:
                        pass

    def delete_book(self):
        index = self.Admin.User_9.text()
        print(index)
        reply = QMessageBox.question(self.Admin,
                                     '询问',
                                     "确定要删除该图书吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                self.WHU_DB.book_delete(index)
                self.Admin.lineEdit.clear()
                self.Admin.lineEdit_2.clear()
                self.Admin.lineEdit_3.clear()
                self.Admin.lineEdit_4.clear()
                self.Admin.User_9.clear()
                QMessageBox.information(self.Admin, '通知', '删除图书成功！')
                self.Admin.stackedWidget.setCurrentIndex(0)
            except Exception as e:
                print(e)
        else:
            pass






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
