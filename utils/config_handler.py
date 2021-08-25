from configparser import ConfigParser
from config.public_data import config_path


class ConfigParse(object):
    cfp = None

    def __init__(self):
        pass

    @classmethod
    def get_db_config(cls):
        # cls使用的类方法,cls就是指定本身
        cls.cfp = ConfigParser()
        cls.cfp.read(config_path)
        host = cls.cfp.get("mysql_conf", "host")
        port = cls.cfp.get("mysql_conf", "port")
        user = cls.cfp.get("mysql_conf", "user")
        password = cls.cfp.get("mysql_conf", "password")
        db = cls.cfp.get("mysql_conf", "db_name")
        return {"host": host, "port": port, "user": user, "password": password, "db": db}
