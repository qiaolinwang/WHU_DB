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

SuperUser = 'Super'  # 超级管理员用户名
SuperPassword = '123'  # 超级管理员密码

# 读者界面
class ReaderIn(Ui_Reader):
    def __init__(self, parent=None):
        super(ReaderIn, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.commandLinkButton.clicked.connect(self.display)  # 书刊查找界面

        self.commandLinkButton_6.clicked.connect(self.display)  # 读者信息修改界面
        self.commandLinkButton_7.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.reset)

    def reset(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

    def display(self):
        sender = self.sender()
        if sender.text() == "书刊查找":
            self.stackedWidget.setCurrentIndex(1)
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


# 主界面
class MainWin(QWidget, Ui_MainWin):  # 实现前后端功能对接
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
        self.Super.doQuery.clicked.connect(self.find_admin)
        self.Super.pushButton.clicked.connect(self.add_admin)
        self.Super.pushButton_2.clicked.connect(self.delete_admin)
        self.Register.pushButton.clicked.connect(self.add_reader)
        self.Reader.pushButton_3.clicked.connect(self.reader_find_book)
        self.Reader.pushButton_2.clicked.connect(self.modify_reader)
        self.Reader.pushButton_4.clicked.connect(self.borrow_book)
        self.Reader.pushButton_5.clicked.connect(self.return_book)
        self.Reader.commandLinkButton_5.clicked.connect(self.displayRentBorrow)  # 借书还书界面
        self.CurrentReader = -1

    def displayRentBorrow(self):
        sender = self.Reader.sender()
        if sender.text() == "借书/还书":
            if not self.CurrentReader == -1:
                stu_id = self.CurrentReader
                try:
                    results = self.WHU_DB.browse_rent(stu_id)
                    self.Reader.tableWidget_2.clearContents()
                    self.Reader.tableWidget_2.setRowCount(0)
                    if not len(results) == 0:
                        for line in results:
                            searched_book = {'id': line[0], 'name': '', 'author': '', 'pubdate': ''}
                            book = self.WHU_DB.search_book(searched_book)
                            print(book)
                            currentRowCount = self.Reader.tableWidget_2.rowCount()
                            self.Reader.tableWidget_2.insertRow(currentRowCount)
                            self.Reader.tableWidget_2.setItem(currentRowCount, 0, QTableWidgetItem(book[0][0]))
                            self.Reader.tableWidget_2.setItem(currentRowCount, 1, QTableWidgetItem(book[0][2]))
                            self.Reader.tableWidget_2.setItem(currentRowCount, 2, QTableWidgetItem(str(book[0][3].strftime('%Y-%m-%d'))))
                            self.Reader.tableWidget_2.setItem(currentRowCount, 3, QTableWidgetItem(str(book[0][1])))
                            self.Reader.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
                except Exception as e:
                    print(e)
            else:
                print("CurrentReader为-1")
            self.Reader.stackedWidget.setCurrentIndex(2)

    def displayReader(self):
        self.LoginReader.show()

    def displayAdmin(self):
        self.LoginAdmin.show()

    def displaySuper(self):
        self.LoginSuper.show()

    def EnterAdmin(self):

        userName = self.LoginAdmin.lineEdit.text()  # 获取工号
        password = self.LoginAdmin.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginAdmin, 'warning', '请补全工号或密码！')
        else:
            verify = self.WHU_DB.login_admin(userName, password)
            if verify:
                self.LoginAdmin.lineEdit.clear()
                self.LoginAdmin.lineEdit_2.clear()

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
                QMessageBox.warning(self.LoginAdmin, 'warning', '工号或密码错误，请检查！')

    def EnterSuper(self):

        userName = self.LoginSuper.lineEdit.text()  # 获取用户名
        password = self.LoginSuper.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginSuper, 'warning', '请补全用户名或密码！')
        elif userName == SuperUser and password == SuperPassword:
            self.Super.show()
            self.LoginSuper.close()
        else:
            QMessageBox.warning(self.LoginSuper, 'warning', '未找到该管理员！')

    def EnterReader(self):
        self.CurrentReader = -1
        userName = self.LoginReader.lineEdit.text()  # 获取学号
        password = self.LoginReader.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginReader, 'warning', '请补全学号或密码！')
        else:
            verify = self.WHU_DB.login_reader(userName, password)
            if verify:
                self.LoginReader.lineEdit.clear()
                self.LoginReader.lineEdit_2.clear()

                self.CurrentReader = userName
                self.Reader.show()
                self.LoginReader.close()
            else:
                QMessageBox.warning(self.LoginReader, 'warning', '学号或密码错误！')

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
                    if line['rent_stu_id'] == -1:
                        self.Admin.tableWidget_4.setItem(currentRowCount, 4, QTableWidgetItem("暂未借出"))
                    else:
                        self.Admin.tableWidget_4.setItem(currentRowCount, 4, QTableWidgetItem(str(line['rent_stu_id'])))
                    self.Admin.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
                print("浏览图书成功")

            except Exception as e:
                print(e)
        else:
            QMessageBox.warning(self.Admin, '警告', '暂无图书信息！')

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
                print("浏览读者成功")

            except Exception as e:
                print(e)
        else:
            QMessageBox.warning(self.Admin, '警告', '暂无读者信息！')

    def find_book(self):
        name = self.Admin.Name_2.text()  # 获取书名
        index = self.Admin.User_3.text()  # 获取索引号
        author = self.Admin.User_4.text()  # 获取作者
        pubdate = self.Admin.Port_2.text()  # 获取出版时间
        splitdate = pubdate.split('-')
        timelen = 0.0
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
                # print(222)
                st = time.time()
                results = self.WHU_DB.search_book(searched_book)
                timelen = time.time()-st
                # print(timelen)
                if len(results) == 0:
                    QMessageBox.warning(self.Admin, 'warning', '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
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
                    QMessageBox.warning(self.Admin, 'warning',
                                        '查询完毕！查询用时：%4f s' % timelen)
            except Exception as e:
                QMessageBox.warning(self.Admin, 'warning',
                                    '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
                print(e)

    def add_book(self):
        name = self.Admin.Name_3.text()  # 获取书名
        index = self.Admin.User_5.text()  # 获取索引号
        author = self.Admin.User_6.text()  # 获取作者
        pubdate = self.Admin.Port_3.text()  # 获取出版时间
        splitdate = pubdate.split('-')

        if len(name) == 0 or len(index) == 0 or len(author) == 0 or len(pubdate) == 0:
            QMessageBox.warning(self.Admin, 'warning', '请补书籍信息！')
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
                        QMessageBox.warning(self.Admin, 'warning', '索引已存在！')
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
        timelen = 0.0
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
                # print(333)
                # results = self.WHU_DB.search_book(searched_book)
                # if len(results) == 0:
                #     QMessageBox.warning(self.Admin, 'warning', '未查找到符合结果，请检查输入信息是否正确！')
                st = time.time()
                results = self.WHU_DB.search_book(searched_book)
                timelen = time.time() - st
                # print(timelen)
                if len(results) == 0:
                    QMessageBox.warning(self.Admin, 'warning',
                                        '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
                else:
                    # 进入修改和删除页面
                    self.Admin.stackedWidget.setCurrentIndex(7)
                    self.Admin.lineEdit.setText(results[0][0])
                    self.Admin.lineEdit_2.setText(str(results[0][1]))
                    self.Admin.lineEdit_3.setText(results[0][2])
                    self.Admin.lineEdit_4.setText(str(results[0][3].strftime('%Y-%m-%d')))
                    self.Admin.User_9.setText(index)

            except Exception as e:
                QMessageBox.warning(self.Admin, 'warning',
                                    '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
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

    # 实现读者信息修改
    def modify_reader(self):
        name = self.Reader.lineEdit.text()
        id = self.Reader.lineEdit_2.text()
        dep = self.Reader.lineEdit_3.text()
        oldpassword = self.Reader.lineEdit_4.text()
        newpassword = self.Reader.lineEdit_5.text()
        if len(name) == 0 or len(id) == 0 or len(dep) == 0 or len(oldpassword) == 0 or len(newpassword) == 0:
            QMessageBox.warning(self.Reader, 'warning', '请补全读者信息！')
        elif not id.isdigit():
            QMessageBox.warning(self.Reader, 'warning', '学号格式错误！')
        else:
            reader = {'id': id, 'name': name, 'dep': dep, 'oldpassword': oldpassword, 'newpassword': newpassword}
            try:
                verify = self.WHU_DB.reader_modify(reader)
                if verify:
                    QMessageBox.information(self.Admin, '通知', '修改读者成功！')
                    self.Reader.lineEdit.clear()
                    self.Reader.lineEdit_2.clear()
                    self.Reader.lineEdit_3.clear()
                    self.Reader.lineEdit_4.clear()
                    self.Reader.lineEdit_5.clear()

                else:
                    QMessageBox.warning(self.Reader, '错误', '请检查学号和原密码是否正确！')
            except Exception as e:
                print(e)

    # 实现读者界面的书刊查找
    def reader_find_book(self):
        name = self.Reader.lineEdit_6.text()  # 获取书名
        index = self.Reader.lineEdit_9.text()  # 获取索引号
        author = self.Reader.lineEdit_12.text()  # 获取作者
        fardate = self.Reader.lineEdit_10.text()
        neardate = self.Reader.lineEdit_11.text()
        timelen = 0.0
        splitdate1 = fardate.split('-')
        splitdate2 = neardate.split('-')

        if len(name) == 0 and len(index) == 0 and len(author) == 0 and (len(fardate) == 0 and len(neardate) == 0):
            QMessageBox.warning(self.Reader, 'warning', '请填写至少一栏信息！')
            return
        else:
            if not len(index) == 0:
                if not index.isdigit():
                    QMessageBox.warning(self.Reader, 'warning', '索引号格式错误！')
                    return
            if len(index) == 0:
                index = -1
            if (len(fardate) == 0 and not len(neardate) == 0) or (not len(fardate) == 0 and len(neardate) == 0):
                QMessageBox.warning(self.Reader, 'warning', '请补全出版时间范围！')
            if not len(fardate) == 0 and not len(neardate) == 0:
                if not len(splitdate1) == 3 or not len(splitdate2) == 3:
                    QMessageBox.warning(self.Reader, 'warning', '出版时间格式错误！')
                    return
                elif splitdate1[0].isdigit() and splitdate1[1].isdigit() and splitdate1[2].isdigit() and splitdate2[
                    0].isdigit() and splitdate2[1].isdigit() and splitdate2[2].isdigit():
                    if not int(splitdate1[0]) in range(0, 2023) or not int(splitdate1[1]) in range(1, 13) or not int(
                            splitdate1[2]) in range(1, 32) or not int(splitdate2[0]) in range(0, 2023) or not int(
                        splitdate2[1]) in range(1, 13) or not int(splitdate2[2]) in range(1, 32):
                        QMessageBox.warning(self.Reader, 'warning', '出版时间格式错误！')
                        return
                else:
                    QMessageBox.warning(self.Reader, 'warning', '出版时间格式错误！')
                    return
            try:
                searched_book = {'id': index, 'name': name, 'author': author, 'fardate': fardate, 'neardate': neardate}
                print(searched_book)
                # print(111)
                # results = self.WHU_DB.reader_search_book(searched_book)
                # if len(results) == 0:
                #     QMessageBox.warning(self.Reader, 'warning', '未查找到符合结果，请检查输入信息是否正确！')
                st = time.time()
                results = self.WHU_DB.search_book(searched_book)
                timelen = time.time() - st
                if len(results) == 0:
                    QMessageBox.warning(self.Reader, 'warning',
                                        '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
                else:
                    self.Reader.tableWidget.clearContents()
                    self.Reader.tableWidget.setRowCount(0)
                    for line in results:
                        currentRowCount = self.Reader.tableWidget.rowCount()
                        self.Reader.tableWidget.insertRow(currentRowCount)
                        self.Reader.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(line[0]))
                        self.Reader.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(line[2]))
                        self.Reader.tableWidget.setItem(currentRowCount, 2,
                                                        QTableWidgetItem(str(line[3].strftime('%Y-%m-%d'))))
                        self.Reader.tableWidget.setItem(currentRowCount, 3,
                                                        QTableWidgetItem(str(line[1])))
                        self.Reader.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                    QMessageBox.warning(self.Reader, 'warning',
                                        '查询完毕！查询用时：%4f s' % timelen)
            except Exception as e:
                QMessageBox.warning(self.Reader, 'warning',
                                    '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
                print(e)

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

    # 实现添加管理员
    def add_admin(self):
        user = self.Super.lineEdit_3.text()
        id = self.Super.lineEdit_2.text()
        password = self.Super.lineEdit_4.text()
        if len(user) == 0 or len(id) == 0 or len(password) == 0:
            QMessageBox.warning(self.Super, '警告', '请补全管理员信息！')
            return
        elif not id.isdigit():
            QMessageBox.warning(self.Super, '警告', '管理员工号格式错误！')
            return
        else:
            admin = {'id': id, 'user': user, 'password': password}
            try:
                self.WHU_DB.insert_admin(admin)
                QMessageBox.information(self.Super, '通知', '添加管理员成功！')
                self.Super.lineEdit_3.clear()
                self.Super.lineEdit_2.clear()
                self.Super.lineEdit_4.clear()
            except Exception as e:
                print(e)

    # 实现查找管理员
    def find_admin(self):
        id = self.Super.lineEdit.text()
        if len(id) == 0:
            admins = self.WHU_DB.show_admin()
            print(admins)
            if not len(admins) == 0:
                try:
                    self.Super.tableWidget.clearContents()
                    self.Super.tableWidget.setRowCount(0)
                    for line in admins:
                        currentRowCount = self.Super.tableWidget.rowCount()
                        self.Super.tableWidget.insertRow(currentRowCount)
                        self.Super.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(line['admin_id'])))
                        self.Super.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(line['admin_user']))
                        self.Super.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(line['admin_password']))
                        self.Super.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                    print("浏览管理员成功")
                except Exception as e:
                    print(e)
            else:
                QMessageBox.warning(self.Super, '警告', '暂无管理员信息！')

        elif not id.isdigit():
            QMessageBox.warning(self.Super, '警告', '管理员工号格式错误！')
            return
        else:
            try:
                results = self.WHU_DB.search_admin(id)
                if len(results) == 0:
                    QMessageBox.warning(self.Super, '警告', '未找到管理员，请检查工号是否正确！')
                    return
                else:
                    self.Super.tableWidget.clearContents()
                    self.Super.tableWidget.setRowCount(0)
                    currentRowCount = self.Super.tableWidget.rowCount()
                    self.Super.tableWidget.insertRow(currentRowCount)
                    self.Super.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(results[0][1])))
                    self.Super.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(results[0][0]))
                    self.Super.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(results[0][2]))
                    self.Super.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            except Exception as e:
                print(e)

    # 实现删除管理员
    def delete_admin(self):
        id = self.Super.lineEdit_5.text()
        if len(id) == 0:
            QMessageBox.warning(self.Super, '警告', '请补全工号！')
            return
        elif not id.isdigit():
            QMessageBox.warning(self.Super, '警告', '管理员工号格式错误！')
            return
        else:
            results = self.WHU_DB.search_admin(id)
            if len(results) == 0:
                QMessageBox.warning(self.Super, '警告', '未找到管理员，请检查工号是否正确！')
                return
            else:
                reply = QMessageBox.question(self.Super,
                                             '询问',
                                             "确定要删除该管理员吗？",
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    try:
                        self.WHU_DB.admin_delete(id)
                        self.Super.lineEdit_5.clear()
                        QMessageBox.information(self.Super, '通知', '删除管理员成功！')
                    except Exception as e:
                        print(e)
                else:
                    pass

    # 实现读者注册（添加读者）
    def add_reader(self):
        user = self.Register.lineEdit_4.text()
        password = self.Register.lineEdit_2.text()
        name = self.Register.lineEdit_5.text()
        dep = self.Register.lineEdit_6.text()
        id = self.Register.lineEdit_7.text()
        if len(user) == 0 or len(id) == 0 or len(password) == 0 or len(name) == 0 or len(dep) == 0:
            QMessageBox.warning(self.Register, '警告', '请补全用户信息！')
            return
        elif not id.isdigit():
            QMessageBox.warning(self.Register, '警告', '学号格式错误！')
            return
        else:
            reader = {'id': id, 'name': name, 'password': password, 'dep': dep, 'user': user}
            try:
                self.WHU_DB.insert_reader(reader)
                QMessageBox.information(self.Register, '通知', '用户注册成功！')
                self.Register.close()
                self.displayReader()

            except Exception as e:
                print(e)

    # 实现借书
    def borrow_book(self):
        book_id = self.Reader.lineEdit_7.text()
        if len(book_id) == 0:
            QMessageBox.warning(self.Reader, '警告', '请填写借书索引')
        elif not book_id.isdigit():
            QMessageBox.warning(self.Reader, '警告', '索引格式错误')
        else:
            try:
                stu_id = self.CurrentReader
                return_num = self.WHU_DB.book_rent(book_id, stu_id)
                if return_num == 1:
                    QMessageBox.warning(self.Reader, '警告', '未找到要借的图书,请检查索引')
                if return_num == 2:
                    QMessageBox.warning(self.Reader, '警告', '该图书已被借阅')
                if return_num == 3:
                    QMessageBox.information(self.Reader, '通知', '借阅成功！')
                    self.Reader.lineEdit_7.clear()
                if return_num == 4:
                    QMessageBox.warning(self.Reader, '警告', '有bug')
                results = self.WHU_DB.browse_rent(stu_id)
                self.Reader.tableWidget_2.clearContents()
                self.Reader.tableWidget_2.setRowCount(0)
                if not len(results) == 0:
                    for line in results:
                        searched_book = {'id': line[0], 'name': '', 'author': '', 'pubdate': ''}
                        book = self.WHU_DB.search_book(searched_book)
                        print(book)
                        currentRowCount = self.Reader.tableWidget_2.rowCount()
                        self.Reader.tableWidget_2.insertRow(currentRowCount)
                        self.Reader.tableWidget_2.setItem(currentRowCount, 0, QTableWidgetItem(book[0][0]))
                        self.Reader.tableWidget_2.setItem(currentRowCount, 1, QTableWidgetItem(book[0][2]))
                        self.Reader.tableWidget_2.setItem(currentRowCount, 2,
                                                          QTableWidgetItem(str(book[0][3].strftime('%Y-%m-%d'))))
                        self.Reader.tableWidget_2.setItem(currentRowCount, 3, QTableWidgetItem(str(book[0][1])))
                        self.Reader.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
            except Exception as e:
                print(e)

    # 实现还书
    def return_book(self):
        book_id = self.Reader.lineEdit_13.text()
        if len(book_id) == 0:
            QMessageBox.warning(self.Reader, '警告', '请填写还书索引')
        elif not book_id.isdigit():
            QMessageBox.warning(self.Reader, '警告', '索引格式错误')
        else:
            try:
                stu_id = self.CurrentReader
                return_num = self.WHU_DB.book_return(book_id, stu_id)
                if return_num == 1:
                    QMessageBox.warning(self.Reader, '警告', '未找到要还的图书,请检查索引')
                if return_num == 2:
                    QMessageBox.warning(self.Reader, '警告', '该图书未被借阅')
                if return_num == 3:
                    QMessageBox.warning(self.Reader, '警告', '无权归还此书')
                if return_num == 4:
                    QMessageBox.information(self.Reader, '通知', '归还成功！')
                    self.Reader.lineEdit_13.clear()
                if return_num == 5:
                    QMessageBox.warning(self.Reader, '警告', '有bug')
                results = self.WHU_DB.browse_rent(stu_id)
                self.Reader.tableWidget_2.clearContents()
                self.Reader.tableWidget_2.setRowCount(0)
                if not len(results) == 0:
                    for line in results:
                        searched_book = {'id': line[0], 'name': '', 'author': '', 'pubdate': ''}
                        book = self.WHU_DB.search_book(searched_book)
                        print(book)
                        currentRowCount = self.Reader.tableWidget_2.rowCount()
                        self.Reader.tableWidget_2.insertRow(currentRowCount)
                        self.Reader.tableWidget_2.setItem(currentRowCount, 0, QTableWidgetItem(book[0][0]))
                        self.Reader.tableWidget_2.setItem(currentRowCount, 1, QTableWidgetItem(book[0][2]))
                        self.Reader.tableWidget_2.setItem(currentRowCount, 2,
                                                          QTableWidgetItem(str(book[0][3].strftime('%Y-%m-%d'))))
                        self.Reader.tableWidget_2.setItem(currentRowCount, 3, QTableWidgetItem(str(book[0][1])))
                        self.Reader.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
            except Exception as e:
                print(e)


# 管理员登录界面
class LoginAdmin(QWidget, Ui_LoginAdmin):
    def __init__(self, parent=None):
        super(LoginAdmin, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
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


# 读者登录界面
class LoginReader(QWidget, Ui_LoginReader):
    def __init__(self, parent=None):
        super(LoginReader, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
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


# 超级管理员登录界面
class LoginSuper(QWidget, Ui_LoginSuper):
    def __init__(self, parent=None):
        super(LoginSuper, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
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


# 读者注册界面
class Register(QWidget, Ui_Register):
    def __init__(self, parent=None):
        super(Register, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
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
