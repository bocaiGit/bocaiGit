import yaml


class Request_Data_Tool:
    def __init__(self):
        """
        此方法是用来读取yaml文件中的请求参数
        """
        with open(r"G:/order_huijiedan/data/request_data.yaml", encoding="utf-8") as fs:
            data = yaml.safe_load(fs)
            # 对账分类修改数据
            self.classified_data = data["对账分类修改数据"]
            # 商品简称列表的请求参数
            self.test_rpc_product_lists_api_1_data = data["商品简称列表数据"]
            # 商品简称修改单个商品的Sku简称
            self.test_rpc_sku_updateSku_api_data = data["商品简称修改单个商品的Sku简称"]
            # 上传前端已处理好的数据
            self.test_rpc_import_order_importOrderFile_api_data = data["导入查看_前端已处理好的数据"]
            # 导入查看数据&&导入查看组合查询
            self.test_rpc_import_order_list_api_data = data["导入查看列表数据详情_组合查询"]
            # 导入查看==>删除已导入数据
            self.test_rpc_import_order_deleteImportOrder_api_data = data["删除已导入数据"]
            # 底单查询==>详细记录--->获取数据接口
            self.test_rpc_order_sub_originalQuery_api_data = data["底单查询详细记录数据"]
            # 底单查询==>汇总报表-->获取数据接口
            self.test_rpc_order_sub_originalSummaryQuery_api_data = data["底单查询汇总报表数据"]
            # 扫描发货==>扫描运单号获取数据接口的请求数据
            self.test_rpc_order_sub_scan_api_data = data["扫描发货请求数据"]
            # 支付宝-删除==>请求数据
            self.test_rpc_task_delete_api_data = data["支付宝删除请求数据"]
            # 财务管理-账单中心==>重新分析__请求数据
            self.test_rpc_task_bill_api_data = data["账单中心_重新分析_请求数据"]
            #账单中心==>组合查询&&列表默认请求数据
            self.test_rpc_bill_lists_api_data = data["账单中心_搜索默认_请求数据"]
            # 订单列表8请求八次的参数
            self.test_order_sub_lists_url_data= data["订单列表请求参数_8"]
            #退款订单列表请求八次的参数
            self.test_rpc_refund_lists_api_data = data["退款订单列表请求参数_8"]
            #切换店铺请求数据
            self.test_rpc_Shop_switch_setSwitchShop_api_data = data["切换店铺请求数据"]
            #修改主店铺的店铺简称的请求数据
            self.test_rpc_Shop_setNick_api_data = data["修改主店铺的店铺简称"]
            #修改子店铺的店铺简称接口的请求数据
            self.test_rpc_Shop_switch_editShopNick_api_data = data["修改子店铺的店铺简称"]
            #解除子店铺的绑定/关联接口的请求数据
            self.test_rpc_Shop_switch_deleteShopSwitch_api_data = data["解除子店铺的绑定_关联"]
            #绑定子店铺请求数据
            self.test_rpc_Shop_switch_addShopSwitch_api_data = data["绑定子店铺_请求数据"]


requ_data = Request_Data_Tool()

if __name__ == '__main__':
    print(requ_data.classified_data)
