import json
from urllib import parse

import requests

from config.config import iv, key, headers, main_url
from util.util import aes_encrypt


def req_get(func_id: str, params: dict) -> str:
    djencrypt_sign = parse.quote(aes_encrypt(iv, key, str(params)))
    url = f'{main_url}?functionId={func_id}&djencrypt={djencrypt_sign}'
    return requests.get(url, headers=headers).text


def req_post(func_id: str, params: dict) -> str:
    djencrypt_sign = parse.quote(aes_encrypt(iv, key, str(params)))
    url = f'{main_url}?functionId={func_id}&djencrypt={djencrypt_sign}'
    return requests.post(url, headers=headers).text
