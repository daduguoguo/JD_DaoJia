import json

from common.common import gen_params
from common.function import NEARBY_STORE_FUNC_ID
from util.request_util import req_get


def get_nearby_store(city: str, address: str, area_code: int, longitude: float, latitude: float, page: int = 1,
                     size: int = 10) -> dict:
    body = {
        "refPageSource": "activityDetail",
        "city": city,
        "areaCode": area_code,
        "longitude": longitude,
        "latitude": latitude,
        "coordType": "2",
        "address": address,
        "channelId": "",
        "channelBusiness": "",
        "currentPage": page,
        "pageSize": size,
        "rankType": 0,
        "lastStoreId": "",
        "filterTagIds": "",
        "slideStoreList": False,
        "venderIndustryType": [],
        "sortType": "",
        "level": [],
        "activityId": "",
        "pageSource": "channelStorePage",
        "ref": "",
        "ctp": "moreStoreList"
    }
    res = req_get(NEARBY_STORE_FUNC_ID, gen_params(NEARBY_STORE_FUNC_ID, body))
    return json.loads(res)
