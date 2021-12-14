import requests
import time

from Tool.order_huijiedan_Tool import Tools
from Log.my_log import logger

headers = {"Content-Type":"application/vnd.ms-excel","hjdtoken": Tools.token}

class a:
    def file_upload(self,url,name,filename,file_path):
        files = {'file': (name,filename,open(file_path, 'rb'),'text/plain')}
        try:
            requ_file = requests.post(url, files=files, headers=headers).json()
            logger.info("文件上传接口 : {},请求成功,返回数据 : {}".format(url, requ_file))
            return requ_file
        except Exception as e:
            logger.error("文件上传接口 : {}, 请求失败,原因是: {}".format(url, e))


if __name__ == '__main__':
    a=a()
    a.file_upload("https://order.huijiedan.cn/public/index.php?s=rpc/free_order/importOrder","import_free_order","trade-free-order-v20.xls","D:\\工作模板\\alipay.xlsx")
