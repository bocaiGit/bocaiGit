from Tool.order_huijiedan_Tool import Order_Tool, Tools
from Log.my_log import logger
from api.Custom_Encapsulation__Request import request_tools
from data.Business_flow_test_data import Bf_request_data


class Business_Flow_api:
    def __init__(self):
        self.headers = {"hjdtoken": Order_Tool().token}  # 公用的请求头:请求头里是token
        self.Host = Order_Tool().Host  # 服务器的ip或名称
        self.logger = logger
        self.Bf_request_data = Bf_request_data

    def Multi_store_order_decryption(self, data):
        # 多店铺订单的解密,每个店铺的订单进行解密
        # 并且每次运行时,都会更换订单的测试数据
        url = self.Host + Tools.rpc_order_decryptLists_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def Multi_store_order_modification_address(self, data):
        """
        多店铺订单修改的地址
        订单编号:蔡:{
                    2295009973292657109
                    2293767720485657109
                     }
                王:{2293746624497657109
                    2293747632504657109}
        t_1497093616947_0277店铺:2个订单
        wangweilon店铺:2个订单
        :return:
        """
        url = self.Host + Tools.rpc_order_sub_updateOrderAddress_url
        rep = request_tools.request_post(url, data, self.headers)
        return rep

    def Batch_number_retrieval(self, check_data=None, data=None, Query_data=None, Abandoned_data=None):
        """
        一共为四步:
                一. 批量取号前的验证
                二. 批量取号
                三. 取号后的打单列表查询
                四. 再去废除已经取号的订单,循环使用
        请求数据:
        t_1497093616947_0277店铺订单:
                2295009145406657109
                2295366770331657109
                wangweilon店铺订单:
                2293749828323657109
                2295335558786657109

        :param check_data: 取号前的验证接口的请求数据
        :param data: 取号接口的请求数据
        :param Query_data: 列表查询接口的请求数据
        :param Abandoned_data: 废弃运单接口的请求数据
        :return:
        """
        check_url = self.Host + Tools.rpc_order_sub_getInvoiceJudge_url  # 第一个查询验证接口的地址
        url = self.Host + Tools.rpc_order_sub_orderSend_url  # 取号接口的地址
        Query_validation_url = self.Host + Tools.rpc_order_sub_lists_url  # 查询列表数据验证接口的地址
        Abandoned_waybill_url = self.Host + Tools.rpc_order_sub_cancelInvoice_url  # 废弃运单接口的地址
        if check_data is not None:
            resp = request_tools.request_post(check_url, check_data, self.headers)  # 这个是取号前的验证接口
            return resp
        elif data is not None:
            rep = request_tools.request_post(url, data, self.headers)  # 这个是取号接口
            return rep
        elif Query_data is not None:
            response = request_tools.request_post(Query_validation_url, Query_data, self.headers)  # 在打单列表进行订单查询验证数据是否取号成功
            return response
        elif Abandoned_data is not None:
            Abandoned_waybill_resp = request_tools.request_post(Abandoned_waybill_url, Abandoned_data, self.headers)  # 废弃运单
            return Abandoned_waybill_resp
        # return [[resp], [rep], [response], [Abandoned_waybill_resp]]
