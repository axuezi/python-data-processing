import json
import requests
from utils.mysql_util import MysqlUtil
from strategy_data import gt

db = MysqlUtil()


def selectList():
    sql = 'select sbzy,sbgt,dbzy,dbgt, lz1,lz2,lz3,lz4,lg1,lg2,lg3,lg4 from saas_solution_meter_reading.t_strategy ' \
          'group by sbzy, sbgt, dbzy, dbgt, lz1, lz2, lz3, lz4, lg1, lg2, lg3, lg4'
    return db.selectList(sql)


if __name__ == '__main__':
    url = "http://gateway-web.fat.svc.spaceiot.local:8000/solution/meter/reading/strategy/addStrategy"
    headers = {'content-type': "application/json", 'Authorization': 'Bearer 407cb895273e4c46a73b91c72b25dc1d',
               'accessToken': 'Bearer 407cb895273e4c46a73b91c72b25dc1d', 'x-space-projectcodes': 'ZH_00001_XM_00000001'}
    res = selectList()
    idx = 1
    for one in res:
        gt['subjectList'][0]['configList'][0]['configInfoList'][0]['price'] = str(one['sbzy'])
        gt['subjectList'][0]['configList'][1]['configInfoList'][0]['price'] = str(one['sbgt'])
        gt['subjectList'][1]['configList'][0]['configInfoList'][0]['price'] = str(one['dbzy'])
        gt['subjectList'][1]['configList'][1]['configInfoList'][0]['price'] = str(one['dbgt'])
        gt['subjectList'][2]['configList'][0]['configInfoList'][0]['price'] = str(one['lz1'])
        gt['subjectList'][2]['configList'][0]['configInfoList'][1]['price'] = str(one['lz2'])
        gt['subjectList'][2]['configList'][0]['configInfoList'][2]['price'] = str(one['lz3'])
        gt['subjectList'][2]['configList'][1]['configInfoList'][1]['price'] = str(one['lz2'])
        gt['subjectList'][2]['configList'][1]['configInfoList'][2]['price'] = str(one['lz3'])
        gt['subjectList'][2]['configList'][2]['configInfoList'][3]['price'] = str(one['lz4'])
        gt['subjectList'][2]['configList'][3]['configInfoList'][0]['price'] = str(one['lg1'])
        gt['subjectList'][2]['configList'][3]['configInfoList'][1]['price'] = str(one['lg2'])
        gt['subjectList'][2]['configList'][3]['configInfoList'][2]['price'] = str(one['lg3'])
        gt['subjectList'][2]['configList'][4]['configInfoList'][1]['price'] = str(one['lg2'])
        gt['subjectList'][2]['configList'][4]['configInfoList'][2]['price'] = str(one['lg3'])
        gt['subjectList'][2]['configList'][5]['configInfoList'][3]['price'] = str(one['lg4'])
        gt['strategyName'] = '科兴科学园计费策略-' + str(idx)
        requests.post(url=url, headers=headers, data=json.dumps(gt))
        idx = idx + 1
