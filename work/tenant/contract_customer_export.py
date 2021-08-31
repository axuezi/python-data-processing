from openpyxl import load_workbook
from config.public_data import excel_tenant_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=excel_tenant_path)
ws = workbook["Sheet8"]

db = MysqlUtil()
customer_map = {}


def selectList():
    # 获取所有的租户数据
    sql = "select id, customer_name from saas_solution_meter_reading.t_customer where logic_del = 0"
    return db.selectList(sql)


def updateCustomerCode(customer_code, contract_code):
    # 更新合同表的租户ID
    sql = "update saas_solution_meter_reading.t_contract set customer_code = '%s' where contract_code = '%s'" \
          % (customer_code, contract_code)
    return db.update(sql)


if __name__ == "__main__":
    customer_list = selectList()
    for item in customer_list:
        # 转map key:customer_name, value:id
        customer_map[str(item["customer_name"])] = item['id']
    for i in ws.rows:
        name = str(i[0].value)
        # 根据name获取code
        code = customer_map[name]
        contract_id = str(i[1].value)
        updateCustomerCode(code, contract_id)
