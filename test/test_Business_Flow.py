import time
import pytest
import yaml

from asse.Assertion_Encapsulation import Assert_Encapsulation
# 封装的断言模块
from api.Business_Flow import Business_Flow_api
# 业务流测试的请求api
from data.Business_flow_test_data import Bf_request_data
# 请求数据
from data.Business_flow_test_resp_data import Bu_response_data
from jsonpath import jsonpath
from Log.my_log import logger


class Test_Business_Flow:
    busin_flow = Business_Flow_api()

    def setup_class(self):
        logger.info("""
                =====================================业务流测试====================================
                 ====================开始时间:{}=============================
                     """.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    def teardown_class(self):
        logger.info("""
                =====================================业务流测试====================================
                 ====================结束时间:{}=============================
                     """.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    @pytest.mark.parametrize("data", Bf_request_data.test_multi_store_order_decryption_data,
                             ids=["t_1497093616947_0277店铺第一次解密", "t_1497093616947_0277店铺第二次解密", "wangweilon店铺第一次解密",
                                  "wangweilon店铺第二次解密"])
    def test_multi_store_order_decryption(self, data):
        """
        多店铺订单解密,此解密不需要跟换测试数据
        :return:
        """
        Assert_Encapsulation(
            lnterface=(jsonpath(self.busin_flow.Multi_store_order_decryption(data), "$..receiver_name")[0]),
            response=Bu_response_data.test_multi_store_order_decryption_data)

    ids = ["t_1497093616947_0277店铺第一次修改地址", "t_1497093616947_0277店铺第二次修改地址", "wangweilon店铺第一次修改地址",
           "wangweilon店铺第二次修改地址", "t_1497093616947_0277店铺第三次修改地址", "t_1497093616947_0277店铺第四次修改地址",
           "wangweilon店铺第三次修改地址", "wangweilon店铺第四次修改地址"
           ]

    @pytest.mark.parametrize("data", Bf_request_data.test_Multi_store_order_modification_address_data[0], ids=ids)
    def test_Multi_store_order_modification_address(self, data):
        """
        多店铺修改地址
        :param data: 存放在yaml文件中的测试数据,请求数据,响应数据
        :return:
        """
        Assert_Encapsulation(lnterface=self.busin_flow.Multi_store_order_modification_address(data),
                             response=Bu_response_data.test_Multi_store_order_modification_address_data)
