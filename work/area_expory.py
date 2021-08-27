from utils.mysql_util import MysqlUtil

db = MysqlUtil()


def selectContractArea():
    sql = "select * from saas_solution_meter_reading.t_rel_contract_area"
    return db.selectList(sql)


def selectArea(internal_code):
    sql = "select convert(ri1.area / ri2.area, decimal(15, 4)) as area from saas_ability_area.resource_info ri1 " \
          "left join saas_ability_area.resource_info ri2 on ri1.internal_parent_code = ri2.internal_code " \
          "where ri1.internal_code = '%s'" % internal_code
    return db.selectOne(sql)


def updateContractArea(share_ratio, contract_area_id):
    sql = "update saas_solution_meter_reading.t_rel_contract_area set share_ratio = '%s' where id = '%s'" \
          % (share_ratio, contract_area_id)
    return db.update(sql)


if __name__ == "__main__":
    # 更新公摊比例
    contract_areas = selectContractArea()
    for contract_area in contract_areas:
        area = selectArea(contract_area['area_code'])
        updateContractArea(area['area'], contract_area['id'])
