import logging
import time
import json

import requests
from Tool.order_huijiedan_Tool import Order_Tool, Tools
from Log.my_log import logger
from api.Custom_Encapsulation__Request import request_tools


# from api.Encapsulation_request import Requests_example


class Test_print_list():
    # 获取打单列表的内容
    def order_sub_lists(self, layId, limit, ):
        Host = Order_Tool().Host
        url = Order_Tool().order_sub_lists_url
        self.layId = layId
        self.limit = limit
        self.url = Host + url
        self.data = {'hjdtoken': Order_Tool().token, 'layId': self.layId, 'limit': self.limit,
                     'list_type': Order_Tool().list_type, 'order_number_type': Order_Tool().order_number_type,
                     'page': Order_Tool().page, 'time_type': Order_Tool().time_type, 'type': Order_Tool().type
                     }
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep


class Home_console():
    def order_sub_lists_payment_url(self):
        # 获取点击控制台的待付款订单后接口返回的数据
        Host = Order_Tool().Host
        url = Order_Tool().order_sub_lists_payment_url
        self.url = Host + url
        self.data = {'hjdtoken': Order_Tool().token, "layId": "1002", 'is_lock': Order_Tool().is_lock,
                     'time': Order_Tool().time,
                     'seller_flag': Order_Tool().seller_flag, 'trade_id': Order_Tool().trade_id,
                     'limit': Order_Tool().limit, 'page': Order_Tool().page, 'time_type': Order_Tool().time_type,
                     'type': Order_Tool().type
                     }
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def order_sub_lists_To_be_shipped_url(self):
        # 获取点击控制台的今日待发货订单后接口返回的数据
        Host = Order_Tool().Host
        url = Order_Tool().order_sub_lists_To_be_shipped_url
        self.url = Host + url
        self.data = {'hjdtoken': Order_Tool().token, "layId": "1003", 'is_lock': Order_Tool().is_lock,
                     'time': Order_Tool().time,
                     'seller_flag': Order_Tool().seller_flag, 'trade_id': Order_Tool().trade_id,
                     'limit': Order_Tool().limit, 'page': Order_Tool().page, 'time_type': Order_Tool().time_type,
                     'type': Order_Tool().type
                     }
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def order_sub_lists_refund_url(self):
        # 获取点击控制台的今日退款订单后接口返回的数据
        Host = Order_Tool().Host
        url = Order_Tool().order_sub_lists_refund_url
        self.url = Host + url
        self.data = {'hjdtoken': Order_Tool().token, "layId": "1005", 'is_lock': Order_Tool().is_lock,
                     'time': Order_Tool().time,
                     'seller_flag': Order_Tool().seller_flag, 'trade_id': Order_Tool().trade_id,
                     'limit': Order_Tool().limit, 'page': Order_Tool().page, 'time_type': Order_Tool().time_type,
                     'type': Order_Tool().type
                     }
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    # 控制台点击配置中心，一共会触发2次请求
    def configure_getConfigInitData(self):
        # 第一次请求
        Host = Order_Tool().Host
        url = Order_Tool().configure_getConfigInitData
        self.url = Host + url
        self.data = {'hjdtoken': Order_Tool().token, "group": Order_Tool().group}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def configure_getConfigInitData1(self):
        # 第二次请求
        Host = Order_Tool().Host
        url = Order_Tool().configure_getConfigInitData
        self.url = Host + url
        self.data1 = {'hjdtoken': Order_Tool().token, "group": Order_Tool().group1}
        rep1 = requests.post(url=self.url, data=self.data1)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep1

    def bill_lists(self):
        # 控制台点击账单中心的接口返回数据
        Host = Order_Tool().Host
        url = Order_Tool().bill_lists_url
        self.url = Host + url
        self.data = {'hjdtoken': Order_Tool().token, 'dataString': Order_Tool().dataString, 'limit': Order_Tool().limit,
                     'page': Order_Tool().page}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def order_sub_list_Real_name(self):
        # 控制台点击实名认证的接口返回数据
        Host = Order_Tool().Host
        url = Order_Tool().Real_name_list
        self.url = Host + url
        self.data = {'hjdtoken': Order_Tool().token, "layId": 1003, "customs_status": Order_Tool().customs_status,
                     "is_free": Order_Tool().is_free, "limit": Order_Tool().limit,
                     "order_number_type": Order_Tool().order_number_type,
                     "page": Order_Tool().page, "time_type": Order_Tool().time_type
                     }
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    # 商品简称接口
    def rpc_product_lists(self, dataString, limit, page):
        Host = Order_Tool().Host
        url = Order_Tool().rpc_product_lists
        self.url = Host + url
        self.dataString = dataString
        self.limit = limit
        self.page = page
        self.data = {"hjdtoken": Order_Tool().token, "dataString": self.dataString, "limt": self.limit,
                     "page": self.page}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()["Params"]["hjdtoken"]))
        return rep

    # 短信充值接口
    def rpc_supply_product(self, DATASTRING):
        # 短信充值触发的第一个接口
        Host = Order_Tool().Host
        URL = Order_Tool().rpc_supply_product_url
        self.URL = Host + URL
        self.DATASTRING = DATASTRING
        self.DATA = {'hjdtoken': Order_Tool().token, 'dataString': self.DATASTRING}
        REP = requests.post(url=self.URL, data=self.DATA)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.URL, REP.json()))
        return REP

    def rpc_Recharge_vNo_url(self, dataString):
        Host = Order_Tool().Host
        # 短信充值触发的第二个接口
        url = Order_Tool().rpc_Recharge_vNo_url
        self.url = Host + url
        self.dataString = dataString
        self.data = {"hjdtoken": Order_Tool().token, "dataString": self.dataString}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep


