from openpyxl import load_workbook
from config.public_data import excel_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=excel_path)
ws = workbook["Sheet16"]

db = MysqlUtil()
contract_map = {}
nn = {}


def selectContractList():
    # 获取合同列表
    sql = "select * from saas_solution_meter_reading.t_contract"
    return db.selectList(sql)


def selectStrategy(contract_id):
    sql = "select * from saas_solution_meter_reading.t_strategy where contract_id = '%s'" % contract_id
    return db.selectOne(sql)


def saveStrategyContractId(contract_id):
    sql = "INSERT INTO saas_solution_meter_reading.t_strategy(contract_id) VALUES ('%s') " % contract_id
    return db.save(sql)


def updateSBGT(contract_id, sbgt):
    sql = "UPDATE saas_solution_meter_reading.t_strategy SET sbgt = '%s' where contract_id = '%s'" % (sbgt, contract_id)
    return db.update(sql)


def updateSBZY(contract_id, sbzy):
    sql = "UPDATE saas_solution_meter_reading.t_strategy SET sbzy = '%s' where contract_id = '%s'" % (sbzy, contract_id)
    return db.update(sql)


def updateDBGT(contract_id, dbgt):
    sql = "UPDATE saas_solution_meter_reading.t_strategy SET dbgt = '%s' where contract_id = '%s'" % (dbgt, contract_id)
    return db.update(sql)


def updateDBZY(contract_id, dbzy):
    sql = "UPDATE saas_solution_meter_reading.t_strategy SET dbzy = '%s' where contract_id = '%s'" % (dbzy, contract_id)
    return db.update(sql)


def updateLLZY(contract_id, lz1, lz2, lz3, lz4):
    sql = "UPDATE saas_solution_meter_reading.t_strategy SET lz1 = '%s',lz2 = '%s',lz3 = '%s',lz4 = '%s'" \
          " where contract_id = '%s'" % (lz1, lz2, lz3, lz4, contract_id)
    return db.update(sql)


def updateLLGT(contract_id, lg1, lg2, lg3, lg4):
    sql = "UPDATE saas_solution_meter_reading.t_strategy SET lg1 = '%s',lg2 = '%s',lg3 = '%s',lg4 = '%s' " \
          "where contract_id = '%s'" % (lg1, lg2, lg3, lg4, contract_id)
    return db.update(sql)


if __name__ == "__main__":
    contract_list = selectContractList()
    for contract in contract_list:
        valid_from = str(contract['valid_from']) + " 00:00:00"
        valid_end = str(contract['valid_end']) + " 00:00:00"
        name = "_".join((str(contract['contract_code']), valid_from, valid_end))
        contract_map[name] = contract['id']
    for item in ws.rows:
        name = "_".join((str(item[0].value), str(item[1].value), str(item[2].value)))
        try:
            contractId = contract_map[name]
            data = selectStrategy(contractId)
            if data is not None:
                # 第一步：导入有效合同信息
                # saveStrategyContractId(contractId)
                if str(item[7].value) == "水表":
                    if str(item[8].value) == "公摊":
                        updateSBGT(contractId, str(item[3].value))
                    if str(item[8].value) == "自用":
                        updateSBZY(contractId, str(item[3].value))
                if str(item[7].value) == "电表":
                    if str(item[8].value) == "公摊":
                        updateDBGT(contractId, str(item[3].value))
                    if str(item[8].value) == "自用":
                        updateDBZY(contractId, str(item[3].value))
                if str(item[7].value) == "办公楼冷量":
                    if str(item[8].value) == "公摊":
                        updateLLGT(contractId, str(item[3].value), str(item[4].value), str(item[5].value),
                                   str(item[6].value))
                    if str(item[8].value) == "自用":
                        updateLLZY(contractId, str(item[3].value), str(item[4].value), str(item[5].value),
                                   str(item[6].value))
        except:
            print(name)
            pass
