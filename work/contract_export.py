from openpyxl import load_workbook
from config.public_data import excel_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=excel_path)
ws = workbook["Sheet7"]

db = MysqlUtil()


def save(contract_code, valid_from, valid_end):
    # 新增合同信息
    sql = "INSERT INTO saas_solution_meter_reading.t_contract (tenement_code, project_code, contract_code, " \
          "customer_code, strategy_id, valid_from, valid_end, cancellation_time, lease_status, lease_mode, version, " \
          "create_time, create_by, update_time, update_by, logic_del)" \
          " VALUES ('ZH_00001', 'ZH_00001_XM_00000001', '%s', null, null, '%s', '%s', null, '0', null, 1, " \
          "'2021-08-25 20:52:21', null, '2021-08-25 20:52:23', null, 0)" \
          % (contract_code, valid_from, valid_end)
    db.save(sql)


def selectOne(contract_code):
    # 根据合同Code获取合同信息
    sql = "select * from saas_solution_meter_reading.t_contract where contract_code = '%s' " % contract_code
    return db.selectOne(sql)


def update(contract_code, valid_from, valid_end):
    # 更新合同信息
    sql = "UPDATE saas_solution_meter_reading.t_contract SET valid_from = '%s', valid_end = '%s'  where " \
          "contract_code = '%s' " % (valid_from, valid_end, contract_code)
    db.update(sql)


if __name__ == "__main__":
    for i in ws.rows:
        name = str(i[0].value)
        code = str(i[1].value)
        start = str(i[2].value)
        end = str(i[3].value)
        # 查询是否存在
        r = selectOne(code)
        if r is not None:
            # 存在 -> 判断当前截至日期是否大于数据库已存在截至日期
            endDate = str(r['valid_end'])
            if end > endDate:
                update(code, start, end)
        else:
            # 不存在，直接新增
            save(code, start, end)
