from common.common import gen_params
from common.function import MY_ORDER_FUNC_ID
from util.request_util import req_get


def get_my_order(page: int = 0, size: int = 10) -> str:
    body = {
        "startIndex": page,
        "dataSize": size
    }
    return req_get(MY_ORDER_FUNC_ID, gen_params(MY_ORDER_FUNC_ID, body))
