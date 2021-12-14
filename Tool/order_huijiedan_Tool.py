import yaml


class Order_Tool():
    def __init__(self):
        with open(r"G:\order_huijiedan\data\order_huijiedan.yaml", encoding="utf-8") as U:
            dic = yaml.safe_load(U)
            # 商家助手的token
            self.token = dic["hjdtoken"]
            # 商家助手的Host
            self.Host = dic["host"]  # 所有请求通用
            # 打单列表的接口请求地址
            self.order_sub_lists_url = dic['order_sub_lists_url']
            # 打单列表的请求参数（参数放在yaml文件）读取出来
            self.layId = dic['layId']
            self.limit = dic['limit']  # 打单列表&&待付款&&今日待发货&&账单中心
            self.list_type = dic['list_type']
            self.order_number_type = dic['order_number_type']
            self.page = dic['page']  # 打单列表&&待付款&&今日待发货&&账单中心
            self.time_type = dic['time_type']  # 打单列表&&待付款&&今日待发货
            self.type = dic['page']  # 打单列表&&待付款&&今日待发货
            '''待付款列表URL'''
            self.order_sub_lists_payment_url = dic['order_sub_lists_payment_url']
            # 待付款列表单独参数
            self.is_lock = dic["is_lock"]
            self.time = dic['time']
            self.seller_flag = dic['seller_flag']
            self.trade_id = dic['trade_id']
            # 今日待发货订单的URL&&今日退款订单的URL
            self.order_sub_lists_To_be_shipped_url = dic['order_sub_lists_To_be_shipped_url']
            self.order_sub_lists_refund_url = dic['order_sub_lists_refund_url']
            # 控制台点击配置中心的请求参数与URL
            self.configure_getConfigInitData = dic['configure_getConfigInitData']
            self.group = dic['group']
            self.group1 = dic['group1']
            # 控制台点击账单中心的请求参数以及URL
            self.dataString = dic['dataString']
            self.bill_lists_url = dic['bill_lists_url']
            # 控制台点击实名认证的请求参数以及URL
            self.Real_name_list = dic['real_name_list']
            self.customs_status = dic['customs_status']
            self.is_free = dic['is_free']
            # 商品简称url
            self.rpc_product_lists = dic['rpc_product_lists_url']
            # 短信充值接口
            self.rpc_supply_product_url = dic['rpc_supply_product_url']
            self.rpc_Recharge_vNo_url = dic['rpc_Recharge_vNo_url']
            # 物流配置接口
            self.rpc_logistics_getLogisticsLists_url = dic['rpc_logistics_getLogisticsLists_url']
            # 物流策略接口
            self.rpc_logistics_getMatchRuleLists_url = dic['rpc_logistics_getMatchRuleLists_url']
            # 新增物流配置接口
            self.rpc_logistics_createUpdateLogistics_url = dic['rpc_logistics_createUpdateLogistics_url']
            # 物流配置-批量删除接口
            self.rpc_logistics_deleteLogistics_url = dic['rpc_logistics_deleteLogistics_url']
            # 新增物流策略接口
            self.rpc_logistics_setMatchRule_url = dic['rpc_logistics_setMatchRule_url']
            # 批量删除物流策略接口
            self.rpc_logistics_deleteMatchRule_url = dic['rpc_logistics_deleteMatchRule_url']
            # 模板中心编辑接口
            self.rpc_Template_info_url = dic['rpc_Template_info_url']
            # 模板中心新建模板接口
            # 第一个接口
            self.rpc_Template_CommonList_url = dic['rpc_Template_CommonList_url']
            # 第二个接口
            self.rpc_Template_CommonInfo_url = dic['rpc_Template_CommonInfo_url']
            # 第三个接口
            self.rpc_Template_create_url = dic['rpc_Template_create_url']
            # 模板中心发货单接口
            # 编辑接口
            self.Shipment_edit_url_1 = dic['rpc_Template_info_url']
            self.Shipment_edit_url_2 = dic['rpc_Template_CommonInfo_url']
            # 预览接口
            self.rpc_Template_preview_url = dic['rpc_Template_preview_url']
            # 保存接口
            self.rpc_Template_edit_url = dic["rpc_Template_edit_url"]
            # 地址配置接口
            # 设为默认接口
            self.rpc_order_sender_setDefault_url = dic['rpc_order_sender_setDefault_url']
            # 智能识别地址接口&地址配置
            self.rpc_order_addressAnalysis_url = dic["rpc_order_addressAnalysis_url"]
            # 智能识别到的地址进行保存
            self.rpc_order_sender_saveSender_url = dic["rpc_order_sender_saveSender_url"]
            # 批量删除接口
            self.rpc_order_sender_delSender_url = dic["rpc_order_sender_delSender_url"]
            # 基础配置接口
            # 订单审核开启按钮
            self.rpc_configure_setConfig_url = dic["rpc_configure_setConfig_url"]
            # 这些都是我把路径以及某些接口请求参数很多都会放在yaml去读取
            # 充值记录接口
            self.rpc_Recharge_rechargeLog_url = dic["rpc_Recharge_rechargeLog_url"]
            # 消息中心接口
            self.rpc_notice_lists_url = dic["rpc_notice_lists_url"]
            # 消息中心查看消息接口
            self.rpc_notice_info_url = dic["rpc_notice_info_url"]
            # 打单列表功能接口
            self.rpc_order_sub_lists_url = dic["rpc_order_sub_lists_url"]
            # 单个订单的日志接口
            self.rpc_order_orderDetailLog_url = dic["rpc_order_orderDetailLog_url"]
            # 单个订单的详情接口
            self.rpc_order_orderDetail_url = dic["rpc_order_orderDetail_url"]
            # 单个订单的备注接口
            self.rpc_order_sub_memoUpdate_url = dic["rpc_order_sub_memoUpdate_url"]
            # 单个订单的解密接口
            self.rpc_order_decryptLists_url = dic["rpc_order_decryptLists_url"]
            # 单个订单中修改商品的商品简称接口
            self.rpc_product_updateProduct_url = dic["rpc_product_updateProduct_url"]
            # 待合并订单接口
            self.rpc_order_sub_listsWaitMerge_url = dic["rpc_order_sub_listsWaitMerge_url"]
            # 合并订单检测接口&&合并订单接口
            self.rpc_trade_merge_url = dic["rpc_trade_merge_url"]
            # 取消合并订单接口
            self.rpc_trade_cancel_url = dic["rpc_trade_cancel_url"]
            # 单个订单发货
            # 获取此账号所有的发货渠道接口
            self.rpc_logistics_getLogistics_url = dic["rpc_logistics_getLogistics_url"]
            # 获取所有快递公司的信息
            self.rpc_logistics_getLogisticsConfigure_url = dic["rpc_logistics_getLogisticsConfigure_url"]
            # 单个订单取号接口
            self.rpc_order_sub_orderSend_url = dic["rpc_order_sub_orderSend_url"]
            # 作废运单号接口
            self.rpc_order_sub_cancelInvoice_url = dic["rpc_order_sub_cancelInvoice_url"]
            # 补单接口
            self.rpc_trade_supply_url = dic["rpc_trade_supply_url"]
            # 批量取号验证接口
            self.rpc_order_sub_getInvoiceJudge_url = dic["rpc_order_sub_getInvoiceJudge_url"]
            # 批量取号发货接口
            self.rpc_order_sub_getInvoice_url = dic["rpc_order_sub_getInvoice_url"]
            # 设置默认打印机接口
            self.rpc_Prints_setPrinter_url = dic["rpc_Prints_setPrinter_url"]
            # 设置默认发货单模板————获取数据的两个接口
            self.rpc_configure_getConfigInitData_url = dic["rpc_configure_getConfigInitData_url"]
            self.rpc_Template_list_url = dic["rpc_Template_list_url"]
            # 修改发货单模板接口
            self.rpc_configure_setConfig_url = dic["rpc_configure_setConfig_url"]
            # 自由订单新增地址接口
            self.rpc_free_address_addAddress_url = dic["rpc_free_address_addAddress_url"]
            # 自由订单：新增自由订单接口
            self.rpc_free_order_saveOrder_url = dic["rpc_free_order_saveOrder_url"]
            # 自由订单列表获取订单接口
            # self.rpc_order_sub_lists_url= dic["rpc_order_sub_lists_url"]
            # 获取订单的物流信息接口
            self.rpc_order_sub_getLogistics_url = dic["rpc_order_sub_getLogistics_url"]
            # 自由订单下单时选择淘宝商品接口
            self.rpc_product_combo_getSkuList_url = dic["rpc_product_combo_getSkuList_url"]
            # 自由订单取号前的验证接口
            self.rpc_order_sub_getInvoiceJudge = dic["rpc_order_sub_getInvoiceJudge"]
            # 商品列表接口
            self.rpc_product_lists_url = dic['rpc_product_lists_url']
            # 单个商品的sku列表
            self.rpc_sku_lists_url = dic["rpc_sku_lists_url"]
            # 单个商品sku绑定组合的详情列表接口
            self.rpc_product_combo_list_url = dic["rpc_product_combo_list_url"]
            # 商品绑定套盒接口
            self.rpc_sku_matchCombo_url = dic["rpc_sku_matchCombo_url"]
            # 解除商品已经绑定的套盒接口
            self.rpc_sku_cancelMatchCombo_url = dic["rpc_sku_cancelMatchCombo_url"]
            # 设置商品的对账主体接口
            self.rpc_product_setcate_url = dic["rpc_product_setcate_url"]
            # 商品列表中更新缓存接口
            self.rpc_product_updateCache_url = dic["rpc_product_updateCache_url"]
            # 商品列表同步商品接口
            self.rpc_task_LoadProduct_url = dic["rpc_task_LoadProduct_url"]
            # 新增商品接口
            self.rpc_Product_addShopProduct_url = dic["rpc_Product_addShopProduct_url"]
            # 提取商品接口
            self.rpc_Product_extractShopProduct_url = dic["rpc_Product_extractShopProduct_url"]
            # 保存提取到的商品接口
            self.rpc_Product_addExtractShopProduct_url = dic["rpc_Product_addExtractShopProduct_url"]
            # 对账主体中的对账分类是否启用
            self.rpc_Category_status_url = dic["rpc_Category_status_url"]
            # 对账分类是否锁定
            self.rpc_Category_lock_url = dic["rpc_Category_lock_url"]
            # 修改对账主体中的对账分类的数据接口
            self.rpc_Category_createUpdateCategory_url = dic["rpc_Category_createUpdateCategory_url"]
            # 修改单个商品的sku简称接口
            self.rpc_sku_updateSku_url = dic["rpc_sku_updateSku_url"]
            # 核对商品列表接口
            self.rpc_stock_lists_url = dic["rpc_stock_lists_url"]
            # 导入查看上传文件接口&&&这里是前端处理好的数据发送给后端,所以只能通过接口传入处理好的数据流
            self.rpc_import_order_importOrderFile_url = dic["rpc_import_order_importOrderFile_url"]
            # 导入查看搜索数据&&导入查看获取数据接口
            self.rpc_import_order_lists_url = dic["rpc_import_order_lists_url"]
            # 导入查看==>删除已导入数据
            self.rpc_import_order_deleteImportOrder_url = dic["rpc_import_order_deleteImportOrder_url"]
            # 底单查询==>详细记录--->获取数据接口
            self.rpc_order_sub_originalQuery_url = dic["rpc_order_sub_originalQuery_url"]
            # 底单查询==>汇总报表-->获取数据接口
            self.rpc_order_sub_originalSummaryQuery_url = dic["rpc_order_sub_originalSummaryQuery_url"]
            # 扫描发货==>扫描过后获取数据的接口
            self.rpc_order_sub_scan_url = dic["rpc_order_sub_scan_url"]
            # 漏单检测接口
            self.rpc_Order_Sub_leakageOrderCheck_url = dic["rpc_Order_Sub_leakageOrderCheck_url"]
            # 支付宝删除接口
            self.rpc_task_delete_url = dic['rpc_task_delete_url']
            # 账单中心-重新分析
            self.rpc_task_bill_url = dic["rpc_task_bill_url"]
            # 财务管理==.账单中心==>获取数据&&搜索url
            self.rpc_bill_lists_url = dic["rpc_bill_lists_url"]
            # 订单管理==>退款订单
            self.rpc_refund_lists_url = dic["rpc_refund_lists_url"]
            # 多店铺操作--->切换店铺
            self.rpc_Shop_switch_setSwitchShop_url = dic["rpc_Shop_switch_setSwitchShop_url"]
            # 多店铺操作--->获取绑定店铺界面的数据
            self.rpc_Shop_getSwitchCode_url = dic["rpc_Shop_getSwitchCode_url"]
            # 多店铺操作---->更新主店铺的店铺代码
            self.rpc_Shop_createSwitchCode_url = dic["rpc_Shop_createSwitchCode_url"]
            # 修改主店铺的店铺简称接口
            self.rpc_Shop_setNick_url = dic["rpc_Shop_setNick_url"]
            # 修改子店铺的店铺简称接口
            self.rpc_Shop_switch_editShopNick_url = dic["rpc_Shop_switch_editShopNick_url"]
            # 解除子店铺的关联/绑定
            self.rpc_Shop_switch_deleteShopSwitch_url = dic["rpc_Shop_switch_deleteShopSwitch_url"]
            # 关联店铺/绑定店铺
            self.rpc_Shop_switch_addShopSwitch_url = dic["rpc_Shop_switch_addShopSwitch_url"]
            # 修改收件地址接口
            self.rpc_order_sub_updateOrderAddress_url = dic["rpc_order_sub_updateOrderAddress_url"]


Tools = Order_Tool()
# print(type(Tools.rpc_order_sub_cancelInvoice_url))
# print(Tools.rpc_order_sub_cancelInvoice_url)
