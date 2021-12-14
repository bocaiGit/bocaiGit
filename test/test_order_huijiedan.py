import time
import pytest
import yaml

from asse.Assertion_Encapsulation import Assert_Encapsulation
from Response_data.Response_information import response_data
# 这里可以将一些接口响应信息过多时,可以放在yaml文件读取,将接口的响应信息和yaml文件的信息做比对
from Log.my_log import logger
# 日志文件的封装
from api.order_huijiedan_api import Test_print_list
# 每个页面的api接口
from api.order_huijiedan_api import Home_console, ManagementCenter, Print_Shipment, Free_Order, Commodity_Management, \
    Order_Management, Multi_Store_Operation
# from api.order_huijiedan_api import *
from Tool.RequestData import requ_data
# 接口的请求数据,封装读取,每次调用
from jsonpath import jsonpath

# 使用jsonpath第三方库提取接口返回的字段用作数据校验


logger.error(
    "=====================================================================================================================================================================================================================================================")


class Test_print():
    def setup_class(self):
        print('接口测试的前置工作')

    @pytest.mark.parametrize("layId", [
        10034, "dshgfdks", "*", ":{>{>", " "
    ])
    @pytest.mark.parametrize("limit", [
        (20), (50), (100),
    ])
    def test_print_list(self, layId, limit):
        # 打单列表
        if layId == 10034:
            Print = Test_print_list()
            status = Print.order_sub_lists(layId, limit).json()['status']
            Assert_Encapsulation(lnterface=status, response=200)
        else:
            Print = Test_print_list()
            status = Print.order_sub_lists(layId, limit).json()['status']
            data = Print.order_sub_lists(layId, limit).json()['data']
            Assert_Encapsulation(lnterface=status, response=200, Interface_data=data, expect_data=[])


# 控制台
class Test_Home_console():

    def setup_method(self):
        self.home = Home_console()

    # 待付款订单后接口
    def test_home_console(self):

        status = self.home.order_sub_lists_payment_url().json()['status']
        Assert_Encapsulation(lnterface=status, response=200)

    # 今日待发货订单后接口
    def test_lists_To_be_shipped(self):

        status = self.home.order_sub_lists_To_be_shipped_url().json()["status"]
        Assert_Encapsulation(lnterface=status, response=200)

    # 今日退款订单后接口
    def test_lists_refund(self):

        status = self.home.order_sub_lists_refund_url().json()['status']
        Assert_Encapsulation(lnterface=status, response=200)

    # 配置中心，一共会触发2次请求
    def test_configure_getConfigInitData(self):
        status = self.home.configure_getConfigInitData().json()['status']
        status1 = self.home.configure_getConfigInitData1().json()["status"]
        Assert_Encapsulation(lnterface=status, response=200, Interface_data=status, expect_data=201)

    # 账单中心的接口
    def test_bill_lists(self):
        status = self.home.bill_lists().json()['status']
        msg = self.home.bill_lists().json()['msg']
        Assert_Encapsulation(code=status, resp_code=200, msg=msg, resp_msg="数据加载成功")

    # 实名认证的接口
    def test_list_Real_name(self):
        status = self.home.order_sub_list_Real_name().json()['status']
        msg = self.home.order_sub_list_Real_name().json()['msg']
        Assert_Encapsulation(code=status, resp_code=200, msg=msg, resp_msg="数据加载成功")

    # 商品简称接口
    @pytest.mark.parametrize("dataString, limit, page", (
            [{"cid": "", "keywords": "", "product_type": "num_iid"}, 20, 1],
            [{"product_type": "num_iid"}, 50, 3],), ids=["商品简称第一次请求", "商品简称第二次请求"]
                             )
    def test_rpc_product_lists(self, dataString, limit, page):
        if limit == 20:
            status = self.home.rpc_product_lists(dataString, limit, page).json()['status']
            data = self.home.rpc_product_lists(dataString, limit, page).json()['data']
            Assert_Encapsulation(lnterface=status, response=200, Interface_data=data, expect_data=[])
        else:
            status = self.home.rpc_product_lists(dataString, limit, page).json()['status']
            data = self.home.rpc_product_lists(dataString, limit, page).json()['data']
            print(data)
            Assert_Encapsulation(lnterface=status, response=200)

    # 短信充值接口
    @pytest.mark.parametrize('DATASTRING', [("{\"v\":\"1\"}"), ], ids=["短信充值接口"])
    def test_rpc_Recharge_vNo(self, DATASTRING):
        # 第一个接口
        MSG = self.home.rpc_supply_product(DATASTRING).json()['msg']
        STATUS = self.home.rpc_supply_product(DATASTRING).json()['status']
        DATA = self.home.rpc_supply_product(DATASTRING).json()['data']
        Assert_Encapsulation(code=STATUS, resp_code=200, msg=MSG, resp_msg="加载成功")


# 物流配置
class Test_ManagementCenter():
    def setup_method(self):
        # 物流配置接口
        self.ManagementCenter = ManagementCenter()

    @pytest.mark.parametrize("limit", [(20), ("*"), (" "), ("[;[.;[;")])
    @pytest.mark.parametrize("page", [(1), ("*"), (" "), ("回复']']'’】‘")])
    def test_logistics_getLogisticsLists(self, limit, page):
        if limit == 20 and page == 1:
            status = self.ManagementCenter.rpc_logistics_getLogisticsLists(limit, page).json()['status']
            datas = self.ManagementCenter.rpc_logistics_getLogisticsLists(limit, page).json()['data']
            Assert_Encapsulation(lnterface=status, response=200, Interface_data=datas, expect_data=[])
        else:
            status1 = self.ManagementCenter.rpc_logistics_getLogisticsLists(limit, page).json()['status']
            Assert_Encapsulation(Interface_data=status1, expect_data=200)

    @pytest.mark.parametrize("limit", [(20), ("*"), (" "), ("[;[.;[;")])
    @pytest.mark.parametrize("page", [(1), ("*"), (" "), ("回复']']'’】‘")])
    def test_logistics_getMatchRuleLists(self, limit, page):
        """
        物流策略接口,此接口后端有设置默认参数,所以传入异常参数,接口返回结果也是正常的
        :param limit: 请求参数
        :param page: 请求参数
        :return:
        """
        msg = self.ManagementCenter.rpc_logistics_getMatchRuleLists(limit, page).json()['msg']
        status = self.ManagementCenter.rpc_logistics_getMatchRuleLists(limit, page).json()['status']
        datas = self.ManagementCenter.rpc_logistics_getMatchRuleLists(limit, page).json()['data']
        Assert_Encapsulation(lnterface=status, response=200, Interface_data=datas, expect_data=[])

    @pytest.mark.parametrize("alias,api_type_id,assign_type,express_id,name,phone,shipp_address,template",
                             yaml.safe_load(
                                 open(r"G:\order_huijiedan\yaml_data\rpc_logistics_createUpdateLogistics_data.yaml",
                                      "r", encoding="utf-8")))  ###新增物流配置
    def test_logistics_createUpdateLogistics(self, alias, api_type_id, assign_type, express_id, name, phone,
                                             shipp_address, template):
        """
        此接口正确参数:{{"api_type_id":"2","alias":"测试自动化","template":"53",
        "assign_type":"1","name":"蔡博","phone":"17681843982",
        "shipp_address":"山东省 青岛市 城阳区 城阳区玉皇岭工业园青虹路29号","express_id":"26",}}
        :return:
        """

        logger.info(
            "alias的参数为{},api_type_id的参数为 {} ,\nassign_type的参数为 {} ,express_id的参数为 {} ,\nname的参数为 {} ,"
            "phone的参数为 {} ,\nshipp_address的参数为 {} ,template的参数为 {} \n请求结果::".format(
                alias, api_type_id,
                assign_type,
                express_id, name, phone, shipp_address, template))

        status = \
            self.ManagementCenter.rpc_logistics_createUpdateLogistics(alias, api_type_id, assign_type, express_id, name,
                                                                      phone, shipp_address, template).json()
        Assert_Encapsulation(lnterface=status,
                             response={'code': 0, 'status': 200, 'sub_code': 'success', 'msg': '操作成功'})

    # 批量删除接口
    @pytest.mark.parametrize("ids", ([171], [172], ["!##!"], [" "], ["*"]),
                             ids=["物流配置批量删除接口", "物流配置批量删除接口", "物流配置批量删除接口", "物流配置批量删除接口", "物流配置批量删除接口"])
    def test_logistics_deleteLogistics(self, ids):

        data = self.ManagementCenter.logistics_deleteLogistics(ids).json()
        Assert_Encapsulation(lnterface=data, response={'code': 0, 'status': 201, 'sub_code': 'error', 'msg': '请求错误'})

    @pytest.mark.parametrize(
        "id, taobao_user_id, express_id, alias, assign_type, name,status, phone, api_type_id, template,customer_id, customer_code, service_code, shipp_address, is_vip,created, express, address, api",
        yaml.safe_load(
            open(r"G:\order_huijiedan\yaml_data\rpc_logistics_createUpdateLogistics1.yaml", "r", encoding="utf-8")))
    def test_rpc_logistics_createUpdateLogistics1(self, id, taobao_user_id, express_id, alias, assign_type, name,
                                                  status, phone, api_type_id, template, customer_id, customer_code,
                                                  service_code, shipp_address, is_vip, created, express, address, api):
        '''修改物流配置接口'''
        msg = self.ManagementCenter.rpc_logistics_createUpdateLogistics1(id, taobao_user_id, express_id, alias,
                                                                         assign_type, name, status, phone, api_type_id,
                                                                         template, customer_id, customer_code,
                                                                         service_code,
                                                                         shipp_address, is_vip, created, express,
                                                                         address, api).json()
        Assert_Encapsulation(lnterface=msg, response={'code': 0, 'msg': '操作成功', 'status': 200, 'sub_code': 'success'})

    @pytest.mark.parametrize(
        "id, condition_type, rule_type, area_value, area_name, condition_type1,area_value1, area_name1,rule_name, remarks, type, status, do_code, express_id, priority",
        yaml.safe_load(open(r"G:\order_huijiedan\yaml_data\rpc_logistics_setMatchRule.yaml", "r",
                            encoding="utf-8")))
    def test_rpc_logistics_setMatchRule(self, id, condition_type, rule_type, area_value, area_name, condition_type1,
                                        area_value1, area_name1,
                                        rule_name, remarks, type, status, do_code, express_id, priority):
        # 新增物流策略接口
        data_s = \
            self.ManagementCenter.rpc_logistics_setMatchRule(id, condition_type, rule_type, area_value, area_name,
                                                             condition_type1,
                                                             area_value1, area_name1,
                                                             rule_name, remarks, type, status, do_code, express_id,
                                                             priority).json()
        response_data = {'status': 1001, 'msg': '非法请求，请先登录！', 'data': {
            'url': 'https://oauth.taobao.com/authorize?response_type=code&client_id=23697889&redirect_uri=https%3A%2F%2Forder.huijiedan.cn%2Fload.html&state=TB_0_0&encode=utf-8&view=web'}}
        Assert_Encapsulation(lnterface=data_s, response=response_data)

    @pytest.mark.parametrize("ids", ([112], [' '], ['*']))
    def test_rpc_logistics_deleteMatchRule(self, ids):
        ##批量删除1物流策略接口
        status = self.ManagementCenter.rpc_logistics_deleteMatchRule(ids[0]).json()
        Assert_Encapsulation(lnterface=status, response={'code': 1, 'msg': '规则删除失败', 'status': 201})

    @pytest.mark.parametrize('seller_template_id', (
            [59], [5623537829525295572355328795263953458756298573453492853475632958757473285632859375], [' '],
            ["流口水更客观地供货商开给对方@%￥#@￥@%#@"]))
    def test_rpc_Template_info(self, seller_template_id):
        if seller_template_id == [59]:
            msg = self.ManagementCenter.rpc_Template_info(seller_template_id).json()['msg']
            code = self.ManagementCenter.rpc_Template_info(seller_template_id).json()
            logger.info("获取快递单模板接口请求成功, 接口数据返回正常")
            assert msg == "获取模板数据成功"
        else:
            msg = self.ManagementCenter.rpc_Template_info(seller_template_id).json()['msg']
            code = self.ManagementCenter.rpc_Template_info(seller_template_id).json()
            logger.info("获取快递单模板接口请求成功, 接口数据返回正常,")
            assert msg != "获取模板数据成功"


