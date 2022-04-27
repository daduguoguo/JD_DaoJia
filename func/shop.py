import json

from common.common import gen_params
from common.function import SHOP_CHANGE_ITEM_NUM
from util.request_util import req_get


def change_item_num():
    """
    修改购物车数量ID === 添加商品
    :return:
    """
    body = {
        "fromSource": 5,
        "chgNumReturnType": 0,
        "positionType": "2",
        "storeId": "11933426",
        "orgCode": "349682",
        "lat": "",
        "lng": "",
        "skus": [
            {
                "id": "2033764109",
                "num": 6,
                "spuId": "",
                "purchaseLimitHotSale": False,
                "skuServiceList": []
            }
        ],
        "showedPurchaseLimitHotSalePopupVo": False,
        "couponId": "",
        "pageSource": "",
        "incrementFlag": False,
        "cartOpenFlag": True,
        "isAdd": True,
        "cartType": 10
    }
    res = req_get(SHOP_CHANGE_ITEM_NUM, gen_params(SHOP_CHANGE_ITEM_NUM, body))
    return json.loads(res)
