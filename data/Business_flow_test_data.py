import yaml


class Business_flow_request_data:
    def __init__(self):
        """
        此方法是用来读取yaml文件中的请求参数
        此方法读取的文件属于业务测试的数据文件,请勿更改
        """
        with open(r"G:\order_huijiedan\data\Business_flow_test_request_data.yaml", encoding="utf-8") as fs:
            data = yaml.safe_load(fs)
            # 多店铺解密的请求数据
            self.test_multi_store_order_decryption_data = data["多店铺解密请求数据"]
            # 多店铺修改地址的请求数据
            self.test_Multi_store_order_modification_address_data = data["多店铺修改收件地址请求数据"]
            # 多店铺批量取号接口数据总和[取号前验证,取号,取号后验证是否取号成功]
            self.Batch_number_retrieval = data["多店铺批量取号的请求数据"]


Bf_request_data = Business_flow_request_data()
if __name__ == '__main__':
    print(Bf_request_data.test_Multi_store_order_modification_address_data[0][0])
    print(Bf_request_data.test_Multi_store_order_modification_address_data[0][1])
    print(Bf_request_data.test_Multi_store_order_modification_address_data[0][2])
    print(Bf_request_data.test_Multi_store_order_modification_address_data[0][3])
    print(Bf_request_data.Batch_number_retrieval[0][0])
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
    print(Bf_request_data.Batch_number_retrieval[0][1])
    for i in Bf_request_data.Batch_number_retrieval[0][2]:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(i)
        print("***************************************************************************************")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
    print(Bf_request_data.Batch_number_retrieval[0][2])
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
    print(Bf_request_data.Batch_number_retrieval[0][3])
    # print(Bf_request_data.test_Multi_store_order_modification_address_data)
