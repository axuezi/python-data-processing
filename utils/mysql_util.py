import pymysql
from utils.config_handler import ConfigParse


class MysqlUtil:
    """mysql util"""

    def __init__(self):
        # 获取mysql连接信息
        self.db_conf = ConfigParse.get_db_config()
        # 获取连接对象
        self.conn = pymysql.connect(
            host=self.db_conf["host"],
            port=int(self.db_conf["port"]),
            user=self.db_conf["user"],
            password=self.db_conf["password"],
            database=self.db_conf["db"],
            charset="utf8"
        )
        # 获取数据的游标
        self.cur = self.conn.cursor()
        print(">>>>>>>>数据库链接成功<<<<<<<<")

    # 关闭链接
    def close_connect(self):
        # 关闭数据连接
        # 提交，物理存储
        self.conn.commit()
        # 游标关闭
        self.cur.close()
        # 连接对象关闭
        self.conn.close()

    # 查询列表数据
    def selectList(self, sql):
        print("执行sql打印 >>> " + sql)
        res = None
        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
        except Exception as e:
            print("查询失败！" + str(e))
        return list(res)

    # 查询一条数据
    def selectOne(self, sql):
        print("执行sql打印 >>> " + sql)
        res = None
        try:
            self.cur.execute(sql)
            res = self.cur.fetchone()
        except Exception as e:
            print("查询失败！" + str(e))
        return res

    # 保存数据
    def save(self, sql):
        return self.__insert(sql)

    # 更新数据
    def update(self, sql):
        return self.__insert(sql)

    # 删除数据
    def delete(self, sql):
        return self.__insert(sql)

    # 插入数据
    def __insert(self, sql):
        print("执行sql打印 >>> " + sql)
        count = 0
        try:
            self.cur.execute(sql)
            self.conn.commit()
            count = count + 1
        except Exception as e:
            print("操作失败！" + str(e))
            self.conn.rollback()
        return count
