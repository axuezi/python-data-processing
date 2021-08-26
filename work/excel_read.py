from openpyxl import load_workbook
from config.public_data import excel_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=excel_path)
ws = workbook["Sheet5"]

f = {}
# 读取全表
for i in ws.rows:
    f[str(i[15].value)] = i

print('集合元素个数为：' + str(len(f)))
s = f['CXM0001-010120190902089'][15].value

if __name__ == "__main__":
    sql = "select * from saas_solution_meter_reading.t_contract where contract_code = '%s'" % s
    r = MysqlUtil().selectOne(sql)
    print(r[5])
