import logging
import os
# flie_path=os.path.join(os.path.dirname(__file__),"my_logger.log")
from Log.log_config import conf


class MyLogger(logging.Logger):

    def __init__(self, file=None):
        # 下方注释这种需要在调用的时候传入参数
        # super().__init__(name,level)
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(conf.get("Log", "log_name"), conf.get("Log", "log_level"))

        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 判断配置文件中的file_ok为True或False
# 为True则会将运行日志写入文件
# 为False则不会写入文件,只会在控制台显示日志记录
if conf.getboolean("Log", "file_ok"):

    file = conf.get("Log", "file_name")
    file_path = os.path.join(os.path.dirname(__file__), file)
else:
    file_path = None

logger = MyLogger(file_path)