class ManagementCenter():
    Host = Order_Tool().Host
    token = Order_Tool().token
    headers = {"hjdtoken": token}

    def rpc_logistics_getLogisticsLists(self, limit, page):
        # 物流配置接口
        url = Order_Tool().rpc_logistics_getLogisticsLists_url
        self.url = self.Host + url
        self.limit = limit
        self.page = page
        self.data = {"hjdtoken": Order_Tool().token, "limit": self.limit, "page": self.page}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def rpc_logistics_getMatchRuleLists(self, limit, page):
        # 物流策略接口
        url = Order_Tool().rpc_logistics_getMatchRuleLists_url
        self.url = self.Host + url
        self.limit = limit
        self.page = page
        self.data = {"hjdtoken": Order_Tool().token, "limit": self.limit, "page": self.page}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    # 新增物流配置
    def rpc_logistics_createUpdateLogistics(self, alias, api_type_id, assign_type, express_id, name, phone,
                                            shipp_address, template):
        url = Order_Tool().rpc_logistics_createUpdateLogistics_url
        self.url = self.Host + url
        self.alias = alias
        self.api_type_id = api_type_id
        self.assign_type = assign_type
        self.express_id = express_id
        self.name = name
        self.phone = phone
        self.shipp_address = shipp_address
        self.template = template
        self.data = {"hjdtoken": Order_Tool().token, "alias": self.alias, 'api_type_id': self.api_type_id,
                     'express_id': self.express_id, 'assign_type': self.assign_type,
                     "name": self.name, "phone": self.phone, 'shipp_address': self.shipp_address,
                     "template": self.template
                     }
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def logistics_deleteLogistics(self, ids):
        url = Order_Tool().rpc_logistics_deleteLogistics_url
        self.ids = ids
        self.url = self.Host + url
        self.data = {"hjdtoken": self.token, "ids": [self.ids]}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_logistics_createUpdateLogistics1(self, id, taobao_user_id, express_id, alias, assign_type, name, status,
                                             phone, api_type_id, template,
                                             customer_id, customer_code, service_code, shipp_address, is_vip,
                                             created, express, address, api):
        url = Order_Tool().rpc_logistics_createUpdateLogistics_url
        self.url = self.Host + url
        self.id = id
        self.api = api
        self.address = address
        self.created = created
        self.express = express
        self.is_vip = is_vip
        self.service_code = service_code
        self.customer_id = customer_id
        self.customer_code = customer_code
        self.taobao_user_id = taobao_user_id
        self.alias = alias
        self.status = status
        self.api_type_id = api_type_id
        self.assign_type = assign_type
        self.express_id = express_id
        self.name = name
        self.phone = phone
        self.shipp_address = shipp_address
        self.template = template
        self.data = {"hjdtoken": self.token, "id": self.id, 'taobao_user_id': self.taobao_user_id,
                     'express_id': self.express_id,
                     "alias": self.alias, 'assign_type': self.assign_type, "name": self.name, "status": self.status,
                     "phone": self.phone,
                     'api_type_id': self.api_type_id, "template": self.template, "customer_id": self.customer_id,
                     'customer_code': self.customer_code, "service_code": self.service_code,
                     'shipp_address': self.shipp_address,
                     "is_vip": self.is_vip, 'created': self.created, "express": self.express, 'address': self.address,
                     'api': self.api,
                     }
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_logistics_setMatchRule(self, id, condition_type, rule_type, area_value, area_name, condition_type1,
                                   area_value1, area_name1,
                                   rule_name, remarks, type, status, do_code, express_id, priority):
        # 新增物流策略接口

        url = Order_Tool().rpc_logistics_setMatchRule_url
        self.url = self.Host + url
        self.id = id
        self.condition_type = condition_type
        self.rule_type = rule_type
        self.area_value = area_value
        self.area_name = area_name
        self.condition_type1 = condition_type1
        self.area_value1 = area_value1
        self.area_name1 = area_name1
        self.rule_name = rule_name
        self.remarks = remarks
        self.type = type
        self.status = status
        self.do_code = do_code
        self.express_id = express_id
        self.priority = priority
        self.data = {
            "id": self.id,
            "condition_data": [
                {
                    "condition_type": self.condition_type,
                    "rule_type": self.rule_type,
                    "area_value": [self.area_value],
                    "area_name": [self.area_name]},
                {
                    "condition_type": self.condition_type1,
                    "rule_type": self.rule_type,
                    "area_value": [self.area_value1],
                    "area_name": [self.area_name1]}
            ],
            "rule_name": self.rule_name,
            "remarks": self.remarks,
            "type": self.type,
            "status": self.status,
            "do_type": self.do_code,
            "express_id": self.express_id,
            "priority": self.priority
        }
        rep = requests.post(url=self.url, json=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_logistics_deleteMatchRule(self, ids):
        # 批量删除物流策略接口
        url = Order_Tool().rpc_logistics_deleteMatchRule_url
        self.url = self.Host + url
        self.ids = ids
        self.data = {'hjdtoken': self.token, "ids": [self.ids]}
        rep = requests.post(url=self.url, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_Template_info(self, seller_template_id):
        # 模板中心编辑接口
        url = Order_Tool().rpc_Template_info_url
        self.url = self.Host + url
        self.seller_template_id = seller_template_id

        self.data = {'seller_template_id': self.seller_template_id}
        rep = requests.post(url=self.url, data=self.data, headers=self.headers)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_Template_CommonList(self, category_id):
        # 新建快递单模板第一个接口
        url = Order_Tool().rpc_Template_CommonList_url
        self.url = self.Host + url
        self.category_id = category_id
        self.data = {"category_id": self.category_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_Template_CommonInfo(self, common_template_id):
        # 新建快递单模板第二个接口
        url = Order_Tool().rpc_Template_CommonInfo_url
        self.url = self.Host + url
        self.common_template_id = common_template_id
        self.data = {"common_template_id": self.common_template_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_Template_create(self, category_id, template_name, express_code, width, height, template_id, needTopLogo,
                            horizontalOffset, verticalOffset):
        self.category_id = category_id
        self.template_name = template_name
        self.express_code = express_code
        self.width = width
        self.height = height
        self.template_id = template_id
        self.needTopLogo = needTopLogo
        self.horizontalOffset = horizontalOffset
        self.verticalOffset = verticalOffset
        url = Order_Tool().rpc_Template_create_url
        self.url = self.Host + url
        self.data = {"category_id": self.category_id, "template_name": self.template_name,
                     "express_code": self.express_code,
                     "width": self.width, "height": self.height, "template_id": self.template_id,
                     "template_data": {"customsData": [],
                                       "textData": []},
                     "printer_config": {'needTopLogo': self.needTopLogo, "horizontalOffset": self.horizontalOffset,
                                        'verticalOffset': self.verticalOffset}
                     }
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    # 发货单编辑接口第一个
    def Shipment_edit_1(self, seller_template_id):
        url = Order_Tool().Shipment_edit_url_1
        self.seller_template_id = seller_template_id
        self.url = self.Host + url
        self.data = {"seller_template_id": self.seller_template_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    # 发货单编辑接口第二个
    def Shipment_edit_2(self, common_template_id):
        url = Order_Tool().Shipment_edit_url_2
        self.url = self.Host + url
        self.common_template_id = common_template_id
        self.data = {"common_template_id": self.common_template_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_Template_preview(self, print_express, print_invoice, seller_template_id):
        url = Order_Tool().rpc_Template_preview_url
        self.url = self.Host + url
        self.print_express = print_express
        self.print_invoice = print_invoice
        self.seller_template_id = seller_template_id
        self.data = {"print_express": self.print_express, "print_invoice": self.print_invoice,
                     "seller_template_id": self.seller_template_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_Template_edit_url(self):
        # 保存发货单接口
        url = self.Host + Order_Tool().rpc_Template_edit_url
        self.data = {"category_id": "88", "template_name": "测试2", "express_code": "", "width": "297", "height": "210",
                     "template_id": "201", "template_data": {
                "page": {"width": "297", "height": "210", "heightTop": 46.566666666667, "heightBottom": 35.71875,
                         "repeatTop": "false", "repeatBottom": 'false'}, "customsData": [
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 68.79166666666667, "height": 8.466666666666667, "top": 25.929166666666664,
                     "left": 20.520833333333332, "position": "top", "id": "201"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 72.49583333333332, "height": 8.466666666666667, "top": 25.929166666666664,
                     "left": 221.60416666666666, "position": "top", "id": "203"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 72.76041666666667, "height": 8.466666666666667, "top": 25.929166666666664,
                     "left": 118.41666666666667, "position": "top", "id": "206"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 68.79166666666667, "height": 7.9375, "top": 18.520833333333332,
                     "left": 20.520833333333332, "position": "top", "id": "301"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "code128",
                     "src": None, "width": 59.53125, "height": 13.229166666666666, "top": 2.6458333333333335, "left": 2,
                     "position": "top", "id": "302"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 72.76041666666667, "height": 7.9375, "top": 18.520833333333332,
                     "left": 118.41666666666667, "position": "top", "id": "303"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 273.57916666666665, "height": 7.9375, "top": 34.395833333333336,
                     "left": 20.520833333333332, "position": "top", "id": "304"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 72.49583333333332, "height": 7.9375, "top": 18.520833333333332,
                     "left": 221.60416666666666, "position": "top", "id": "313"},
                    {"style": "fontSize:12;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "qrcode",
                     "width": 26.458333333333332, "height": 26.458333333333332, "top": 5.291666666666667,
                     "left": 268.43541666666664, "position": "bottom", "id": "106"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 144.19791666666666, "height": 7.9375, "top": 7.9375,
                     "left": 20.520833333333332, "position": "bottom", "id": "315"}], "textData": [
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 18.520833333333332, "left": 2,
                     "position": "top", "id": "DTBXggyq", "value": "订单编号："},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 18.520833333333332,
                     "left": 99.89583333333333, "position": "top", "id": "gbn3Nm2e", "value": "下单时间："},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 18.520833333333332,
                     "left": 203.08333333333334, "position": "top", "id": "BdF4aWM9", "value": "付款时间："},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 26.458333333333332,
                     "left": 2.2645833333333334, "position": "top", "id": "XX4Ed1fn", "value": "收件姓名："},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 26.458333333333332,
                     "left": 99.89583333333333, "position": "top", "id": "PIoMXK1z", "value": "买家昵称："},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 26.458333333333332,
                     "left": 203.08333333333334, "position": "top", "id": "GGBeFvR0", "value": "收件电话："},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 34.395833333333336, "left": 2,
                     "position": "top", "id": "ivVCrudK", "value": "卖家备注："},
                    {"style": "fontSize:14;fontWeight:bold;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 26.458333333333332, "height": 7.9375, "top": 2.6458333333333335,
                     "left": 139.58333333333334, "position": "top", "id": "G0qC6WVX", "value": "发货单"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 162.71875, "height": 7.9375, "top": 15.875, "left": 2, "position": "bottom",
                     "id": "hLiyCToe", "value": "感谢您在本店购物，收到宝贝后满意请麻烦给5分好评，您的评价是我们努力的动力！"},
                    {"style": "fontSize:10;fontWeight:normal;fontFamily:SimHei;lineHeight:5;", "type": "text",
                     "src": None, "width": 18.520833333333332, "height": 7.9375, "top": 7.9375, "left": 2,
                     "position": "bottom", "id": "1JN58Unt", "value": "店铺名称："}],
                "tableData": {"table": {"top": 0, "left": 3, "width": 291},
                              "header": {"title": {"show": 'true', "width": 86, "isCustom": 'true'},
                                         "sku_properties_name": {"show": 'true', "width": 70, "isCustom": 'true'},
                                         "outer_sku_id": {"show": 'true', "width": 40, "isCustom": 'true'},
                                         "num": {"show": 'true', "width": 20, "isCustom": 'true'},
                                         "pic_path": {"show": 'true', "width": 20, "isCustom": 'true'},
                                         "price": {"show": 'true', "width": 25, "isCustom": 'true'},
                                         "discount_fee": {"show": 'true', "width": 20, "isCustom": 'true'}},
                              "footer": {"total_num": {"show": 'true'}, "post_fee": {"show": 'true'}}}},
                     "printer_config": {"needTopLogo": 'false', "horizontalOffset": 0, "verticalOffset": 0},
                     "seller_template_id": "11"}
        rep = requests.post(url=url, headers=self.headers, json=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_sender_setDefault(self, id):
        # 设为默认地址接口
        self.id = id
        url = Order_Tool().rpc_order_sender_setDefault_url
        self.url = self.Host + url
        self.data = {"id": self.id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_addressAnalysis(self, receiver):
        # 地址配置中智能识别地址接口
        self.receiver = receiver
        url = Order_Tool().rpc_order_addressAnalysis_url
        self.url = self.Host + url
        self.data = {"receiver": self.receiver}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_sender_saveSender_url(self, addr, city, id, contact_name, country, mobile_phone, province, zip_code):
        # 保存地址接口
        self.addr = addr
        self.city = city
        self.id = id
        self.contact_name = contact_name
        self.country = country
        self.mobile_phone = mobile_phone
        self.province = province
        self.zip_code = zip_code
        url = Order_Tool().rpc_order_sender_saveSender_url
        self.url = self.Host + url
        self.data = {"addr": self.addr, "city": self.city, "id": self.id, "contact_name": self.contact_name,
                     "country": country,
                     "mobile_phone": self.mobile_phone, "province": self.province, "zip_code": self.zip_code}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_sender_delSender_api(self, ids):
        # 批量删除接口
        url = Order_Tool().rpc_order_sender_delSender_url  # 接口的请求路径
        self.url = self.Host + url  # 地址加上路径，组合成完整的接口地址
        self.ids = ids  # 这个只是一个形参
        self.data = {"ids": self.ids}  # 接口的请求参数
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)  # 带上请求地址和请求头以及请求参数发送直接口
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    # 基础配置接口
    def rpc_configure_setConfig_api(self, basic_order_check, basic_order_send, order_send):
        url = Order_Tool().rpc_configure_setConfig_url
        self.url = self.Host + url
        self.basic_order_check = basic_order_check
        self.basic_order_send = basic_order_send
        self.order_send = order_send
        self.data = {
            "group": "2", "basic_order_check": self.basic_order_check, "basic_order_check_id": "352",
            "order_send": self.order_send, "order_check": [], "basic_order_send": self.basic_order_send,
            "basic_order_send_id": "353", "basic_is_service": "0",
            "service_id": "347", "basic_time_type": "Y-m-d H:i:s", "basic_is_time": "0", "time_id": "348",
            "basic_symbol": "0", "basic_is_symbol": "0", "symbol_id": "349", "basic_flag": "0", "basic_is_flag": "0",
            "flag_id": "350", "basic_post_flag": "0", "basic_is_post_flag": "0", "post_flag_id": "351"
        }
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    # 充值记录接口
    def rpc_Recharge_rechargeLog_api(self, page, limit):
        url = Order_Tool().rpc_Recharge_rechargeLog_url
        self.url = self.Host + url
        self.page = page
        self.limit = limit

        self.data = {"page": self.page, "limit": self.limit,
                     "dataString": "{\"order_no\":\"\",\"change_date\":\"\",\"page\":1,\"limit\":10}"}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def rpc_notice_lists_api(self):
        # 消息中心
        url = Order_Tool().rpc_notice_lists_url
        self.url = self.Host + url
        self.data = {}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        return rep

    def rpc_notice_info_api(self, dataString):
        # 消息中心查看消息的接口
        self.dataString = dataString
        url = Order_Tool().rpc_notice_info_url
        self.url = self.Host + url
        self.data = {"dataString": self.dataString}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep


class Print_Shipment():
    # 打单列表功能
    Host = Order_Tool().Host
    token = Order_Tool().token
    headers = {"hjdtoken": token}

    data = {"list_type": "printList", "time_type": "1", "type": "3", "order_number_type": "1",
            "layId": "10034", "page": 1, "limit": 20, "sort_type": "created", "sort_order": "desc"}

    def rpc_order_sub_lists_api(self, layId, list_type, time_type, type, order_number_type, page, limit, sort_type,
                                sort_order):
        # 设置勾选待发货未取号宝贝
        url = Order_Tool().rpc_order_sub_lists_url
        self.url = self.Host + url
        self.list_type = list_type
        self.time_type = time_type
        self.type = type
        self.order_number_type = order_number_type
        self.layId = layId
        self.page = page
        self.limit = limit
        self.sort_type = sort_type
        self.sort_order = sort_order
        self.data = {"layId": self.layId, "list_type": self.list_type, "time_type": self.time_type, 'type': self.type,
                     'order_number_type': self.order_number_type, 'page': self.page, 'limit': self.limit,
                     'sort_type': self.sort_type, 'sort_order': self.sort_order}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def rpc_configure_setConfig_api(self, group, sort_order, sort_type):
        # 高级设置接口
        url = Order_Tool().rpc_configure_setConfig_url
        self.url = self.Host + url
        self.group = group
        self.sort_order = sort_order
        self.sort_type = sort_type
        self.data = {"group": self.group, "sort_order": self.sort_order, "sort_type": self.sort_type}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_orderDetailLog_api(self, trade_id):
        # 单个订单的日志接口
        url = Order_Tool().rpc_order_orderDetailLog_url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.data = {"trade_id": self.trade_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_orderDetail_api(self, trade_id):
        # 单个订单的详情接口
        url = Order_Tool().rpc_order_orderDetail_url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.data = {"trade_id": self.trade_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def rpc_order_sub_memoUpdate_api(self, flag, is_free, remarks, trade_id):
        # 单个订单备注接口
        url = Order_Tool().rpc_order_sub_memoUpdate_url
        self.url = self.Host + url
        self.flag = flag
        self.is_free = is_free
        self.remarks = remarks
        self.trade_id = trade_id
        self.data = {"flag": self.flag, 'is_free': self.is_free, 'remarks': self.remarks, "trade_id": [self.trade_id]}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_decryptLists_api(self, tids):
        # 单个订单的解密接口
        url = Order_Tool().rpc_order_decryptLists_url
        self.url = self.Host + url
        self.tids = tids
        self.data = {"tids": self.tids}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_product_updateProduct_api(self, num_iid, short_name):
        # 修改单个订单中的商品简称
        url = Order_Tool().rpc_product_updateProduct_url
        self.url = self.Host + url
        self.num_iid = num_iid
        self.short_name = short_name
        self.data = {"num_iid": self.num_iid, "short_name": self.short_name}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    a = {"list_type": "printList", "time_type": "2", "time": "2021-10-11 00:00:00到2021-10-13 23:59:59", "type": "3",
         "keyword": "", "keyword2": "", "keyword3": "", "order_number_type": "2", "is_get_invoice_sub": "1",
         "is_print_express": "", "is_print_invoice": "", "is_message": "1", "is_unpack": "", "is_not_refund": "",
         "layId": "10034", "seller_flag": ["5"], "trade_id": [], "page": 1, "limit": 20, "receiver_name": "菠菜",
         "buyer_nick": "", "sort_type": "created", "sort_order": "desc", "order_number": "15003777184"}

    def rpc_order_sub_print_lists(self, buyer_nick, is_get_invoice_sub, is_message, is_not_refund, is_print_express,
                                  is_print_invoice, is_unpack,
                                  keyword,
                                  keyword2, keyword3, layId, limit, list_type,
                                  order_number, order_number_type, page, receiver_name, seller_flag, sort_order,
                                  sort_type, time,
                                  time_type, trade_id, type):
        # 打单列表查询接口
        url = Order_Tool().rpc_order_sub_lists_url
        self.url = self.Host + url
        self.list_type = list_type

        self.time_type = time_type
        self.time = time
        self.type = type
        self.keyword = keyword
        self.keyword2 = keyword2
        self.keyword3 = keyword3
        self.order_number_type = order_number_type
        self.is_get_invoice_sub = is_get_invoice_sub
        self.is_print_express = is_print_express
        self.is_print_invoice = is_print_invoice
        self.is_message = is_message
        self.is_unpack = is_unpack
        self.is_not_refund = is_not_refund
        self.layId = layId
        self.seller_flag = seller_flag
        self.trade_id = trade_id
        self.page = page
        self.limit = limit
        self.receiver_name = receiver_name
        self.buyer_nick = buyer_nick
        self.sort_type = sort_type
        self.sort_order = sort_order
        self.order_number = order_number
        self.data = {"list_type": self.list_type, "time_type": self.time_type, "time": self.time,
                     "type": self.type,
                     "keyword": self.keyword, "keyword2": self.keyword2, "keyword3": self.keyword3,
                     "order_number_type": self.order_number_type,
                     "is_get_invoice_sub": self.is_get_invoice_sub,
                     "is_print_express": self.is_print_express, "is_print_invoice": self.is_print_invoice,
                     "is_message": self.is_message, "is_unpack": self.is_unpack,
                     "is_not_refund": self.is_not_refund,
                     "layId": self.layId, "seller_flag": [self.seller_flag], "trade_id": [self.trade_id],
                     "page": self.page, "limit": self.limit,
                     "receiver_name": self.receiver_name,
                     "buyer_nick": self.buyer_nick, "sort_type": self.sort_type, "sort_order": self.sort_order,
                     "order_number": self.order_number}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def rpc_order_sub_listsWaitMerge_api(self, trade_id):
        # 待合并订单接口
        url = Order_Tool().rpc_order_sub_listsWaitMerge_url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.data = {"trade_id": self.trade_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def rpc_trade_merge_api_testing(self, trade_id):
        # 合并订单检测接口
        url = Order_Tool().rpc_trade_merge_url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.data = {"trade_id": self.trade_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_trade_merge_api_merge(self, trade_id, action, address_id):
        # 合并订单接口，这里需要调用上面一个接口返回的““mergeToken””
        url = Order_Tool().rpc_trade_merge_url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.action = action
        self.address_id = address_id
        testing = Print_Shipment()  # 实例化Print_Shipment类
        merge_testing = testing.rpc_trade_merge_api_testing("2049765076674657109,2057533301366657109").json()[
            "mergeToken"]  # 调用类方法传入参数并通过key获取value值，赋值后传入本方法的接口data
        self.data = {"trade_id": self.trade_id, "action": self.action, "address_id": self.address_id,
                     "mergeToken": merge_testing, }
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_trade_cancel_api(self, trade_id):
        # 取消合并订单接口
        url = Order_Tool().rpc_trade_cancel_url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.data = {"trade_id": self.trade_id}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_logistics_getLogistics_api(self):
        # 获取此账号所有的发货渠道接口
        url = Order_Tool().rpc_logistics_getLogistics_url
        self.url = self.Host + url
        self.data = {}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_logistics_getLogisticsConfigure_api(self, status):
        # 获取所有快递公司的信息
        url = Order_Tool().rpc_logistics_getLogisticsConfigure_url
        self.url = self.Host + url
        self.status = status
        self.data = {"status": self.status}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep))
        return rep

    def rpc_order_sub_orderSend_api_01(self, checked_express, checked_invoice, express_info_id, get_invoice_type,
                                       printer_express, printer_invoice, trade_id, type):
        # 单个订单取号接口
        url = Order_Tool().rpc_order_sub_orderSend_url
        self.url = self.Host + url
        self.checked_express = checked_express
        self.checked_invoice = checked_invoice
        self.express_info_id = express_info_id
        self.get_invoice_type = get_invoice_type
        self.printer_express = printer_express
        self.printer_invoice = printer_invoice
        self.trade_id = trade_id
        self.type = type
        oids_json = [2051226102209657109]
        self.data = {"checked_express": self.checked_express, "checked_invoice": checked_invoice, "type": self.type,
                     "express_info_id": self.express_info_id,
                     "get_invoice_type": self.get_invoice_type, "printer_express": self.printer_express,
                     "printer_invoice": self.printer_invoice, "oids": oids_json,
                     "trade_id": self.trade_id, }
        rep = requests.post(url=self.url, headers=self.headers, json=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_sub_cancelInvoice_api(self, oid):
        # 作废运单号接口
        url = Order_Tool().rpc_order_sub_cancelInvoice_url
        self.url = self.Host + url
        self.oid = oid
        self.data = {"oid": self.oid}
        rep = requests.post(url=self.url, headers=self.headers, json=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_trade_supply_api(self):
        # 补单接口
        url = Order_Tool().rpc_trade_supply_url
        self.url = self.Host + url
        self.data = {"trade_id": "2051226534208657109", "target_trade_id": "1634551509001001", "data": [
            {"name": "服务市场测试产品，不出售，勿拍", "spec": "颜色分类:白色睡裙+T裤;尺码:L", "code": "0", "price": 5, "num": "1"},
            {"name": "测试自动化", "spec": "测试自动化", "code": "1", "price": 1, "num": "1"}],
                     "address": {"receiver_address": "*堡街道近胜嫁路商品交易中心a楼***", "receiver_city": "杭州市",
                                 "receiver_district": "上城区", "receiver_mobile": "150****7184", "receiver_name": "菠*",
                                 "receiver_phone": "", "receiver_state": "浙江省", "receiver_town": "九堡街道",
                                 "receiver_zip": "0", "tid": "2051226534208657109", "trade_id": "2051226534208657109"},
                     "action": "supplyOrder", "express_info_id": "0"}
        rep = requests.post(url=self.url, headers=self.headers, json=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_sub_orderSend_api(self):
        # 发货接口
        url = Order_Tool().rpc_order_sub_orderSend_url
        self.url = self.Host + url
        self.data = {"checked_express": "false", "checked_invoice": "false", "type": 2, "express_info_id": "0",
                     "get_invoice_type": 1, "printer_express": "QR-588 LABEL (副本 3)",
                     "printer_invoice": "QR-588 LABEL (副本 3)", "oids": ["2049762952350657109"],
                     "trade_id": "2049762952350657109"}
        rep = requests.post(url=self.url, headers=self.headers, data=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_sub_getInvoiceJudge_api(self, trade_id, oids, trade_id1, oids1):
        # 批量取号验证接口
        url = Order_Tool().rpc_order_sub_getInvoiceJudge_url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.trade_id1 = trade_id1
        self.oids = oids
        self.oids1 = oids1
        self.data = {"type": 2, "do_type": "2", "get_invoice_type": 2, "express_info_id": "0",
                     "printer_express": "QR-588 LABEL (副本 3)", "printer_invoice": "QR-588 LABEL (副本 3)",
                     "checked_express": "false", "checked_invoice": "false",
                     "trade_ids": [{"trade_id": self.trade_id, "oids": [self.oids]},
                                   {"trade_id": self.trade_id1, "oids": [self.oids1]}]}
        rep = requests.post(url=self.url, headers=self.headers, json=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_order_sub_getInvoice_api(self, trade_id, oids, get_invoice_type, trade_id1, oids1):
        # 批量取号接口
        url = Order_Tool().rpc_order_sub_getInvoice_url
        self.url = self.Host + url
        self.url = self.Host + url
        self.trade_id = trade_id
        self.trade_id1 = trade_id1
        self.oids = oids
        self.oids1 = oids1
        get_invoice_type = get_invoice_type
        data = {"type": 2, "do_type": "2", "get_invoice_type": get_invoice_type, "express_info_id": "0",
                "printer_express": "QR-588 LABEL (副本 3)", "printer_invoice": "QR-588 LABEL (副本 3)",
                "checked_express": "false", "checked_invoice": "false",
                "trade_ids": [{"trade_id": self.trade_id, "oids": [self.oids]},
                              {"trade_id": self.trade_id1, "oids": [self.oids1]}]}
        rep = requests.post(url=self.url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_Prints_setPrinter_url(self):
        # 设置默认打印机接口
        url = Order_Tool().rpc_Prints_setPrinter_url
        self.url = self.Host + url
        self.data = {"printer_express": "QR-588 LABEL (副本 3)", "printer_invoice": "QR-588 LABEL (副本 3)"}
        rep = requests.post(url=self.url, headers=self.headers, json=self.data)
        logger.info("接口{}请求成功,返回数据为:{}".format(self.url, rep.json()))
        return rep

    def rpc_configure_getConfigInitData_api(self):
        ## 设置默认发货单模板————获取数据的两个接口(##第一个接口)
        url = self.Host + Order_Tool().rpc_configure_getConfigInitData_url
        data = {"group": 6}
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_Template_list_api(self):
        # 设置默认发货单模板————获取数据的两个接口(##第一个接口)
        url = self.Host + Order_Tool().rpc_Template_list_url
        data = {"category_id": 88, "page": 1, "limit": 1000}
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep

    def rpc_configure_setConfig_api_01(self):
        url = self.Host + Order_Tool().rpc_configure_setConfig_url  # 拼接地址
        # template_invoice的值是发货单模板的id
        data = {"group": 6, "template_invoice": "55", "template_express_custom": "true"}  # 请求数据
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        # headers参数是hjdtoken
        return rep

    def rpc_order_sub_getInvoice_Batch_shipment(self, trade_id, oids, get_invoice_type, trade_id1, oids1):
        # 设置发货单接口
        Print = Print_Shipment()  # 实例化对象调用
        rep = Print.rpc_order_sub_getInvoice_api(trade_id, oids, get_invoice_type, trade_id1, oids1)  # 这里传入形参
        return rep


########################################################################################自由订单功能接口###############################################################################
class Free_Order():
    def __init__(self):
        self.headers = {"hjdtoken": Order_Tool().token}  # 公用的请求头:请求头里是token
        self.Host = Order_Tool().Host  # 服务器的ip或名称

    def rpc_free_address_addAddress_api(self, type, province, city, district, address, name, mobile):
        # 自由订单新增收件地址接口
        type = type  # 正确的值；receiver
        province = province  # 具体省份
        city = city  # 具体市名称
        district = district  # 具体区/县名称
        address = address  # 详细地址
        name = name  # 此地址的名字
        mobile = mobile  # 手机号码
        url = self.Host + Order_Tool().rpc_free_address_addAddress_url  # 拼接请求路径
        data = {"type": type, "province": province, "city": city, "district": district,
                "address": address, "name": name, "mobile": mobile
                }  # 请求数据
        rep = requests.post(url=url, headers=self.headers, json=data)  # 发送请求到服务器
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep.json()  # 接收返回值并把返回值转换为json格式

    def rpc_free_order_saveOrder_api(self):
        # 自由订单新增订单接口
        url = self.Host + Order_Tool().rpc_free_order_saveOrder_url
        data = {
            "orderInfo": "[{\"title\":\"男士衬衫服务市场测试专用\",\"sku_properties_name\":\"\",\"sku_id\":\"573934164201\",\"outer_sku_id\":null,\"price\":\"5.00\",\"num\":1,\"pic_path\":\"https://img.alicdn.com/bao/uploaded/i2/35255526/TB2mIM5XN3IL1JjSZPfXXcrUVXa_!!35255526.jpg\",\"discount_fee\":0}]",
            "trade_from": "", "tid": "", "fee": "", "seller_remarks": "", "buyer_message": "", "replace_id": "0",
            "receiver_id": "984"}
        logger.info("自由订单新增订单接口的测试数据为:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def Free_order_lists_api(self):
        # 自由订单列表获取数据
        url = self.Host + Order_Tool().rpc_order_sub_lists_url
        data = {"is_free": 1, "layId": 10034, "limit": 20, "order_number_type": "1", "page": 1, 'time_type': "1",
                "type": "3"}
        logger.info("测试数据为{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data).json()["data"][0]["trade_id"]
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def logistics_information_api(self, invoice_no):
        # 获取订单的物流信息接口
        url = self.Host + Order_Tool().rpc_order_sub_getLogistics_url
        data = {"invoice_no": invoice_no}
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_product_combo_getSkuList_api(self):
        # 选择淘宝商品接口
        url = self.Host + Order_Tool().rpc_product_combo_getSkuList_url
        data = {"title": "", "page": 1, "limit": 30, "type": "1"}
        logger.info("选择淘宝商品接口的请求数据为{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep

    def free_order_No_api(self):
        # 自由订单取号验证接口
        id = Free_Order().Free_order_lists_api()
        url = self.Host + Order_Tool().rpc_order_sub_getInvoiceJudge
        data = {"trade_ids": [{"trade_id": id, "oids": [id]}], "express_info_id": "0"}
        logger.info("自由订单取号验证接口的请求数据:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_order_sub_orderSend_api(self):
        # 自由订单取号接口
        url = self.Host + Order_Tool().rpc_order_sub_orderSend_url
        data = {"checked_express": "false", "checked_invoice": "false", "type": 2, "express_info_id": "0",
                "get_invoice_type": 2,
                "printer_express": "QR-588 LABEL (副本 3)", "printer_invoice": "QR-588 LABEL (副本 3)",
                "oids": ["1636178283111001"], "trade_id": "1636178283101001"}

        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def order_sub_orderSend_api(self):
        # 自由订单取号发货接口
        url = self.Host + Order_Tool().rpc_order_sub_orderSend_url  # 拼接url
        Free_Order().rpc_free_order_saveOrder_api()  # 这里是调用上面的方法,创建新的自由订单,保证每次使用的订单都是一个新的订单
        time.sleep(5)
        id = Free_Order().Free_order_lists_api()  # 调用上面的方法获取订单编号,这里的订单编号是系统创建的,所以trade_id和ids都是一个
        # 1636342738101001
        oids = id.replace(id[11:], "11001")
        data = {"checked_express": "false", "checked_invoice": "false", "type": 2, "express_info_id": "0",
                "get_invoice_type": 1,
                "printer_express": "QR-588 LABEL (副本 3)", "printer_invoice": "QR-588 LABEL (副本 3)",
                "oids": [oids], "trade_id": id}
        logger.info("自由订单取号发货接口==>接口请求数据:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep


class Commodity_Management():
    # 商品模块测试
    def __init__(self):
        self.headers = {"hjdtoken": Order_Tool().token}  # 公用的请求头:请求头里是token
        self.Host = Order_Tool().Host  # 服务器的ip或名称

    def rpc_product_lists_api(self):
        # 获取商品列表的数据
        url = self.Host + Order_Tool().rpc_product_lists_url
        data = {
            "dataString": "%7B%22cid%22:%22%22,%22checkId%22:%22%22,%22keywords%22:%22%22,%22product_type%22:%22num_iid%22%7D",
            "page": 1, "limit": 20}
        logger.info("请求数据为:page:{},limit:{},dataString:{}".format(data["page"], data["limit"],
                                                                  {"cid": "", "checkId": "", "keywords": "",
                                                                   "product_type": "num_iid"}))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep

    def product_search_api(self):
        # 搜索商品数据
        url = self.Host + Order_Tool().rpc_product_lists_url
        data = {
            "dataString": "%7B%22cid%22:%2250012773%22,%22checkId%22:%22234%22,%22keywords%22:%22626168878736%22,%22product_type%22:%22num_iid%22%7D",
            "page": 1, "limit": 20}
        rep = requests.post(url=url, headers=self.headers, json=data).json()["data"]
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_sku_lists_api(self):
        # 获取单个商品的sku列表
        url = self.Host + Order_Tool().rpc_sku_lists_url
        data = {"num_iid": "625880701144", "page": 1, "limit": 1.7976931348623157e+308}
        logger.info("获取单个商品的sku列表==>请求数据:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_product_combo_list_api(self):
        # 单个商品sku绑定组合的详情列表接口
        url = self.Host + Order_Tool().rpc_product_combo_list_url
        data = {"page": 1, "limit": 10, "current_page": 1, "per_page": 10, "title": "", "is_match": 1}
        logger.info("单个商品sku绑定组合的详情列表接口==>请求数据:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep

    def rpc_sku_matchCombo_api(self):
        # 商品绑定套盒接口
        url = self.Host + Order_Tool().rpc_sku_matchCombo_url
        data = {"sku_id": "5221331559291", "combo_id": "62"}
        logger.info("商品绑定套盒接口==>请求数据:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_sku_cancelMatchCombo_api(self):
        # 解除商品已经绑定的套盒接口
        url = self.Host + Order_Tool().rpc_sku_cancelMatchCombo_url
        data = {"sku_id": "5221331559291"}
        logger.info("解除商品已经绑定的套盒接口,==>请求数据:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_product_setcate_api(self):
        # 设置商品的对账主体接口
        url = self.Host + Order_Tool().rpc_product_setcate_url
        data = {
            "dataString": "{\"num_iid\":[\"626169538067\",\"617137758223\",\"636079973388\",\"626458019944\"],\"cateVal\":\"263\"}"}
        logger.info("设置商品的对账主体接口,==>请求数据:{}".format(data))
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_product_updateCache_api(self):
        # 商品列表中更新缓存接口
        url = self.Host + Order_Tool().rpc_product_updateCache_url
        data = {}
        logging.info("商品列表中更新缓存接口, 此接口无请求参数, 所以请求参数传给接口的是{}")
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_task_LoadProduct_api(self):
        # 商品列表中同步商品接口&&加载商品接口
        url = self.Host + Order_Tool().rpc_task_LoadProduct_url
        data = {}
        logging.info("商品列表中更新缓存接口, 此接口无请求参数, 所以请求参数传给接口的是{}")
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_Product_addShopProduct_api(self):
        # 新增商品接口
        url = self.Host + Order_Tool().rpc_Product_addShopProduct_url
        data = {"type": 1, "title": "蔡博测试商品1", "short_name": "", "price": "", "outer_iid": "", "m_id": "43", "cost": "",
                "verify_cid": "234",
                "item": [{"outer_iid": "12147412909", "sku_properties_name": "", "barcode": "", "price": 0, "num": 1}]}
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_Product_extractShopProduct_api(self):
        # 提取商品接口
        url = self.Host + Order_Tool().rpc_Product_extractShopProduct_url
        data = {"extractOrderNum": "2080574165623657109"}
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def rpc_Product_addExtractShopProduct_api(self):
        # 保存提取到的商品接口
        url = self.Host + Order_Tool().rpc_Product_addExtractShopProduct_url
        data = {"ExtractShopProductArr": [
            {"num_iid": "626458019944", "cid": "50012771", "verify_cid": "234", "taobao_user_id": "35255526",
             "title": "测试商品2不对外出售", "price": "69.00", "outer_iid": "0", "nr_outer_iid": "0", "type": "0",
             "sku_id": "4606578546255", "outer_sku_id": "0", "sku_properties_name": "颜色分类:白色睡袍;尺码:160(M)",
             "is_free": "0", "status_string": ""}]}
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep.json()))
        return rep

    def portfolio_goods_api(self):
        # 组合商品列表获取数据
        url = self.Host + Order_Tool().rpc_product_combo_list_url
        data = {"page": 1, "limit": 20, "composeGoodsTitle": ""}
        rep = requests.post(url=url, headers=self.headers, json=data)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep

    def rpc_category_status_api(self, data):
        # 对账分类是否启用
        url = self.Host + Tools.rpc_Category_status_url  # 拼接接口URL
        rep = request_tools.request_post(url, data, self.headers)  # 调用封装的请求
        return rep

    def rpc_Category_lock_api(self, data):
        # 对账主体的对账分类是否锁定接口
        url = self.Host + Tools.rpc_Category_lock_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_Category_createUpdateCategory_api(self, data):
        # 修改对账主体中的对账分类数据--接口&&对账分类新增接口
        url = self.Host + Tools.rpc_Category_createUpdateCategory_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_product_lists_api_1(self, data):
        # 商品简称列表获取数据&&商品简称列表组合查询
        url = self.Host + Tools.rpc_product_lists
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_sku_updateSku_api(self, data):
        # 修改单个商品的sku简称
        url = self.Host + Tools.rpc_sku_updateSku_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_stock_lists_api(self, data):
        # 核对商品列表
        url = self.Host + Tools.rpc_stock_lists_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_import_order_list_api(self, data):
        # 导入查看搜索数据&&导入查看获取数据接口
        url = self.Host + Tools.rpc_import_order_lists_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_import_order_importOrderFile_api(self, data):
        # 导入查看上传文件接口&&&这里是前端处理好的数据发送给后端,所以只能通过接口传入处理好的数据流
        url = self.Host + Tools.rpc_import_order_importOrderFile_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_import_order_deleteImportOrder_api(self, data):
        # 导入查看==>删除已导入数据
        url = self.Host + Tools.rpc_import_order_deleteImportOrder_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_order_sub_originalQuery_api(self, data):
        # 底单查询==>详细记录--->获取数据接口
        url = self.Host + Tools.rpc_order_sub_originalQuery_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_order_sub_originalSummaryQuery_api(self, data):
        # 底单查询==>汇总报表-->获取数据接口
        url = self.Host + Tools.rpc_order_sub_originalSummaryQuery_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_order_sub_scan_api(self, data):
        # 扫描发货==>扫描过后获取数据的接口
        url = self.Host + Tools.rpc_order_sub_scan_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_Order_Sub_leakageOrderCheck_api(self, data):
        # 漏单检测接口
        url = self.Host + Tools.rpc_Order_Sub_leakageOrderCheck_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_task_delete_api(self, data):
        # 支付宝删除已上传的数据
        url = self.Host + Tools.rpc_task_delete_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_task_bill_api(self, data):
        # 账单中心==>重新加载&&账单导出任务提交
        url = self.Host + Tools.rpc_task_bill_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_bill_lists_api(self, data):
        # 账单中心==>默认获取数据&&搜索数据
        url = self.Host + Tools.rpc_bill_lists_url
        rep = requests.post(url, data, self.headers)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep


class Order_Management:
    # 订单管理
    def __init__(self):
        self.headers = {"hjdtoken": Order_Tool().token}  # 公用的请求头:请求头里是token
        self.Host = Order_Tool().Host  # 服务器的ip或域名

    def order_list(self, data):
        # 获取订单列表的数据
        url = self.Host + Tools.order_sub_lists_url
        rep = requests.post(url, data, self.headers)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep

    def rpc_refund_lists_api(self, data):
        # 退款订单列表
        url = self.Host + Tools.rpc_refund_lists_url
        rep = requests.post(url, data, self.headers)
        logger.info("接口{}请求成功,返回数据为:{}".format(url, rep))
        return rep


class Multi_Store_Operation:
    def __init__(self):
        # 初始化工作
        self.headers = {"hjdtoken": Order_Tool().token}  # 公用的请求头:请求头里是token
        self.Host = Order_Tool().Host  # 服务器的ip或域名

    def rpc_Shop_switch_setSwitchShop_api(self, data):
        # 多店铺操作==>切换店铺
        url = self.Host + Tools.rpc_Shop_switch_setSwitchShop_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_Shop_getSwitchCode_api(self):
        # 获取关联店铺的数据
        url = self.Host + Tools.rpc_Shop_getSwitchCode_url
        rep = request_tools.request_post(url, {}, self.headers)
        return rep

    def rpc_Shop_createSwitchCode_api(self):
        # 更新店铺的店铺代码
        url = self.Host + Tools.rpc_Shop_createSwitchCode_url
        rep = request_tools.request_post(url, {}, self.headers)
        return rep

    def rpc_Shop_setNick_api(self, data):
        # 修改主店铺的店铺简称
        url = self.Host + Tools.rpc_Shop_setNick_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_Shop_switch_editShopNick_api(self, data):
        # 修改子店铺的店铺简称接口
        url = self.Host + Tools.rpc_Shop_switch_editShopNick_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_Shop_switch_deleteShopSwitch_api(self, data):
        # 解除子店铺的关联/绑定
        url = self.Host + Tools.rpc_Shop_switch_deleteShopSwitch_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def rpc_Shop_switch_addShopSwitch_api(self, data):
        # 绑定店铺
        url = self.Host + Tools.rpc_Shop_switch_addShopSwitch_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

# if __name__ == '__main__':
#     Comm = Commodity_Management()
#     data = {"dataString": "{\"ids\":\"177\",\"checked\":true}"}
#     res = Comm.rpc_category_status_api(data)
#     print(res)
#     a=Comm.sss().json()
#     print(a)
