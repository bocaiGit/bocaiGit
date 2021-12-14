"""
基于项目做定制化封装
1、鉴权:token
2、项目通用的请求头:
    {"X-Lemonban-Media-Type": "lemonban.v2"}

3、请求体格式：application/json
"""
import requests
import urllib3

from Log.my_log import logger
from Tool.order_huijiedan_Tool import Tools


class Requests_tools:
    def __init__(self):
        self.token = Tools.token  # 读取配置文中的token
        self.headers = {
            "hjdtoken": self.token
        }

    def get(self, url, data=None):
        """
        get方法请求封装
        :param url: url链接
        :param data: 请求参数
        :return: 返回请求状态码，请求响应body，请求响应时间
        """

        try:
            response = requests.get(url=url, headers=self.headers, params=data)
            logger.info("请求数据===>: {}".format(data))
            response_time = response.elapsed.total_seconds()
            response_code = response.status_code
            response_boby = response.json()
            response_msg = response_boby["msg"]
            response_data = dict()
            response_data['response_code'] = response_code  # 获取响应码
            response_data['response_time'] = response_time  # 获取响应时间
            response_data['response_body'] = response_boby  # 获取响应boby
            response_data['response_msg'] = response_msg
            return response_data

        except requests.RequestException as e:
            logger.error("请求异常：" + str(e) + "请求失败url" + url)
            raise
        except KeyError as Key:
            logger.error("KeyError:::::::此异常可能未获取到请求体{}".format((str(Key))))
            raise

    def post(self, url, data=None):
        """
        post请求封装
        :param url: 请求url
        :param data: 请求参数
        :return:
        """
        try:
            urllib3.disable_warnings()
            response = requests.post(url=url, headers=self.headers, json=data, verify=False)
            response_time = response.elapsed.total_seconds()
            response_code = response.status_code
            response_boby = response.json()
            response_data = dict()
            response_data['response_code'] = response_code
            response_data['response_time'] = response_time
            response_data['response_body'] = response_boby
            response_msg = response_boby["msg"]
            response_data['response_msg'] = response_msg
            return response_data
        except Exception as e:
            logger.error("请求异常" + str(e) + "请求失败url" + url)
            raise
        except KeyError as Key:
            logger.error("KeyError:::::::此异常可能未获取到请求体{}".format((str(Key))))
            raise


Requests_example = Requests_tools()
if __name__ == '__main__':
    requ = Requests_tools()
    resp = requ.post("https://order.huijiedan.cn/public/index.php?s=rpc/Category/status",
                     {"dataString": "{\"ids\":\"177\",\"checked\":false}"})

    print(resp)
