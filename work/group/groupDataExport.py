from openpyxl import load_workbook
from config.public_data import execl_group_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=execl_group_path)
ws = workbook["总用水,用电,用冷"]

db = MysqlUtil()

if __name__ == "__main__":
    for i in ws.rows:
        print(i)
