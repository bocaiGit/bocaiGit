import yaml


class Business_flow_response_data:
    def __init__(self):
        """
        此方法是用来读取yaml文件中的请求参数
        此方法读取的文件属于业务测试的数据文件,请勿更改
        """
        with open(r"G:\order_huijiedan\data\ Business_flow_test_response_data.yaml", encoding="utf-8") as fs:
            data = yaml.safe_load(fs)
            # 多店铺解密的响应数据数据
            self.test_multi_store_order_decryption_data = data["多店铺解密响应数据"]
            # 多店铺修改地址的响应数据
            self.test_Multi_store_order_modification_address_data = data["多店铺修改收件地址响应数据"]


Bu_response_data = Business_flow_response_data()
