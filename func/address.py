import json

from common.common import gen_params
from common.function import GET_CITYS_FUNC_ID, SEARCH_ADDRESS
from util.request_util import req_get


def get_citys() -> dict:
    body = {}
    res = req_get(GET_CITYS_FUNC_ID, gen_params(GET_CITYS_FUNC_ID, body))
    return json.loads(res)


def search_address(city, district) -> dict:
    """
    搜索地址
    :param city: 市
    :param district: 区 具体地址
    :return:
    """
    body = {
        "region": city,
        "key": district
    }
    res = req_get(SEARCH_ADDRESS, gen_params(SEARCH_ADDRESS, body))
    return json.loads(res)
