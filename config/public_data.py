import os

# 整个项目的根目录绝对路劲
baseDir = os.path.dirname(os.path.dirname(__file__))

# 数据库配置文件绝对路径
config_path = baseDir + "/config/db_config.ini"

# 租户Excel文件
excel_tenant_path = baseDir + "/在租合同能耗数据.xlsx"

# 设备分组数据
execl_group_path = baseDir + "/分组设备数据.xlsx"