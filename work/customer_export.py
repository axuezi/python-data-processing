from openpyxl import load_workbook
from config.public_data import excel_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=excel_path)
ws = workbook["Sheet5"]

if __name__ == "__main__":
    for i in ws.rows:
        s = str(i[0].value)
        sql = "INSERT INTO saas_solution_meter_reading.t_customer (tenement_code, project_code, customer_name, " \
              "lease_status, version, create_time, create_by, update_time, update_by, logic_del) VALUES " \
              "('ZH_00001', 'ZH_00001_XM_00000001', '%s', '0', 1, '2021-08-24 14:15:38', null, " \
              "'2021-08-24 14:15:42', null, 0)" % s
        MysqlUtil().save(sql)
