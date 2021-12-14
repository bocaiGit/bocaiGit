import yaml


class Response_Data_Tool:
    def __init__(self):
        with open(r"G:/order_huijiedan/yaml_data/Response.yaml", encoding="utf-8") as fs:
            dic = yaml.safe_load(fs)
            # 测试搜索商品的预期响应结果
            self.Product_Search_Response = dic["Product_Response"]
            # 测试单个商品获取sku列表详情数据==>预期响应结果
            self.rpc_sku_lists_api_response = dic["rpc_sku_lists_api_response"]
            # 单个商品sku绑定组合的详情列表==>预期数据
            self.rpc_product_combo_list_api_response = dic['rpc_product_combo_list_api_response']
            # 通过订单号提取商品接口==>预期数据
            self.Withdraw_goods_response = dic["Withdraw_goods_response"]
            # 商品简称列表的接口==>预期数据
            self.taobao_user_nick = dic["taobao_user_nick"]
            # 修改单个商品的Sku简称接口==>预期数据
            self.test_rpc_sku_updateSku_api_data = dic["修改单个商品的Sku简称_预期数据"]
            # 导入查看接口==>成功==>预期数据
            self.test_rpc_import_order_importOrderFile_api_data = dic["导入查看成功的_预期数据"]
            # 导入查看==>删除已导入数据==>预期数据
            self.test_rpc_import_order_deleteImportOrder_api_data = dic["导入查看_删除已导入数据"]
            # 底单查询==>详细记录--->获取数据接口==>预期数据
            self.test_rpc_order_sub_originalQuery_api_data = dic["底单查询详细数据_预期数据"]
            # 底单查询==>汇总报表-->获取数据接口==>预期数据
            self.test_rpc_order_sub_originalSummaryQuery_api_data = dic["底单查询汇总报表_预期数据"]
            # 扫描发货==>扫描运单号-->获取数据==>预期数据
            self.test_rpc_order_sub_scan_api_data = dic["扫描发货_预期数据"]
            #漏单检测==>预期数据
            self.test_rpc_Order_Sub_leakageOrderCheck_api_data = dic["漏单检测_预期数据"]
            #账单中心==>重新分析==>msg字段
            self.test_rpc_task_bill_api_data = dic["账单中心重新分析_预期数据_msg"]
            #账单中心==>默认请求接口 end 组合查询 的预期结果
            self.test_rpc_bill_lists_api_data = dic["账单中心_组合查询_默认请求_预期数据"]
            # 切换店铺预期数据
            self.test_rpc_Shop_switch_setSwitchShop_api_data=dic["切换店铺预期响应数据"]
            #关联店铺界面的接口预期响应数据
            self.test_rpc_Shop_getSwitchCode_api_data = dic["关联店铺预期响应数据"]
            #更新店铺代码的接口预期响应数据
            self.test_rpc_Shop_createSwitchCode_api_data = dic["更新店铺代码响应数据"]
            #修改主店铺的店铺简称的接口返回的预期响应数据
            self.test_rpc_Shop_setNick_api_data=dic["修改主店铺的店铺简称_预期响应数据"]
            #修改子店铺的店铺简称的接口返回的预期响应数据
            self.test_rpc_Shop_switch_editShopNick_api_data = dic["修改子店铺的店铺简称_预期响应数据"]
            # 解除子店铺绑定/关联的接口预期响应数据
            self.test_rpc_Shop_switch_deleteShopSwitch_api_data = dic["解除子店铺_预期响应数据"]
            #绑定店铺的接口预期数据
            self.test_rpc_Shop_switch_addShopSwitch_api_data = dic["绑定店铺响应数据"]




response_data = Response_Data_Tool()
# print(response_data.test_rpc_Shop_switch_setSwitchShop_api_data)
print(response_data.test_rpc_Shop_getSwitchCode_api_data)