class Test_Template_center():
    #############新增快递单模板##############
    def setup_method(self):
        self.ManagementCenter = ManagementCenter()

    @pytest.mark.parametrize("category_id", ([87], ['fsgfsjfs'], [" "], ["*#$%#%$#%"]))
    def test_rpc_Template_CommonList(self, category_id):
        # 新建快递单模板请求的第一个接口,用于获取模板尺寸
        status = self.ManagementCenter.rpc_Template_CommonList(category_id).json()['status']
        assert status == 200
        if category_id == [87]:
            logger.info("新建快递单模板,第一个接口请求成功,用于获取模板尺寸请求数据为 : {}".format(category_id))
        elif category_id != [87]:
            logger.info("注意请求数据::[{}],请求数据不正确,这是由于接口有默认数据,新建快递单模板,第一个接口请求成功,用于获取模板尺寸".format(category_id))

    @pytest.mark.parametrize("common_template_id", ([465713], ['gfsfhgakfha森岛帆高就是个'], [" "], ["$#@$@#$***"]))
    def test_rpc_Template_CommonInfo(self, common_template_id):
        # 新建快递单模板请求的第二个接口,用于已经选择的模板尺寸的详细数据
        if common_template_id == [465713]:
            status = self.ManagementCenter.rpc_Template_CommonInfo(common_template_id).json()['status']
            data = self.ManagementCenter.rpc_Template_CommonInfo(common_template_id).json()['data']
            logger.info("新建快递单模板,第一个接口请求成功,用于获取模板尺寸请求数据为 : {}".format(common_template_id))
            assert status == 200 and data != {}
        else:
            data = self.ManagementCenter.rpc_Template_CommonInfo(common_template_id).json()
            logger.info("注意请求数据::[{}],请求数据不正确,这是由于接口有默认数据,新建快递单模板,第一个接口请求成功,用于获取模板尺寸".format(common_template_id))
            assert data == {'status': 200, 'data': None}

    @pytest.mark.parametrize(
        "category_id, template_name, express_code, width, height, template_id, needTopLogo,horizontalOffset, verticalOffset",
        yaml.safe_load(open(r"G:\order_huijiedan\yaml_data\rpc_Template_create.yaml", "r", encoding="utf-8")))
    def test_rpc_Template_create(self, category_id, template_name, express_code, width, height, template_id,
                                 needTopLogo,
                                 horizontalOffset, verticalOffset):
        # 新建快递单模板请求的第三个接口,用于保存模板数据
        if category_id == 87:
            status = self.ManagementCenter.rpc_Template_create(category_id, template_name, express_code, width, height,
                                                               template_id, needTopLogo,
                                                               horizontalOffset, verticalOffset).json()['status']
            msg = self.ManagementCenter.rpc_Template_create(category_id, template_name, express_code, width, height,
                                                            template_id, needTopLogo,
                                                            horizontalOffset, verticalOffset).json()['msg']
            logger.info("保存模板数据接口请求成功, 接口返回数据正确")
            assert status == 200 and msg == '添加模板成功'
        else:
            status = self.ManagementCenter.rpc_Template_create(category_id, template_name, express_code, width, height,
                                                               template_id, needTopLogo,
                                                               horizontalOffset, verticalOffset).json()
            logger.info("保存模板数据接口请求成功, 接口返回数据正确,由于是异常参数,所以接口的返回是错误的,具体如下: {}".format(status))
            assert status == {'msg': '模板分类必须是：快递单、发货单、备货单或备货单小标签', 'status': 201}

    ###############发货单接口##############
    @pytest.mark.parametrize("seller_template_id,common_template_id",
                             ([107, 206], ["dfg34", " "], ["*", "*"], ["fgf说%#%^$的跟", "十几个时间#%#$"]))
    def test_Shipment_edit(self, seller_template_id, common_template_id):
        # 发货单编辑,可能由于环境中的模板被删除,会出错,所以需要时常检查
        if seller_template_id == 107 and common_template_id == 206:
            status = self.ManagementCenter.Shipment_edit_1(seller_template_id).json()['status']
            data = self.ManagementCenter.Shipment_edit_1(seller_template_id).json()['data']
            msg = self.ManagementCenter.Shipment_edit_1(seller_template_id).json()['msg']
            try:
                assert status == 200 and data != {} and msg == "获取模板数据成功"
            except KeyError:
                logger.exception("此时报错是因为,环境中的发货单模板数据被删除导致的")
            else:
                logger.info("发货单接口请求成功,接口返回正确,数据校验正确")
            status1 = self.ManagementCenter.Shipment_edit_2(common_template_id).json()['status']
            data = self.ManagementCenter.Shipment_edit_2(common_template_id).json()['data']
            assert status1 == 200 and data != {}
            logger.info("发货单编辑第二个接口请求正确,接口返回正确,数据校验成功")
        else:
            status1 = self.ManagementCenter.Shipment_edit_1(seller_template_id).json()
            assert status1 == {'status': 201, 'msg': '获取模板数据失败'}
            status2 = self.ManagementCenter.Shipment_edit_2(common_template_id).json()
            logger.info("发货单编辑接口请求数据为异常数据: [seller_template_id:{},common_template_id:{} ],请求成功,接口返回数据符合预期结果".format(
                seller_template_id, common_template_id))
            assert status2 == {'status': 200, 'data': None}

    ########################################################忽略下面第一条测试用例####################################################
    @pytest.mark.xfail
    @pytest.mark.parametrize("print_express,print_invoice,seller_template_id", (
            ["true", "false", 5], ["false", "true", 5], ["true", "true", " "], [" ", " ", " "], ["*", "*", "*"]))
    def test_rpc_Template_preview(self, print_express, print_invoice, seller_template_id):
        # 发货单预览
        if seller_template_id == 5 and print_express == "true" and print_invoice == "false":
            status2 = self.ManagementCenter.rpc_Template_preview(print_express, print_invoice, seller_template_id)
            assert status2 != {}
        elif seller_template_id == 5 and print_express == "false" and print_invoice == "true":
            status = \
                self.ManagementCenter.rpc_Template_preview(print_express, print_invoice, seller_template_id).json()[
                    'status']
            msg = self.ManagementCenter.rpc_Template_preview(print_express, print_invoice, seller_template_id).json()[
                'msg']
            data = self.ManagementCenter.rpc_Template_preview(print_express, print_invoice, seller_template_id).json()[
                'data']
            assert status == 200 and msg == "获取模板数据成功" and data != {}
        else:
            status1 = self.ManagementCenter.rpc_Template_preview(print_express, print_invoice,
                                                                 seller_template_id).json()
            assert status1 == {'sub_code': 'error', 'status': 201, 'msg': '请先创建发货单模板！'}

    def test_rpc_Template_edit(self):
        # 保存发货单接口
        status = self.ManagementCenter.rpc_Template_edit_url().json()
        logger.info("保存发货单数据接口请求成功,接口返回数据正确,数据校验成功")
        assert status == {'status': 200, 'msg': '编辑模板成功'}

    @pytest.mark.parametrize("receiver", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\rpc_order_addressAnalysis_data.yaml", "r", encoding="utf-8")))
    def test_rpc_order_addressAnalysis(self, receiver):
        # 地址配置中的智能识别地址接口
        status = self.ManagementCenter.rpc_order_addressAnalysis(receiver).json()["status"]
        code = self.ManagementCenter.rpc_order_addressAnalysis(receiver).json()['code']
        msg = self.ManagementCenter.rpc_order_addressAnalysis(receiver).json()["msg"]
        try:
            assert status == 200 and code == 0 and msg == ''
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
        else:
            logger.info("断言成功,测试通过")

    @pytest.mark.parametrize(" addr, city, id, contact_name, country, mobile_phone, province, zip_code", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\test_rpc_order_sender_saveSender_data.yaml", "r", encoding="utf-8")),
                             ids=["保存新建地址1", "保存新建地址2", "保存新建地址3", "保存新建地址4"])
    def test_rpc_order_sender_saveSender(self, addr, city, id, contact_name, country, mobile_phone, province, zip_code):
        global Interface_return
        # 保存新建的地址
        if id == 2061976002:
            status = \
                self.ManagementCenter.rpc_order_sender_saveSender_url(addr, city, id, contact_name, country,
                                                                      mobile_phone,
                                                                      province, zip_code).json()['status']
            try:
                assert status == 200
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
            else:
                logger.info("断言成功,测试通过")
        else:
            try:
                Interface_return = self.ManagementCenter.rpc_order_sender_saveSender_url(addr, city, id, contact_name,
                                                                                         country,
                                                                                         mobile_phone, province,
                                                                                         zip_code).json()
                assert Interface_return == {'code': 0, 'msg': '电话不符合指定规则', 'status': 201,
                                            'data': []} or Interface_return == {'code': 0, 'data': [], 'msg': '非法省',
                                                                                'status': 201}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
            else:
                logger.info("断言成功,测试通过")

    @pytest.mark.parametrize("ids",
                             ([2034722003], ['fhafklasfkjajh'], [" "], ["*"]))  # 这里是给形参ids传的参数每个列表是一组参数，这里是4组参数会请求接口4次
    # 参数类型：正确，异常的，为空的，为*好的
    def test_rpc_order_sender_delSender_api(self, ids):
        if ids == [2034722003]:  # 去做一个分支参数为正常时走这个
            status = self.ManagementCenter.rpc_order_sender_delSender_api(ids).json()
            assert status == {"code": 0, "msg": "删除成功", "status": 200} \
                   or status == {'code': 0, 'msg': '删除失败, 请同步淘宝地址', 'status': 201}
            logger.error("这里使用的or逻辑运算,主要是为了防止出错")
            # assert status=={'code': 0, 'msg': '删除失败, 请同步淘宝地址', 'status': 201}
        else:  # 其他异常参数都走这个分支
            data = self.ManagementCenter.rpc_order_sender_delSender_api(ids).json()
            assert data == {'code': 0, 'msg': 'Invalid arguments:contact_id', 'status': 201} \
                   or data == {'code': 0, 'msg': 'Missing required arguments:contact_id', 'status': 201} \
                   or data == {'code': 0, 'msg': 'Invalid arguments:contact_id', 'status': 201}

    # 基础配置保存接口
    @pytest.mark.parametrize("basic_order_check,basic_order_send,order_send", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\rpc_configure_setConfig_data.yaml", "r", encoding="utf-8")))
    def test_rpc_configure_setConfig(self, basic_order_check, basic_order_send, order_send):
        status = self.ManagementCenter.rpc_configure_setConfig_api(basic_order_check, basic_order_send,
                                                                   order_send).json()
        assert status == {'code': 0, 'status': 200, 'sub_code': 'success', 'msg': '修改配置成功'}
        logger.info("修改完基础配置后,请求成功,接口返回数据校验成功")

    # 充值记录接口
    @pytest.mark.parametrize("page,limit",
                             ([1, 10], [1, 50], [1, 500], [1, 5000], [" ", " "], ["fsgffgshjdfsdfjh", "fsdfsgdfsdjfh"]),
                             ids=["充值记录获取10条数据", "充值记录获取50条数据", "充值记录获取500条数据", "充值记录获取5000条数据", "充值记录请求参数异常1",
                                  "充值记录请求参数异常2"])
    def test_rpc_Recharge_rechargeLog_api(self, page, limit):
        if page == 1:
            status = self.ManagementCenter.rpc_Recharge_rechargeLog_api(page, limit).json()['status']
            sub_code = self.ManagementCenter.rpc_Recharge_rechargeLog_api(page, limit).json()['sub_code']
            msg = self.ManagementCenter.rpc_Recharge_rechargeLog_api(page, limit).json()['msg']
            logger.info("充值记录接口获取数据请求正常")
            assert status == 200 and sub_code == "success" and msg == "请求成功"
        else:
            data_s1 = self.ManagementCenter.rpc_Recharge_rechargeLog_api(page, limit).json()
            try:
                assert data_s1 == {'sub_code': 'error', 'status': 201, 'msg': 'A non-numeric value encountered'}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("dataString", (("%7B%22id%22:%222%22%7D"), (4324328476324), (" "), ("*")))
    def test_rpc_notice(self, dataString):
        code = self.ManagementCenter.rpc_notice_lists_api().json()['code']
        data = self.ManagementCenter.rpc_notice_lists_api().json()['data']
        assert code == 0 and data != {}
        code = self.ManagementCenter.rpc_notice_lists_api().json()['code']
        data = self.ManagementCenter.rpc_notice_lists_api().json()['data']
        if dataString == "%7B%22id%22:%222%22%7D":
            try:
                assert code == 0 and data != {}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")
        else:
            Error_code = self.ManagementCenter.rpc_notice_info_api(dataString).json()
            try:
                assert Error_code == {'code': 0, 'status': 200}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")


class Test_Print_lists():
    Print_Shipment = Print_Shipment()

    def setup_class(self):
        print("打单列表功能接口测试开始时间：",
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 获取系统的当前时间，方法：setup_class会在测试开始前执行一次

    def teardown_class(self):
        print("打单列表功能接口测试结束时间：",
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 获取当前系统的时间，方法：teardown_class会在测试结束后执行一次

    @pytest.mark.parametrize("group,sort_order,sort_type", yaml.safe_load(
        open("G:\order_huijiedan\yaml_data\print_advanced_setting_data.yaml", "r", encoding="utf-8")))
    def test_rpc_configure_setConfig(self, group, sort_order, sort_type):
        # 修改高级设置的接口
        status = self.Print_Shipment.rpc_configure_setConfig_api(group, sort_order, sort_type).json()
        try:
            assert status == {'code': 0, 'status': 200, 'sub_code': 'success', 'msg': '修改配置成功'}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("layId,list_type,time_type,type,order_number_type,page,limit,sort_type,sort_order",
                             yaml.safe_load(open(r"G:\order_huijiedan\yaml_data\rpc_order_sub_lists_data.yaml", "r",
                                                 encoding="utf-8")))
    def test_rpc_order_sub_lists(self, layId, list_type, time_type, type, order_number_type, page, limit, sort_type,
                                 sort_order):
        if layId == 10034:
            if sort_type == "pay_time":
                status = \
                    self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                page, limit, sort_type, sort_order).json()['status']
                code = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                   page, limit, sort_type, sort_order).json()['code']
                msg = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                  page, limit, sort_type, sort_order).json()['msg']
                data = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                   page, limit, sort_type, sort_order).json()['data']
                try:
                    assert status == 200 and code == 0 and msg == "数据加载成功" and data != []
                except AssertionError:
                    logger.exception("断言失败,测试用例不通过")
                    raise
                else:
                    logger.info("断言成功,用例通过!")
            elif sort_type == "created":
                # 这个参数修改完高级设置后请求的第二个接口
                status1 = \
                    self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                page, limit, sort_type, sort_order).json()['status']
                code1 = \
                    self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                page, limit, sort_type, sort_order).json()['code']
                msg1 = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                   page, limit, sort_type, sort_order).json()['msg']
                data1 = \
                    self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                page, limit, sort_type, sort_order).json()['data']
                try:
                    assert status1 == 200 and code1 == 0 and msg1 == "数据加载成功" and data1 != []
                except AssertionError:
                    logger.exception("断言失败,测试用例不通过")
                    raise
                else:
                    logger.info("断言成功,用例通过!")


        elif layId == "dgjsdj":
            status = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                 page, limit, sort_type, sort_order).json()['status']
            code = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                               page, limit, sort_type, sort_order).json()['code']
            msg = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                              page, limit, sort_type, sort_order).json()['msg']
            data = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                               page, limit, sort_type, sort_order).json()['data']
            try:
                assert status == 200 and code == 0 and msg == "数据加载成功" and data != []
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")


        else:
            error_rep = \
                self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                            page, limit, sort_type, sort_order).json()['msg']
            code = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                               page, limit, sort_type, sort_order).json()['code']
            status = self.Print_Shipment.rpc_order_sub_lists_api(layId, list_type, time_type, type, order_number_type,
                                                                 page, limit, sort_type, sort_order).json()['status']
            try:
                assert error_rep == '数据加载失败：Undefined index: keyword/usr/share/nginx/html/application/common/lib/OrderCache.php860' and code == 0 and status == 201
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("trade_id", ((2050350186405657109), ("ghjfjhgfjh@%$"), (""), ("*")))
    def test_rpc_order_orderDetailLog(self, trade_id):
        # 单个订单的日志接口
        if trade_id == 2050350186405657109:
            status = self.Print_Shipment.rpc_order_orderDetailLog_api(trade_id).json()['status']
            data = self.Print_Shipment.rpc_order_orderDetailLog_api(trade_id).json()['data']
            try:
                assert status == 200 and data != {}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")
        else:
            code = self.Print_Shipment.rpc_order_orderDetailLog_api(trade_id).json()
            assert code == {'sub_code': 'error', 'status': 201, 'msg': 'Undefined index: log'}

    @pytest.mark.parametrize("trade_id", (("2050350186405657109"), ("ghjfjhgfjh@%$"), ("*"), (" ")))
    def test_rpc_order_orderDetail(self, trade_id):
        if trade_id == "2050350186405657109":
            status = self.Print_Shipment.rpc_order_orderDetail_api(trade_id).json()["data"]["trade_id"]
            assert status == trade_id
        else:
            code = self.Print_Shipment.rpc_order_orderDetail_api(trade_id).json()
            assert code == {'code': 0, 'msg': '数据加载成功', 'status': 200,
                            'data': {'tid': '', 'buyer_nick': '', 'encrypt_buyer_nick': '', 'count': 0, 'created': '',
                                     'pay_time': '', 'consign_time': '', 'end_time': '', 'modified': '', 'status': '',
                                     'type_string': '', 'get_invoice_status': -1, 'receiver': '', 'item': [],
                                     'logistic': [], 'cost': [], 'item_count': 1}}

    @pytest.mark.parametrize("flag,is_free,remarks,trade_id", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\rpc_order_sub_memoUpdate_data.yaml", "r", encoding="utf-8")))
    def test_rpc_order_sub_memoUpdate_api(self, flag, is_free, remarks, trade_id):
        status = self.Print_Shipment.rpc_order_sub_memoUpdate_api(flag, is_free, remarks, trade_id).json()
        try:
            assert status == {'code': 0, 'sub_code': 'success', 'msg': '订单备注修改成功', 'error_data': [], 'status': 200,
                              'save_res': []}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("tids", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\rpc_order_decryptLists_data.yaml", "r", encoding="utf-8")))
    def test_rpc_order_decryptLists_api(self, tids):
        # 修改收件地址接口
        if tids == 2051511115069657109:
            status = self.Print_Shipment.rpc_order_decryptLists_api(tids).json()
            try:
                assert status == {'code': 0, 'status': 200, 'msg': '数据加载成功', 'data': [
                    {'tid': '2051511115069657109', 'receiver_mobile': '15003777184', 'receiver_phone': '',
                     'receiver_name': '菠菜', 'receiver_address': ' 浙江省 杭州市 上城区九堡街道近胜嫁路商品交易中心a楼512',
                     'address': '九堡街道近胜嫁路商品交易中心a楼512'}]}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")
        elif tids != 2051511115069657109:
            code = self.Print_Shipment.rpc_order_decryptLists_api(tids).json()
            try:
                assert code == {'code': 0, 'msg': '数据解密失败', 'status': 201} or code == {'code': 0,
                                                                                       'data': [{
                                                                                           'address': '九堡街道近胜嫁路商品交易中心a楼512',
                                                                                           'receiver_address': ' 浙江省 杭州市 上城区九堡街道近胜嫁路商品交易中心a楼512',
                                                                                           'receiver_mobile': '15003777184',
                                                                                           'receiver_name': '菠菜',
                                                                                           'receiver_phone': '',
                                                                                           'tid': '2051511115069657109'}],
                                                                                       'msg': '数据加载成功',
                                                                                       'status': 200}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("num_iid,short_name",
                             ((653229344554, "自动化测试修改商品简称"), ("gdghdskgfdg", 53453534795435), (1, "测试"), (" ", " ")))
    def test_rpc_product_updateProduct_api(self, num_iid, short_name):
        # 修改商品简称接口
        if num_iid == 653229344554:
            status = self.Print_Shipment.rpc_product_updateProduct_api(num_iid, short_name).json()
            try:
                assert status == {'code': 0, 'msg': 'success', 'status': 200}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")
        else:
            code = self.Print_Shipment.rpc_product_updateProduct_api(num_iid, short_name).json()
            try:
                assert code == {'code': 0, 'msg': 'success', 'status': 200}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize(
        "buyer_nick, is_get_invoice_sub, is_message, is_not_refund, is_print_express, is_print_invoice, is_unpack,keyword,keyword2, keyword3, layId, limit, list_type,order_number, order_number_type, page, receiver_name, seller_flag, sort_order, sort_type, time,time_type, trade_id, type",
        yaml.safe_load(
            open(r"G:\order_huijiedan\yaml_data\rpc_order_sub_print_lists_query_data.yaml", "r", encoding="utf-8")))
    def test_rpc_order_sub_print_lists(self, buyer_nick, is_get_invoice_sub, is_message, is_not_refund,
                                       is_print_express, is_print_invoice, is_unpack,
                                       keyword,
                                       keyword2, keyword3, layId, limit, list_type,
                                       order_number, order_number_type, page, receiver_name, seller_flag, sort_order,
                                       sort_type, time,
                                       time_type, trade_id, type):
        # 打单列表查询接口
        if order_number != 15003777184:
            data = self.Print_Shipment.rpc_order_sub_print_lists(buyer_nick, is_get_invoice_sub, is_message,
                                                                 is_not_refund, is_print_express, is_print_invoice,
                                                                 is_unpack,
                                                                 keyword,
                                                                 keyword2, keyword3, layId, limit, list_type,
                                                                 order_number, order_number_type, page, receiver_name,
                                                                 seller_flag, sort_order, sort_type, time,
                                                                 time_type, trade_id, type).json()['data']
            status = self.Print_Shipment.rpc_order_sub_print_lists(buyer_nick, is_get_invoice_sub, is_message,
                                                                   is_not_refund, is_print_express, is_print_invoice,
                                                                   is_unpack,
                                                                   keyword,
                                                                   keyword2, keyword3, layId, limit, list_type,
                                                                   order_number, order_number_type, page, receiver_name,
                                                                   seller_flag, sort_order, sort_type, time,
                                                                   time_type, trade_id, type).json()["status"]
            try:
                if data == []:
                    assert status == 200
                else:
                    assert data != [] and status == 200
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

        else:
            code = self.Print_Shipment.rpc_order_sub_print_lists(buyer_nick, is_get_invoice_sub, is_message,
                                                                 is_not_refund, is_print_express, is_print_invoice,
                                                                 is_unpack,
                                                                 keyword,
                                                                 keyword2, keyword3, layId, limit, list_type,
                                                                 order_number, order_number_type, page, receiver_name,
                                                                 seller_flag, sort_order, sort_type, time,
                                                                 time_type, trade_id, type).json()['code']
            status_01 = self.Print_Shipment.rpc_order_sub_print_lists(buyer_nick, is_get_invoice_sub, is_message,
                                                                      is_not_refund, is_print_express, is_print_invoice,
                                                                      is_unpack,
                                                                      keyword,
                                                                      keyword2, keyword3, layId, limit, list_type,
                                                                      order_number, order_number_type, page,
                                                                      receiver_name,
                                                                      seller_flag, sort_order, sort_type, time,
                                                                      time_type, trade_id, type).json()['status']
            msg = self.Print_Shipment.rpc_order_sub_print_lists(buyer_nick, is_get_invoice_sub, is_message,
                                                                is_not_refund, is_print_express, is_print_invoice,
                                                                is_unpack,
                                                                keyword,
                                                                keyword2, keyword3, layId, limit, list_type,
                                                                order_number, order_number_type, page,
                                                                receiver_name,
                                                                seller_flag, sort_order, sort_type, time,
                                                                time_type, trade_id, type).json()['msg']
            try:
                assert code == 0 and status_01 == 200 and msg == '数据加载成功'
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("trade_id", ((2057674277879657109), (" "), ("*"), ("$@##$#@$")))
    def test_rpc_order_sub_listsWaitMerge_api(self, trade_id):
        # 待合并订单接口
        if trade_id == 2057674277879657109:
            requ = self.Print_Shipment.rpc_order_sub_listsWaitMerge_api(trade_id).json()
            data = self.Print_Shipment.rpc_order_sub_listsWaitMerge_api(trade_id).json()["data"]["buyer_nick"]
            print(requ)
            try:
                assert data == "tb100502162"
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")
        else:
            response = self.Print_Shipment.rpc_order_sub_listsWaitMerge_api(trade_id).json()
            try:
                assert response == {'code': 0, 'status': 200, 'sub_code': 'success', 'msg': '获取成功',
                                    'data': {'buyer_nick': '', 'wait_merge_count': 0, 'wait_merge_data': [],
                                             'address_count': 0, 'address_data': []}}
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("trade_id", (["2060551476606423439,2060552052699423439"]))
    def test_rpc_trade_merge_api_testing(self, trade_id):
        # 合并订单检测接口
        data_mergeToken = self.Print_Shipment.rpc_trade_merge_api_testing(trade_id).json()["mergeToken"]
        data_trade_id = self.Print_Shipment.rpc_trade_merge_api_testing(trade_id).json()["data"]["trade"][0]["trade_id"]
        try:
            assert data_mergeToken != "" and data_trade_id == "2060551476606423439"
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("trade_id,action,address_id", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\rpc_trade_merge_api_merge_data.yaml", "r", encoding="utf-8")))
    def test_rpc_trade_merge_api_merge(self, trade_id, action, address_id):
        # 合并订单合并接口
        data = self.Print_Shipment.rpc_trade_merge_api_merge(trade_id, action, address_id).json()
        assert data == {'code': 0, 'status': 200, 'msg': '合并成功', 'data': []}

    @pytest.mark.parametrize("trade_id", ([2057533301366657109], [""]))
    def test_rpc_trade_cancel_api(self, trade_id):
        # 取消合并订单接口
        if trade_id == 2057533301366657109:
            Cancel_merge_01 = self.Print_Shipment.rpc_trade_cancel_api(trade_id).json()
            assert Cancel_merge_01 == {'msg': '取消合并成功', 'status': 200}

    def test_rpc_logistics_getLogistics_api(self):
        # 获取此账号所有的发货渠道接口
        status = self.Print_Shipment.rpc_logistics_getLogistics_api().json()['status']
        sub_code = self.Print_Shipment.rpc_logistics_getLogistics_api().json()["sub_code"]
        msg = self.Print_Shipment.rpc_logistics_getLogistics_api().json()['msg']
        data = self.Print_Shipment.rpc_logistics_getLogistics_api().json()['data']['logistics_company'][0:1]
        assert status == 200 and sub_code == "success" and msg == "请求成功" and data == [{"id": "86", "alias": "速邮达个人物品"}]

    @pytest.mark.parametrize("status", ((0), (""), ("*")))
    def test_rpc_logistics_getLogisticsConfigure_api(self, status):
        # 获取所有快递公司的信息
        status_01 = self.Print_Shipment.rpc_logistics_getLogisticsConfigure_api(status).json()['status']
        msg = self.Print_Shipment.rpc_logistics_getLogisticsConfigure_api(status).json()['msg']
        data = self.Print_Shipment.rpc_logistics_getLogisticsConfigure_api(status).json()['data']['express_company'][
               0:1]
        if status == 0:
            try:
                assert status_01 == 200 and msg == "success" and data == [
                    {"id": "1", "express_name": "顺丰", "express_code": "SF", "express_type": "1", "status": "1",
                     "type_string": "直营型"}]
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")
        else:
            try:
                assert status_01 == 200 and msg == "success" and data == [
                    {"id": "1", "express_name": "顺丰", "express_code": "SF", "express_type": "1", "status": "1",
                     "type_string": "直营型"}]
            except AssertionError:
                logger.exception("断言失败,测试用例不通过")
                raise
            else:
                logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize(
        "checked_express, checked_invoice, express_info_id, get_invoice_type,printer_express, printer_invoice, trade_id, type",
        yaml.safe_load(open(r"G:\order_huijiedan\yaml_data\rpc_order_sub_orderSend_data.yaml", "r", encoding="utf-8")))
    def test_rpc_order_sub_orderSend_api_01(self, checked_express, checked_invoice, express_info_id, get_invoice_type,
                                            printer_express, printer_invoice, trade_id, type):
        # 单个订单取号接口&&取号并发货接口
        Take_number = self.Print_Shipment.rpc_order_sub_orderSend_api_01(checked_express, checked_invoice,
                                                                         express_info_id,
                                                                         get_invoice_type,
                                                                         printer_express, printer_invoice, trade_id,
                                                                         type).json()
        try:
            assert Take_number != {'status': 201, 'sub_code': 'error', 'msg': '选中的子订单中有已取号订单，请重新选择！',
                                   'file': '/usr/share/nginx/html/application/common/lib/TradeOrder.php', 'line': 1085}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("oid", ((2051226102209657109), (2057529665609657109), (2049760540535657109)))
    def test_rpc_order_sub_cancelInvoice_api(self, oid):
        # 作废运单号接口
        Void_waybill = self.Print_Shipment.rpc_order_sub_cancelInvoice_api(oid).json()
        try:
            assert Void_waybill == {'sub_code': 'success', 'msg': '取消成功', 'status': 200, 'code': 0} \
                   or Void_waybill == {'code': 0, 'msg': '未取号', 'status': 201, 'sub_code': 'error'}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_trade_supply_api(self):
        # 补单接口
        Supplement_es_msg = self.Print_Shipment.rpc_trade_supply_api().json()["es_msg"]
        Supplement_msg = self.Print_Shipment.rpc_trade_supply_api().json()["msg"]
        try:
            assert Supplement_es_msg == 'elastic 数据同步成功' and Supplement_msg != '下单失败错误码:余额不足,请充值!'
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_order_sub_orderSend_api(self):
        # 发货接口
        deliver_goods = self.Print_Shipment.rpc_order_sub_orderSend_api().json()
        try:
            assert deliver_goods == {'status': 201, 'sub_code': 'error', 'msg': '选中的子订单中有已取号订单，请重新选择！',
                                     'file': '/usr/share/nginx/html/application/common/lib/TradeOrder.php',
                                     'line': 1085} or deliver_goods != {'status': 201, 'sub_code': 'error',
                                                                        'msg': '选中的子订单中有已取号订单，请重新选择！',
                                                                        'file': '/usr/share/nginx/html/application/common/lib/TradeOrder.php',
                                                                        'line': 1085}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("trade_id,oids,trade_id1,oids1", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\rpc_order_sub_get_InvoiceJudge_data.yaml", "r", encoding="utf-8")))
    def test_rpc_order_sub_getInvoiceJudge_api(self, trade_id, oids, trade_id1, oids1):
        # 批量取号验证接口
        verification = self.Print_Shipment.rpc_order_sub_getInvoiceJudge_api(trade_id, oids, trade_id1, oids1).json()
        try:
            assert verification == {'code': 0, 'sub_code': 'error', 'msg': '选择的宝贝非待发货状态，请重新选择'} or verification == \
                   {'code': 0, 'msg': '提交获取运单号的请求', 'status': 200, 'sub_code': 'success'}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("trade_id,oids,get_invoice_type,trade_id1,oids1", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\rpc_order_sub_getInvoice_api_data.yaml", "r", encoding="utf-8")))
    def test_rpc_order_sub_getInvoiceJudge_api(self, trade_id, oids, get_invoice_type, trade_id1, oids1):
        # 批量取号接口
        batch_number_retrieval = self.Print_Shipment.rpc_order_sub_getInvoice_api(trade_id, oids, get_invoice_type,
                                                                                  trade_id1,
                                                                                  oids1).json()
        try:
            assert batch_number_retrieval == {'code': 0, 'sub_code': 'error',
                                              'msg': '该宝贝已取号，请勿再次取号'} or batch_number_retrieval == \
                   {'code': 0, 'msg': '提交获取运单号的请求', 'status': 200, 'sub_code': 'success'} or \
                   batch_number_retrieval == {'code': 0, 'msg': '选择的宝贝非待发货状态，请重新选择', 'sub_code': 'error'}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_Prints_setPrinter_url(self):
        # 设置默认打印机接口
        set_default = self.Print_Shipment.rpc_Prints_setPrinter_url().json()
        try:
            assert set_default == {"code": 0, "msg": "更新成功", "sub_code": "success", "status": 200}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_configure_getConfigInitData_url(self):
        # 设置默认发货单模板————获取数据的两个接口(##第一个接口)
        data = self.Print_Shipment.rpc_configure_getConfigInitData_api().json()["data"]["20"]["value"]['data'][0][
            "name"]
        data1 = self.Print_Shipment.rpc_configure_getConfigInitData_api().json()["data"]["20"]["name"]
        try:
            assert data1 == '发货单模板' and data == 'A5发货单模板'
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_Template_list_api(self):
        # 设置默认发货单模板————获取数据的两个接口(##第二个接口)
        data = self.Print_Shipment.rpc_Template_list_api().json()["data"]['list'][0]["template_name"]
        try:
            assert data == "预发布测试1"
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_configure_setConfig_api_01(self):
        # 设置默认发货单接口
        request_data = self.Print_Shipment.rpc_configure_setConfig_api_01().json()
        # 调用设置默认发货单接口的请求，并将请求成功的数据转换为json格式
        try:
            assert request_data == {'code': 0, 'status': 200, 'sub_code': 'success', 'msg': '修改配置成功'}
        # assert判断比对接口返回的数据和预期数据
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("trade_id,oids,get_invoice_type,trade_id1,oids1", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\Batch_shipment.yaml", "r", encoding="utf-8")))
    def test_Batch_shipment(self, trade_id, oids, get_invoice_type, trade_id1, oids1):
        # 测试批量发货
        data = self.Print_Shipment.rpc_order_sub_getInvoice_Batch_shipment \
            (trade_id, oids, get_invoice_type, trade_id1, oids1).json()  # 使用换行符\换行
        # 下方这个判断数据有2种可能，trade_id和oids可以再yaml文件更换，第一种订单未发货就会发货成功，第二种已发货接口会提示订单已取号
        # 所以用了or（或）来判断
        try:
            assert data == {"code": 0, "sub_code": "success", "msg": "提交获取运单号的请求", "status": 200} or data == \
                   {'code': 0, 'sub_code': 'error', 'msg': '该宝贝已取号，请勿再次取号'}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")


#####################################################################################自由订单接口自动化测试##################################################################################
class Test_Free_Order():
    Free_Order = Free_Order()

    def setup_method(self):
        logger.info('==> 开始执行测试用例======================')

    def teardown_method(self):
        logger.info("==> 测试用例执行结束======================")

    def setup_class(self):
        print("自由订单功能接口测试开始时间：",
              time.strftime("\n%Y-%m-%d %H:%M:%S", time.localtime()))  # 获取系统的当前时间，方法：setup_class会在测试开始前执行一次
        logger.fatal("自由订单开始时间:{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))  # 在日志中写入开始时间

    def teardown_class(self):
        print("自由订单功能接口测试结束时间：",
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 获取当前系统的时间，方法：teardown_class会在测试结束后执行一次
        logger.fatal("自由订单结束时间:{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))  # 在日志中写入结束时间

    @pytest.mark.parametrize("type, province, city, district, address, name, mobile", yaml.safe_load(
        open(r"G:\order_huijiedan\yaml_data\free_order_address_data.yaml", "r",
             encoding="utf-8")))  # 将yaml文件中存放的3组数据循环读取，每读出一组数据，便用这组数据请求一次接口
    def test_rpc_free_address_addAddress_api(self, type, province, city, district, address, name, mobile):
        # 自由订单新增寄件地址接口
        code = self.Free_Order.rpc_free_address_addAddress_api(type, province, city, district, address, name, mobile)[
            'code']  # 提取code，用做判断接口是否请求成功
        msg = self.Free_Order.rpc_free_address_addAddress_api(type, province, city, district, address, name, mobile)[
            'msg']  # 提取msg，用做判断接口是否请求成功
        status = self.Free_Order.rpc_free_address_addAddress_api(type, province, city, district, address, name, mobile)[
            'status']  # 提取status，用做判断接口是否请求成功
        logger.info(
            "自由订单新增寄件地址请求数据为:type:{},province:{},city:{},district:{}, address:{}, name:{}, mobile:{}".format(type,
                                                                                                             province,
                                                                                                             city,
                                                                                                             district,
                                                                                                             address,
                                                                                                             name,
                                                                                                             mobile))
        try:
            assert code == 0 and msg == '新增成功' and status == 200  # 判断接口的响应结果和预期结果是否符合
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_free_order_saveOrder_api(self):
        # 创建订单接口
        data = self.Free_Order.rpc_free_order_saveOrder_api().json()
        try:
            assert data == {"msg": "订单创建成功", "status": 200, "data": [], "code": 0}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功，用例通过！")

    def test_Free_order_lists_api(self):
        # 获取自由订单列表的数据
        trade_id = self.Free_Order.Free_order_lists_api()
        try:
            assert trade_id != ""
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功，用例通过！")

    logger.info("第一次请求的数据为底单查询的,第二次为打单列表的,第三次为自由订单的,第四次的请求参数为空字符串")

    @pytest.mark.parametrize("invoice_no", ((163584376777576), (163608311177236), (163584365077733), ("")))
    def test_logistics_information_api(self, invoice_no):
        # 获取订单物流信息接口
        logger.info("获取订单物流信息接口的请求数据为{}".format(invoice_no))
        try:
            case1 = \
                self.Free_Order.logistics_information_api(invoice_no).json()["data"]["trace_list"]["transit_step_info"][
                    0][
                    "status_desc"]
            case2 = self.Free_Order.logistics_information_api(invoice_no).json()
            assert case1 == "商品已经下单" or case2 == {"code": 0, "status": 201, "sub_code": "error", "msg": "暂无物流信息"}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        except KeyError:
            logger.exception("响应信息索引获取信息失败,由于上面用的是or逻辑运算,所以此地方报错属于正常")
            raise
        else:
            logger.info("断言成功，用例通过！")

    def test_rpc_product_combo_getSkuList_api(self):
        # 选择淘宝商品接口
        datas = self.Free_Order.rpc_product_combo_getSkuList_api().json()["data"]["data"][0]["num_iid"]
        try:
            assert datas == "573934164201"
        except AssertionError and KeyError:
            if AssertionError:
                logger.exception("断言失败,测试用例不通过!")
                raise
            elif KeyError:
                logger.error("可能由于线上环境的数据改变,导致出现通过索引获取数据时异常")
                raise
        else:
            logger.info("断言成功，用例通过！")

    def test_free_order_No_api(self):
        # 自由订单取号验证接口
        datas = self.Free_Order.free_order_No_api().json()
        try:
            assert datas == {"code": 0, "sub_code": "pass", "msg": "通过", "status": 200}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功，用例通过！")

    def test_rpc_order_sub_orderSend_api(self):
        # 自由订单取号接口
        datas = self.Free_Order.rpc_order_sub_orderSend_api().json()['msg']
        data = self.Free_Order.rpc_order_sub_orderSend_api().json()["msg"]
        data_sp = data.split(",", 1)

        try:
            assert datas == '选中的子订单中有已取号订单，请重新选择！' or data_sp == "取号成功"

        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            logger.info("由于此条测试用例使用or(或)逻辑运算判断,所以将此信息写入日志")
            raise
        else:
            logger.info("断言成功，用例通过！")

    def test_order_sub_orderSend_api(self):
        # 自由订单取号发货接口
        data = self.Free_Order.order_sub_orderSend_api().json()["msg"]
        data_sp = data[0:4]
        try:
            assert data_sp == "取号成功" or data_sp == '勾选的订'
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")


class Test_Commodity_Management:
    Commodity_Management = Commodity_Management()

    def test_rpc_product_lists_api(self):
        # 商品列表请求数据模块测试
        data = self.Commodity_Management.rpc_product_lists_api().json()["data"][1]["title"]
        try:
            assert data == "测试商品4不对外出售" or data != ""

        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_product_search_api(self):
        # 测试搜索商品接口
        data = self.Commodity_Management.product_search_api()['data']  # 调用方法,发送请求
        try:
            assert data == {}
            # 这里的判断主要是引入了yaml文件,提前将预期结果写入yaml文件
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_sku_lists_api(self):
        # 测试单个商品获取sku列表详情数据
        data = self.Commodity_Management.rpc_sku_lists_api().json()["data"][0]
        try:
            assert data == response_data.rpc_sku_lists_api_response
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_product_combo_list_api(self):
        # 102371790557
        # 单个商品sku绑定组合的详情列表接口
        data = self.Commodity_Management.rpc_product_combo_list_api().json()["data"][0]
        try:
            assert data == response_data.rpc_product_combo_list_api_response
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_sku_matchCombo_api(self):
        # 商品绑定套盒接口
        data = self.Commodity_Management.rpc_sku_matchCombo_api().json()['msg']
        try:
            assert data == "绑定成功"
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_sku_cancelMatchCombo_api(self):
        # 解除商品已经绑定的套盒接口
        data = self.Commodity_Management.rpc_sku_cancelMatchCombo_api().json()["msg"]
        try:
            assert data == "解绑成功"
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_product_setcate_api(self):
        # 设置商品的对账主体接口
        data = self.Commodity_Management.rpc_product_setcate_api().json()
        try:
            assert data == {"status": 200, "sub_code": "error", "code": 0, "msg": "操作成功", "statusCode": 200}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_product_updateCache_api(self):
        # 商品列表中更新缓存接口
        data = self.Commodity_Management.rpc_product_updateCache_api().json()
        try:
            assert data == {"code": 0, "sub_code": "success", "msg": "更新缓存成功", "status": 200}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_task_LoadProduct_api(self):
        # 商品列表中同步商品接口
        name = self.Commodity_Management.rpc_task_LoadProduct_api().json()["task"]["suc"]["LoadProduct"]["data"]["name"]
        data_keyerror = self.Commodity_Management.rpc_task_LoadProduct_api().json()
        # 此数据为接口相应数据的索引取值==>'wangweilon:cb -> 加载商品数据'
        # 注意此接口2分钟只能使用一次
        try:
            assert name == 'wangweilon:cb -> 加载商品数据'
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        except KeyError:
            assert data_keyerror == {"code": 0, "msg": "请于 <strong class=\"new-red\">1分钟59秒<\/strong> 以后在执行此操作 ",
                                     "status": 200, "sub_code": "error"}
            logger.exception("如果这句话执行了, 就是接口在2分钟内执行了2次就会写入日志,因为做了分支判断")

        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_Product_addShopProduct_api(self):
        # 新增商品接口
        data = self.Commodity_Management.rpc_Product_addShopProduct_api().json()
        try:
            assert data == {"code": 0, "sub_code": "success", "msg": "新增商品成功", "status": 200}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_Product_extractShopProduct_api(self):
        # 提取商品接口
        data = self.Commodity_Management.rpc_Product_extractShopProduct_api().json()
        try:
            assert data == response_data.Withdraw_goods_response
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_rpc_Product_addExtractShopProduct_api(self):
        # 保存提取到的商品接口
        data = self.Commodity_Management.rpc_Product_addExtractShopProduct_api().json()
        try:
            assert data == {"code": 0, "sub_code": "error", "msg": "添加商品成功", "status": 200}
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    def test_portfolio_goods_api(self):
        data = self.Commodity_Management.portfolio_goods_api().json()["data"][0]["title"]
        try:
            assert data == '测试套装005'
        except AssertionError:
            logger.exception("断言失败,测试用例不通过")
            raise
        else:
            logger.info("断言成功,用例通过!")

    # pytest.mark.parametrize则是循环将数据发送到接口
    @pytest.mark.parametrize("data", yaml.safe_load(
        open(r"G:\order_huijiedan\data\rpc_category_status_api.yaml", "r", encoding="utf-8")))
    def test_rpc_category_status_api(self, data):
        # 对账主体中的对账分类是否启用
        rep = self.Commodity_Management.rpc_category_status_api(data[0])  # 调用函数

        try:
            assert rep == {"code": 0, "msg": "设置成功", "status": 200}  # 判断接口响应数据是否符合预期不符合预期则会捕获异常

        except AssertionError:
            logger.exception("断言失败,测试用例不通过,==>此数据为True则是启用/显示, 为False则是禁用,不通过的请求数据为:{}".format(data))
            # 捕获到异常则会写入到日志文件
            raise  # 抛出异常   然后继续执行下个测试用例
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("data", yaml.safe_load(
        open(r"G:\order_huijiedan\data\rpc_category_status_api.yaml", "r", encoding="utf-8")))
    def test_rpc_Category_lock_api(self, data):
        # 对账主体的对账分类是否锁定
        rep = self.Commodity_Management.rpc_Category_lock_api(data[0])
        try:
            assert rep == {"code": 0, "msg": "设置成功", "status": 200}  # 判断接口响应数据是否符合预期不符合预期则会捕获异常

        except AssertionError:
            logger.exception("断言失败,测试用例不通过,==>此数据为True则是启用/显示, 为False则是禁用,不通过的请求数据为:{}".format(data))
            # 捕获到异常则会写入到日志文件
            raise  # 抛出异常   然后继续执行下个测试用例
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("data", requ_data.classified_data)
    def test_rpc_Category_createUpdateCategory_api(self, data):
        # 测试对账分类修改数据
        print(data)
        rep = self.Commodity_Management.rpc_Category_createUpdateCategory_api(data)
        print(data)
        try:
            assert rep == {"status": 200, "msg": "success"}  # 判断接口响应数据是否符合预期不符合预期则会捕获异常

        except AssertionError:
            logger.exception("断言失败,测试用例不通过,==>此数据为True则是启用/显示, 为False则是禁用,不通过的请求数据为:{}".format(data))
            # 捕获到异常则会写入到日志文件
            raise  # 抛出异常   然后继续执行下个测试用例
        else:
            logger.info("断言成功,用例通过!")

    @pytest.mark.parametrize("data", requ_data.test_rpc_product_lists_api_1_data, ids=["商品简称列表获取列表数据", "商品列表组合查询"])
    def test_rpc_product_lists_api_1(self, data):
        # 商品简称列表获取数据和组合查询
        rep = self.Commodity_Management.rpc_product_lists_api_1(data)["Params"]["permissionData"]["UserData"][
            "taobao_user_nick"]
        try:
            assert rep == response_data.taobao_user_nick
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_sku_updateSku_api_data, ids=["修改单个商品的Sku简称"])
    def test_rpc_sku_updateSku_api(self, data):
        # 修改单个商品的sku简称
        print(data)
        rep = self.Commodity_Management.rpc_sku_updateSku_api(data)
        try:
            assert rep == response_data.test_rpc_sku_updateSku_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_import_order_importOrderFile_api_data, ids=["导入查看:前端已处理好的数据"])
    def test_rpc_import_order_importOrderFile_api(self, data):
        # 导入查看上传文件接口&&&这里是前端处理好的数据发送给后端,所以只能通过接口传入处理好的数据流
        rep = self.Commodity_Management.rpc_import_order_importOrderFile_api(data)
        try:
            assert rep == response_data.test_rpc_import_order_importOrderFile_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_import_order_list_api_data,
                             ids=["导入查看列表数据", "导入查看==>组合查询:名称+商品编码"])
    def test_rpc_import_order_list_api(self, data):
        # 导入查看搜索数据&&导入查看获取数据接口
        rep = self.Commodity_Management.rpc_import_order_list_api(data)["msg"]
        rep1 = self.Commodity_Management.rpc_import_order_list_api(data)["data"]
        try:
            assert rep == "请求成功" and rep1 != []
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_import_order_deleteImportOrder_api_data, ids=["导入查看==>删除已导入数据"])
    def test_rpc_import_order_deleteImportOrder_api(self, data):
        # 导入查看==>删除已导入数据
        rep = self.Commodity_Management.rpc_import_order_deleteImportOrder_api(data)
        try:
            assert rep == response_data.test_rpc_import_order_deleteImportOrder_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_order_sub_originalQuery_api_data, ids=["底单查询==>详细记录列表"])
    def test_rpc_order_sub_originalQuery_api(self, data):
        # 底单查询==>详细记录--->获取数据接口
        rep = int(self.Commodity_Management.rpc_order_sub_originalQuery_api(data)["data"][0]["exp_order_id"])
        msg = self.Commodity_Management.rpc_order_sub_originalQuery_api(data)["msg"]
        try:
            assert rep == int(response_data.test_rpc_order_sub_originalQuery_api_data) and msg == "数据加载成功"
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_order_sub_originalSummaryQuery_api_data, ids=["底单查询==>汇总报表列表"])
    def test_rpc_order_sub_originalSummaryQuery_api(self, data):
        # 底单查询==>汇总报表-->获取数据接口
        rep = self.Commodity_Management.rpc_order_sub_originalSummaryQuery_api(data)
        try:
            assert rep == response_data.test_rpc_order_sub_originalSummaryQuery_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_order_sub_scan_api_data, ids=["扫描发货==>扫描运单号获取数据"])
    def test_rpc_order_sub_scan_api(self, data):
        # 扫描发货==>扫描过后获取数据的接口
        resp = self.Commodity_Management.rpc_order_sub_scan_api(data)
        try:
            assert resp == response_data.test_rpc_order_sub_scan_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    ids = ['漏单检测第1次', "漏单检测第2次", "漏单检测第3次", "漏单检测第4次", '漏单检测第5次', '漏单检测第6次', '漏单检测第7次',
           '漏单检测第8次', '漏单检测第9次', '漏单检测第10次', '漏单检测第11次', '漏单检测第12次', '漏单检测第13次', '漏单检测第14次',
           '漏单检测第15次', '漏单检测第16次', '漏单检测第17次', '漏单检测第18次', '漏单检测第19次', '漏单检测第20次', '漏单检测第21次',
           '漏单检测第22次', '漏单检测第23次', '漏单检测第24次', '漏单检测第25次', '漏单检测第26次', '漏单检测第27次', '漏单检测第28次',
           '漏单检测第29次', '漏单检测第30次']

    @pytest.mark.parametrize("data", yaml.safe_load(
        open(r"G:/order_huijiedan/yaml_data/ Missing_Order_Detection.yaml", "r", encoding="utf-8")), ids=ids)
    def test_rpc_Order_Sub_leakageOrderCheck_api(self, data):
        # 漏单检测
        resp = self.Commodity_Management.rpc_Order_Sub_leakageOrderCheck_api(data[0])
        msg = self.Commodity_Management.rpc_Order_Sub_leakageOrderCheck_api(data[0])["msg"]
        # jsonpath用法
        # msg=jsonpath.jsonpath(self.Commodity_Management.rpc_Order_Sub_leakageOrderCheck_api(data[0]),"$.msg")

        try:
            assert resp == response_data.test_rpc_Order_Sub_leakageOrderCheck_api_data or msg == '无漏单'
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_task_delete_api_data, ids=["财务管理==>支付宝==>删除"])
    def test_rpc_task_delete_api(self, data):
        # 支付宝删除已上传的数据
        try:
            assert (jsonpath(self.Commodity_Management.rpc_task_delete_api(data), "msg")[0]) == '删除成功'
            # 使用jsonpath模块提取接口返回的msg字段用作数据校验
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    @pytest.mark.parametrize("data", requ_data.test_rpc_task_bill_api_data, ids=["账单中心==>重新分析", "账单中心==>账单导出任务提交"])
    def test_rpc_task_bill_api(self, data):
        # 账单中心的重新提交请求&&提交账单导出任务请求
        try:
            assert (jsonpath(self.Commodity_Management.rpc_task_bill_api(data), "msg")[0]) == \
                   response_data.test_rpc_task_bill_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")
            time.sleep(6)

    @pytest.mark.parametrize("data", requ_data.test_rpc_bill_lists_api_data, ids=["列表组合查询", "列表默认请求数据"])
    def test_rpc_bill_lists_api(self, data):
        # 账单中心==>获取默认数据&&组合查询
        try:
            assert (jsonpath(self.Commodity_Management.rpc_bill_lists_api(data), "msg")[
                0]) == response_data.test_rpc_bill_lists_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")


class Test_Order_Management:
    # 订单管理模块
    order_management = Order_Management()

    ids = ["待发货列表", "待付款列表", "部分发货列表", "已发货列表", "退款中列表", "交易成功列表", "交易关闭列表", "近三个月订单列表"]

    @pytest.mark.parametrize("data", requ_data.test_order_sub_lists_url_data, ids=ids)
    def test_order_sub_lists_api(self, data):
        # 待发货列表
        try:
            assert (jsonpath(self.order_management.order_list(data), "msg")[
                0]) == response_data.test_rpc_bill_lists_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    ids = ["所有退款列表", "待处理退款列表", "等待退款列表", "退货待确认列表", "拒绝退款列表", "退款成功列表", "退款关闭列表", "退款订单==>【商品名称+订单编号】组合查询"]

    @pytest.mark.parametrize("data", requ_data.test_rpc_refund_lists_api_data, ids=ids)
    def test_rpc_refund_lists_api(self, data):
        # 退款订单列表查询
        try:
            assert (jsonpath(self.order_management.rpc_refund_lists_api(data), "msg")[
                0]) == response_data.test_rpc_bill_lists_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")


class Test_Multi_Store_Operation:
    Multistoreoperation = Multi_Store_Operation()

    @pytest.mark.parametrize("data", requ_data.test_rpc_Shop_switch_setSwitchShop_api_data,
                             ids=["切换为主店铺的订单", "切换为主店铺店铺增加t_0277店铺", "切换店铺未选择店铺", "切换店铺全选店铺:3个店铺"])
    def test_rpc_Shop_switch_setSwitchShop_api(self, data):
        # 切换店铺
        try:
            assert (jsonpath(self.Multistoreoperation.rpc_Shop_switch_setSwitchShop_api(data), "status")[0]) == \
                   response_data.test_rpc_Shop_switch_setSwitchShop_api_data[0][0]
            assert (jsonpath(self.Multistoreoperation.rpc_Shop_switch_setSwitchShop_api(data), "sub_code")[0]) == \
                   response_data.test_rpc_Shop_switch_setSwitchShop_api_data[0][1]
            assert (jsonpath(self.Multistoreoperation.rpc_Shop_switch_setSwitchShop_api(data), "msg")[0]) == \
                   response_data.test_rpc_Shop_switch_setSwitchShop_api_data[0][2]
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    def test_rpc_Shop_getSwitchCode_api(self):
        # 获取关联店铺的数据
        try:
            assert (jsonpath(self.Multistoreoperation.rpc_Shop_getSwitchCode_api(), "msg")[0]) == \
                   response_data.test_rpc_Shop_getSwitchCode_api_data[0][0]
            assert (jsonpath(self.Multistoreoperation.rpc_Shop_getSwitchCode_api(), "data")[0]) != \
                   response_data.test_rpc_Shop_getSwitchCode_api_data[0][1]
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!")
            raise
        else:
            logger.info("断言成功,测试用例通过")

    def test_rpc_Shop_createSwitchCode_api(self):
        # 更新店铺的店铺代码
        try:
            assert (jsonpath(self.Multistoreoperation.rpc_Shop_createSwitchCode_api(), "msg")[
                0]) == response_data.test_rpc_Shop_createSwitchCode_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!!")
            raise
        else:
            logger.info("断言成功,测试用例通过!!")

    @pytest.mark.parametrize("data", requ_data.test_rpc_Shop_setNick_api_data, ids=["修改主店铺的店铺简称"])
    def test_rpc_Shop_setNick_api(self, data):
        # 修改主店铺的店铺简称
        try:
            assert self.Multistoreoperation.rpc_Shop_setNick_api(
                data[0]) == response_data.test_rpc_Shop_setNick_api_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!!")
            raise
        else:
            logger.info("断言成功,测试用例通过!!")

    @pytest.mark.parametrize("data", requ_data.test_rpc_Shop_switch_editShopNick_api_data, ids=["修改子店铺的店铺简称"])
    def test_rpc_Shop_switch_editShopNick_api(self, data):
        # 修改子店铺的店铺简称
        rep = self.Multistoreoperation.rpc_Shop_switch_editShopNick_api(data[0])
        Assert_Encapsulation(lnterface=rep, response=response_data.test_rpc_Shop_switch_editShopNick_api_data[0],
                             or_lnterface=rep,
                             or_response=response_data.test_rpc_Shop_switch_editShopNick_api_data[0][1]
                             )

    @pytest.mark.parametrize("data", requ_data.test_rpc_Shop_switch_deleteShopSwitch_api_data, ids=["解除子店铺"])
    def test_rpc_Shop_switch_deleteShopSwitch_api(self, data):
        # 解除子店铺的绑定/关联
        Assert_Encapsulation(lnterface=(self.Multistoreoperation.rpc_Shop_switch_deleteShopSwitch_api(data[0])),
                             response=response_data.test_rpc_Shop_switch_deleteShopSwitch_api_data)

    @pytest.mark.parametrize("data", requ_data.test_rpc_Shop_switch_addShopSwitch_api_data, ids=["绑定蔡博店铺"])
    def test_rpc_Shop_switch_addShopSwitch_api(self, data):
        # 绑定店铺
        Assert_Encapsulation(
            lnterface=(jsonpath(self.Multistoreoperation.rpc_Shop_switch_addShopSwitch_api(data[0]), "$..msg")[0]),
            response=response_data.test_rpc_Shop_switch_addShopSwitch_api_data,
            or_lnterface=self.Multistoreoperation.rpc_Shop_switch_addShopSwitch_api(data[0]),
            or_response={'status': 201, 'sub_code': 'error', 'msg': '该店铺已与其他店铺绑定'}
        )

# if __name__ == '__main__':
# pytest.main(["test_order_huijiedan.py"])
# pytest.main('-s','-v')
# pytest.main({'-s', '-v', '--html=order_huijiedan/report/report.html'})
# 日志级别(Level)：DEBUG、INFO、WARNING、ERROR、CRITICAL(FATAL)
# 启动按钮
