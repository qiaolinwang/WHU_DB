import pymysql
from pymysql import cursors


class Database:
    def __init__(self):
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


if __name__ == '__main__':
    WHU_DB = Database()
    test = {'id': 2020301152360, 'name': '假人', 'user': 'test', 'password': '12asdiuags', 'dep': '计算机学院'}
    WHU_DB.insert_reader(test)
    print(WHU_DB.show_reader())