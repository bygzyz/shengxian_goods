from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


# 使用peewee的连接池， 使用ReconnectMixin来防止出现连接断开查询失败
class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


MYSQL_DB = "mxshop_user_srv"
MYSQL_HOST = "1.117.229.170"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "yuwellmysql"

DB = ReconnectMysqlDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT,
                            user=MYSQL_USER, password=MYSQL_PASSWORD)
