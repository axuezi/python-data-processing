from openpyxl import load_workbook
from config.public_data import excel_path
from utils.mysql_util import MysqlUtil

workbook = load_workbook(filename=excel_path)
ws = workbook["Sheet10"]

db = MysqlUtil()
contract_area_map = {}
contract_map = {}


def selectContractList():
    # 获取合同列表
    sql = "select * from saas_solution_meter_reading.t_contract"
    return db.selectList(sql)


def selectArea(external_code):
    sql = "select ri.internal_code, ta.id_path from saas_ability_area.resource_info ri left " \
          "join saas_ability_area.t_area ta on ri.internal_code = ta.code where external_code =  '%s'" % external_code
    return db.selectOne(sql)


def save(contract_id, id_path, area_code, share_ratio, settlement_ratio):
    sql = "INSERT INTO saas_solution_meter_reading.t_rel_contract_area (tenement_code, project_code, contract_id, " \
          "id_path, area_code, share_ratio, settlement_ratio, share_area_code, version, create_time, create_by, " \
          "update_time, update_by, logic_del) VALUES ('ZH_00001', 'ZH_00001_XM_00000001', '%s', '%s', '%s', " \
          "'%s', '%s', null, 1, '2021-08-24 15:01:52', null, '2021-08-24 15:01:54', null, 0)" \
          % (contract_id, id_path, area_code, share_ratio, settlement_ratio)
    return db.save(sql)


if __name__ == "__main__":
    contract_list = selectContractList()
    for contract in contract_list:
        valid_from = str(contract['valid_from']) + " 00:00:00"
        valid_end = str(contract['valid_end']) + " 00:00:00"
        name = "_".join((str(contract['contract_code']), valid_from, valid_end))
        contract_map[name] = contract['id']
    for item in ws.rows:
        name = "_".join((str(item[0].value), str(item[1].value), str(item[2].value)))
        area_codes = item[3].value.split(',')
        for area_code in area_codes:
            try:
                contractId = contract_map[name]
                area = selectArea(area_code)
                save(contractId, area['id_path'], area['internal_code'], 1, 1)
            except:
                print(name)
                pass
