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
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class encapsulate_request:
    def __init__(self):
        # 读取文件中的token
        self.__logger = logger

    def requests_get(self, url, data=None, headers=None):  # get请求

        # 根据请求类型，调用请求方法
        try:
            resp = requests.get(url, data, headers=headers, verify=False,
                                allow_redirects=False)  # 发送请求,将接口的响应数据转换为json格式
            self.__logger.info("接口{}请求成功,返回数据为:{}".format(url, resp))  # 将外部每次传入的请求数据写入日志
            print(resp.headers)
            return resp  # 返回值
        except Exception as e:  # 捕获异常,如果捕获到就会写入日志
            self.__logger.info("接口{}请求失败,原因是:{}".format(url, e))

    def request_post(self, url, data=None, headers=None):  # post请求
        try:
            resp = requests.post(url, json=data, headers=headers).json()
            self.__logger.info("接口{}请求成功,返回数据为:{}".format(url, resp))
            return resp
        except Exception as e:
            self.__logger.info("接口{}请求失败,原因是:{}".format(url, e))


request_tools = encapsulate_request()

# if __name__ == '__main__':
# urllib3.disable_warnings()
# resp = requests.post(url, json=data, headers=headers, verify=False).json()
