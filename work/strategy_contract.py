from openpyxl import load_workbook
from config.public_data import excel_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=excel_path)
ws = workbook["Sheet17"]

db = MysqlUtil()


def update_strategy_id(fee_strategy, sbzy, sbgt, dbzy, dbgt, lz1, lz2, lz3, lz4, lg1, lg2, lg3, lg4):
    # 新增合同信息
    sql = "UPDATE saas_solution_meter_reading.t_strategy SET fee_strategy = '%s' where sbzy = '%s' and sbgt = '%s' " \
          "and dbzy = '%s' and dbgt = '%s' and lz1 = '%s' and lz2 = '%s' and lz3 = '%s' and lz4 = '%s'" \
          " and lg1 = '%s' and lg2 = '%s' and lg3 = '%s' and lg4 = '%s'" \
          % (fee_strategy, sbzy, sbgt, dbzy, dbgt, lz1, lz2, lz3, lz4, lg1, lg2, lg3, lg4)
    db.update(sql)


if __name__ == "__main__":
    # 计费策略与合同之间的关系
    for i in ws.rows:
        update_strategy_id(str(i[12].value), str(i[0].value), str(i[1].value), str(i[2].value), str(i[3].value),
                           str(i[4].value), str(i[5].value), str(i[6].value), str(i[7].value), str(i[8].value),
                           str(i[9].value), str(i[10].value), str(i[11].value))


# 更新合同表的租户计费策略关系
# UPDATE t_contract c, t_strategy s SET c.strategy_id = s.fee_strategy WHERE c.id = s.contract_id