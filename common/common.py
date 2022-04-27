import json

from config.config import djencrypt


def gen_params(func_id: str, body: dict) -> dict:
    """
    生成请求参数
    :param func_id: 功能id
    :param body: 请求体
    :return:
    """
    djencrypt["body"] = json.dumps(body)
    djencrypt["functionId"] = func_id
    return djencrypt
