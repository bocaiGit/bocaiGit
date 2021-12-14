from Log.my_log import logger


def Assert_Encapsulation(lnterface=None, response=None, Interface_data=None, expect_data=None, or_lnterface=None,
                         or_response=None, code=None, msg=None, resp_code=None, resp_msg=None):
    """
    :param Interface_data: 主要用于断言接口的data字段内是否有数据
    :param expect_data:    主要用于断言接口的data字段内是否有数据
    :param lnterface:      主要用于断言接口返回的数据分动态响应
    :param response:       主要用于断言接口返回的数据分动态响应
    :return:
    """
    if lnterface is not None and response is not None and Interface_data is None and or_response is None:
        try:
            assert lnterface == response
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!!")
            raise
        else:
            logger.info("断言成功,测试用例通过!!")
    elif Interface_data is not None and expect_data is not None and lnterface is None:
        try:
            assert Interface_data != expect_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!!")
            raise
        else:
            logger.info("断言成功,测试用例通过!!")
    elif lnterface is not None and response is not None and \
            Interface_data is not None and expect_data is not None:
        try:
            assert lnterface == response and Interface_data != expect_data
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!!")
            raise
        else:
            logger.info("断言成功,测试用例通过!!")
    elif lnterface is not None and response is not None and Interface_data is None and expect_data is None and \
            or_lnterface is not None and or_response is not None:
        try:
            assert lnterface == response or or_lnterface == or_response
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!!")
            raise
        else:
            logger.info("断言成功,测试用例通过!!")
    elif lnterface is None and response is None and Interface_data is None and expect_data is None and or_lnterface is \
            None and or_response is None and code is not None and msg is not None:
        try:
            assert code == resp_code and msg == resp_msg
        except AssertionError:
            logger.exception("断言失败,测试用例不通过!!")
            raise
        else:
            logger.info("断言成功,测试用例通过!!")
            wh

if __name__ == '__main__':
    Assert_Encapsulation(code=1, resp_code=1,msg="测试打断点",resp_msg="测试打断点")
    # Assert_Encapsulation(Interface_data=[576443827542138753264532], expect_data=[])
    # Assert_Encapsulation(lnterface=1, response=1, Interface_data=[5532453453245], expect_data=[])
    # Assert_Encapsulation(lnterface=1,response=0,or_lnterface=100,or_response=100)
