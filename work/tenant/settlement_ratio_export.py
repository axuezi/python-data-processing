from openpyxl import load_workbook
from config.public_data import excel_tenant_path
from utils.mysql_util import MysqlUtil
from decimal import Decimal

workbook = load_workbook(filename=excel_tenant_path)
ws = workbook["Sheet12"]

db = MysqlUtil()
customer_map = {}


def select_internal_code(external_code):
    # 获取区域对应的CODE
    sql = "select internal_code from saas_ability_area.resource_info where external_code = '%s'" % external_code
    return db.selectList(sql)


def update_select_internal(share_ratio, settlement_ratio, area_code):
    # 更新公摊费率
    sql = "UPDATE saas_solution_meter_reading.t_rel_contract_area SET share_ratio = '%s', settlement_ratio = '%s' " \
          "where area_code = '%s' " % (share_ratio, settlement_ratio, area_code)
    return db.update(sql)


def select_share_ratio(area_code):
    # 查询公摊费率
    sql = "select share_ratio from saas_solution_meter_reading.t_rel_contract_area where area_code = '%s'" % area_code
    return db.selectOne(sql)


if __name__ == "__main__":
    # 更新费率，公摊比例
    for i in ws.rows:
        code = str(i[0].value)
        area = select_internal_code(code)
        internalCode = str(area[0]['internal_code'])
        contract_area = select_share_ratio(internalCode)
        shareRatio = contract_area["share_ratio"]
        pool = Decimal(shareRatio) * Decimal(i[3].value)
        update_select_internal(round(pool, 4), str(i[2].value), internalCode)
