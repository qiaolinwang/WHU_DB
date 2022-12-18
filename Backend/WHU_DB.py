import pymysql
from pymysql import cursors


class Database:
    def __init__(self):
        # 创建数据库whu_db 创建读者表whu_reader 创建管理员表whu_admin 创建图书表whu_book whu_rent
        # 将mysql参数改成本地参数
        self.host = "localhost"
        self.port = 3306
        self.user = 'root'
        self.password = '121517'
        self.charset = 'utf8'

        db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                             charset=self.charset)  # 连接数据库

        # 创建图书表
        cursor = db.cursor()  # 创建游标对象

        try:

            dbname = 'whu_db'
            sql = 'create database if not exists %s' % dbname  # 创建数据库
            cursor.execute(sql)

            print('创建数据库whu_db成功')

        except Exception as e:
            print(e)
            db.rollback()  # 回滚事务

        finally:
            cursor.close()
            db.close()  # 关闭数据库连接

        self.database = "whu_db"

        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                             port=self.port,
                             charset=self.charset)

        cursor = db.cursor()  # 创建游标对象

        try:

            tableName = 'whu_book'
            sql = """create table if not exists whu_book(name VARCHAR(40),id BIGINT,author VARCHAR(40),pubdate DATE,
            PRIMARY KEY(id)) """
            cursor.execute(sql)  # 执行sql语句，创建表
            print('创建表whu_book成功')
            sql2 = "ALTER TABLE whu_book \
        ADD rent_stu_id BIGINT DEFAULT -1"
            cursor.execute(sql2)
            sql = 'desc %s' % tableName
            cursor.execute(sql)
            print('whu_book表结构:', cursor.fetchall())  # 显示表结构

        except Exception as e:
            print(e)
            db.rollback()  # 回滚事务

        finally:
            cursor.close()
            db.close()  # 关闭数据库连接

        # 创建读者表

        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                             port=self.port,
                             charset=self.charset)

        cursor = db.cursor()  # 创建游标对象

        try:

            tableName = 'whu_reader'
            sql = """create table if not exists whu_reader(stu_name VARCHAR(40),stu_id BIGINT,stu_user VARCHAR(40),
            stu_password VARCHAR(40),stu_dep VARCHAR(40),PRIMARY KEY(stu_id)) """
            cursor.execute(sql)  # 执行sql语句，创建表
            print('创建表whu_reader表成功')
            sql = 'desc %s' % tableName
            cursor.execute(sql)
            print('whu_reader表结构:', cursor.fetchall())  # 显示表结构

        except Exception as e:
            print(e)
            db.rollback()  # 回滚事务

        finally:
            cursor.close()
            db.close()  # 关闭数据库连接

        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                             port=self.port,
                             charset=self.charset)

        cursor = db.cursor()  # 创建游标对象

        try:

            tableName = 'whu_admin'
            sql = """create table if not exists whu_admin(admin_user VARCHAR(40),admin_id BIGINT,admin_password 
            VARCHAR(40),PRIMARY KEY(admin_id)) """
            cursor.execute(sql)  # 执行sql语句，创建表
            print('创建表whu_admin表成功')
            sql = 'desc %s' % tableName
            cursor.execute(sql)
            print('whu_admin表结构:', cursor.fetchall())  # 显示表结构

        except Exception as e:
            print(e)
            db.rollback()  # 回滚事务

        finally:
            cursor.close()
            db.close()  # 关闭数据库连接

        # 创建借阅者表
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                             port=self.port,
                             charset=self.charset)

        cursor = db.cursor()  # 创建游标对象

        try:

            tableName = 'whu_rent'
            sql = """create table if not exists whu_rent(stu_id BIGINT,book_id BIGINT,PRIMARY KEY(book_id)) """
            cursor.execute(sql)  # 执行sql语句，创建表
            print('创建表whu_rent表成功')
            sql = 'desc %s' % tableName
            cursor.execute(sql)
            print('whu_rent表结构:', cursor.fetchall())  # 显示表结构

        except Exception as e:
            print(e)
            db.rollback()  # 回滚事务

        finally:
            cursor.close()
            db.close()  # 关闭数据库连接

    # 实现浏览图书信息
    def show_book(self):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
        cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
        # 写sql语句
        sql = "select * from whu_book"
        try:
            cur.execute(sql)
            books = cur.fetchall()
            """
                此处判断很重要，如果数据库中没有记录，则会结果是一个空的元组类型，
                如果有记录，则结果是list类型，所以可以根据类型来判断数据库是否为空，
                如果不是就返回一个空列表。
            """
            if type(books) == list:
                print("成功获取whu_book中数据！")
                return books
            else:
                print("whu_book表为空")
                return []

        except Exception as e:
            raise e
        finally:
            connection.close()  # 关闭连接

    # 实现浏览管理员信息
    def show_admin(self):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
        cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
        # 写sql语句
        sql = "select * from whu_admin"
        try:
            cur.execute(sql)
            admins = cur.fetchall()
            """
                此处判断很重要，如果数据库中没有记录，则会结果是一个空的元组类型，
                如果有记录，则结果是list类型，所以可以根据类型来判断数据库是否为空，
                如果不是就返回一个空列表。
            """
            if type(admins) == list:
                print("成功获取whu_admin中数据！")
                return admins
            else:
                print("whu_admin表为空")
                return []

        except Exception as e:
            raise e
        finally:
            connection.close()  # 关闭连接

    # 实现浏览读者信息
    def show_reader(self):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
        cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
        # 写sql语句
        sql = "select * from whu_reader"
        try:
            cur.execute(sql)
            readers = cur.fetchall()
            """
                此处判断很重要，如果数据库中没有记录，则会结果是一个空的元组类型，
                如果有记录，则结果是list类型，所以可以根据类型来判断数据库是否为空，
                如果不是就返回一个空列表。
            """
            if type(readers) == list:
                print("成功获取whu_reader中数据！")
                return readers
            else:
                print("whu_reader表为空")
                return []

        except Exception as e:
            raise e
        finally:
            connection.close()  # 关闭连接

    # 实现添加图书
    def insert_book(self, book):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
        cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
        # 写sql语句
        sql = "insert into whu_book(name,id,author,pubdate) values('%s','%s','%s','%s')"
        id = book['id']
        name = book['name']
        author = book['author']
        pubdate = book['pubdate']
        try:
            cur.execute(sql % (name, id, author, pubdate))
            connection.commit()
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 图书查找
    def search_book(self, book):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()

        id = book['id']
        name = book['name']
        author = book['author']
        pubdate = book['pubdate']
        if id == -1:
            if not len(name) == 0 and len(author) == 0 and len(pubdate) == 0:
                sql = "select * from whu_book where name = '%s'" % name
            elif len(name) == 0 and not len(author) == 0 and len(pubdate) == 0:
                sql = "select * from whu_book where author = '%s'" % author
            elif len(name) == 0 and len(author) == 0 and not len(pubdate) == 0:
                sql = "select * from whu_book where pubdate = '%s'" % pubdate
            elif not len(name) == 0 and not len(author) == 0 and len(pubdate) == 0:
                sql = "select * from whu_book where name = '%s' and author = '%s'" % (name, author)
            elif not len(name) == 0 and len(author) == 0 and not len(pubdate) == 0:
                sql = "select * from whu_book where name = '%s' and pubdate = '%s'" % (name, pubdate)
            elif len(name) == 0 and not len(author) == 0 and not len(pubdate) == 0:
                sql = "select * from whu_book where author = '%s' and pubdate = '%s'" % (author, pubdate)
            elif not len(name) == 0 and not len(author) == 0 and not len(pubdate) == 0:
                sql = "select * from whu_book where name = '%s' and author = '%s' and pubdate = '%s'" % (
                    name, author, pubdate)
            else:
                print("查找格式错误")
                connection.close()
                return

            try:
                # 执行sql语句
                cur.execute(sql)
                # 获取所有记录列表
                results = cur.fetchall()
                print(results)
                if not len(results) == 0:
                    print("查找成功！")
                    return results
                else:
                    print("未找到")
                    return []
            except Exception as e:
                # 错误回滚
                connection.rollback()
                raise e
            finally:
                connection.close()  # 关闭连接

        else:
            id = book['id']
            print(id)
            sql = "select * from whu_book where id = '%s'" % id
            try:
                # 执行sql语句
                cur.execute(sql)
                # 获取所有记录列表
                results = cur.fetchall()
                if not len(results) == 0:
                    print("查找成功！")
                    return results
                else:
                    print("未找到")
                    return []
            except Exception as e:
                # 错误回滚
                connection.rollback()
                raise e
            finally:
                connection.close()  # 关闭连接

    # 由于读者界面的查找出版时间是个范围 又写了个查找函数
    def reader_search_book(self, book):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        id = book['id']
        name = book['name']
        author = book['author']
        fardate = book['fardate']
        neardate = book['neardate']
        if id == -1:
            if not len(name) == 0 and len(author) == 0 and len(fardate) == 0 and len(neardate) == 0:
                sql = "select * from whu_book where name = '%s'" % name
            elif len(name) == 0 and not len(author) == 0 and len(fardate) == 0 and len(neardate) == 0:
                sql = "select * from whu_book where author = '%s'" % author
            elif len(name) == 0 and len(author) == 0 and not len(fardate) == 0 and not len(neardate) == 0:
                sql = "select * from whu_book where pubdate between '%s' and '%s'" % (fardate, neardate)
            elif not len(name) == 0 and not len(author) == 0 and len(fardate) == 0 and len(neardate) == 0:
                sql = "select * from whu_book where name = '%s' and author = '%s'" % (name, author)
            elif not len(name) == 0 and len(author) == 0 and not len(fardate) == 0 and not len(neardate) == 0:
                sql = "select * from whu_book where name = '%s' and pubdate between '%s' and '%s'" % (
                    name, fardate, neardate)
            elif len(name) == 0 and not len(author) == 0 and not len(fardate) == 0 and not len(neardate) == 0:
                sql = "select * from whu_book where author = '%s' pubdate between '%s' and '%s'" % (
                    author, fardate, neardate)
            elif not len(name) == 0 and not len(author) == 0 and not len(fardate) == 0 and not len(neardate) == 0:
                sql = "select * from whu_book where name = '%s' and author = '%s' and pubdate between '%s' and '%s'" % (
                    name, author, fardate, neardate)
            else:
                print("查找格式错误")
                connection.close()
                return

            try:
                # 执行sql语句
                cur.execute(sql)
                # 获取所有记录列表
                results = cur.fetchall()
                print(results)
                if not len(results) == 0:
                    print("查找成功！")
                    return results
                else:
                    print("未找到")
                    return []
            except Exception as e:
                # 错误回滚
                connection.rollback()
                raise e
            finally:
                connection.close()  # 关闭连接

        else:
            id = book['id']
            print(id)
            sql = "select * from whu_book where id = '%s'" % id
            try:
                # 执行sql语句
                cur.execute(sql)
                # 获取所有记录列表
                results = cur.fetchall()
                if not len(results) == 0:
                    print("查找成功！")
                    return results
                else:
                    print("未找到")
                    return []
            except Exception as e:
                # 错误回滚
                connection.rollback()
                raise e
            finally:
                connection.close()  # 关闭连接

    # 实现添加读者
    def insert_reader(self, reader):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
        cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
        # 写sql语句
        sql = "insert into whu_reader(stu_name,stu_id,stu_user,stu_password,stu_dep) values('%s','%s','%s','%s','%s')"
        id = reader['id']
        name = reader['name']
        password = reader['password']
        user = reader['user']
        dep = reader['dep']
        try:
            cur.execute(sql % (name, id, user, password, dep))
            connection.commit()
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 添加管理员信息
    def insert_admin(self, admin):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
        cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
        # 写sql语句
        sql = "insert into whu_admin(admin_user,admin_id,admin_password) values('%s','%s','%s')"
        id = admin['id']
        user = admin['user']
        password = admin['password']
        try:
            cur.execute(sql % (user, id, password))
            connection.commit()
            print("添加管理员成功")
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 删除管理员
    def admin_delete(self, index):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        sql = "delete from whu_admin where admin_id = '%s'"
        try:
            cur.execute(sql % index)
            connection.commit()
            print("删除管理员成功")
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 查找管理员
    def search_admin(self, id):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        sql = "select * from whu_admin where admin_id = '%s'" % id
        try:
            # 执行sql语句
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            if not len(results) == 0:
                print("查找管理员成功！")
                return results
            else:
                print("未找到管理员")
                return []
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 实现管理员登录
    def login_admin(self, id, password):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        sql = "select * from whu_admin where admin_id = '%s' and admin_password = '%s'" % (id, password)
        try:
            # 执行sql语句
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            if not len(results) == 0:
                print("登录管理员成功！")
                return True
            else:
                print("未找到管理员")
                return False
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 实现读者登录
    def login_reader(self, id, password):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        sql = "select * from whu_reader where stu_id = '%s' and stu_password = '%s'" % (id, password)
        try:
            # 执行sql语句
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            if not len(results) == 0:
                print("登录读者成功！")
                return True
            else:
                print("未找到该读者")
                return False
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 修改图书信息
    def book_modify(self, book):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        id = book['id']
        name = book['name']
        author = book['author']
        pubdate = book['pubdate']
        sql = "update whu_book set name='%s',author='%s',pubdate='%s' where id='%s'"
        try:
            cur.execute(sql % (name, author, pubdate, id))
            connection.commit()
            print("修改图书成功")
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 删除图书
    def book_delete(self, index):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        sql = "delete from whu_book where id = '%s'"
        try:
            cur.execute(sql % index)
            connection.commit()
            print("删除图书成功")
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 实现修改读者
    def reader_modify(self, reader):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()
        id = reader['id']
        oldpassword = reader['oldpassword']
        newpassword = reader['newpassword']
        name = reader['name']
        dep = reader['dep']
        sql1 = "select * from whu_reader where stu_id = '%s' and stu_password = '%s'"
        sql2 = "update whu_reader set stu_name='%s',stu_password='%s',stu_dep='%s' where stu_id='%s'"
        try:
            cur.execute(sql1 % (id, oldpassword))
            # 获取所有记录列表
            results = cur.fetchall()
            if len(results) == 0:
                print("未找到要修改的读者")
                return False
            else:
                cur.execute(sql2 % (name, newpassword, dep, id))
                connection.commit()
                print("修改读者成功")
                return True
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接

    # 实现读者借书
    def book_rent(self, book_id, stu_id):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)

        cur = connection.cursor()  # 创建游标对象
        if not stu_id == -1:
            try:
                sql_check = "select * from whu_book where id = '%s'" % book_id
                cur.execute(sql_check)
                results = cur.fetchall()
                if len(results) == 0:
                    print("未找到要借的图书")
                    return 1
                else:
                    sql_check_borrow = "select * from whu_rent where book_id = '%s'" % book_id
                    cur.execute(sql_check_borrow)
                    results2 = cur.fetchall()
                    if not len(results2) == 0:
                        print("该图书已被借阅")
                        return 2
                    else:
                        sql_borrow = "update whu_book set rent_stu_id ='%s' where id='%s'"
                        sql_borrow2 = "insert into whu_rent(stu_id,book_id) values('%s','%s')"
                        cur.execute(sql_borrow % (stu_id, book_id))
                        connection.commit()
                        cur.execute(sql_borrow2 % (stu_id, book_id))
                        connection.commit()
                        print("借书成功")
                        return 3
            except Exception as e:
                # 错误回滚
                connection.rollback()
                raise e
            finally:
                connection.close()  # 关闭连接
        else:
            connection.close()  # 关闭连接
            return 4

    # 实现还书
    def book_return(self, book_id, stu_id):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)

        cur = connection.cursor()  # 创建游标对象
        if not stu_id == -1:
            try:
                sql_check = "select * from whu_book where id = '%s'" % book_id
                cur.execute(sql_check)
                results = cur.fetchall()
                if len(results) == 0:
                    print("未找到要还的图书")
                    return 1
                else:
                    sql_check_borrow = "select * from whu_rent where book_id = '%s'" % book_id
                    cur.execute(sql_check_borrow)
                    results2 = cur.fetchall()
                    if len(results2) == 0:
                        print("该图书未被借阅")
                        return 2
                    else:
                        if not str(results2[0][0]) == str(stu_id):
                            print("无权归还此书")
                            return 3
                        else:
                            stu_id2 = -1
                            sql_return = "delete from whu_rent where book_id = '%s'"
                            sql_return2 = "update whu_book set rent_stu_id ='%s' where id='%s'"
                            cur.execute(sql_return % (book_id))
                            connection.commit()
                            cur.execute(sql_return2 % (stu_id2, book_id))
                            connection.commit()
                            print("还书成功")
                            return 4
            except Exception as e:
                # 错误回滚
                connection.rollback()
                raise e
            finally:
                connection.close()  # 关闭连接
        else:
            connection.close()  # 关闭连接
            return 5

    def browse_rent(self, stu_id):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        cur = connection.cursor()  # 创建游标对象
        try:
            sql = "select book_id from whu_rent where stu_id = '%s'"
            cur.execute(sql % stu_id)
            results = cur.fetchall()
            return results
        except Exception as e:
            # 错误回滚
            connection.rollback()
            raise e
        finally:
            connection.close()  # 关闭连接



if __name__ == '__main__':
    WHU_DB = Database()
    test = {'id': 10001, 'name': '', 'author': '', 'pubdate': ''}
    WHU_DB.search_book(test)
    print(WHU_DB.show_book())
