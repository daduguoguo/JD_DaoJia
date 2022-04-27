import base64
import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def md5(sign_str: str) -> str:
    h = hashlib.md5()
    h.update(sign_str.encode("utf8"))
    sign = h.hexdigest()
    return sign


def aes_decrypt(iv: str, key: str, sign_str: str) -> str:
    sign_str = sign_str.encode('utf8')
    encode_bytes = base64.decodebytes(sign_str)
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
    text_decrypted = cipher.decrypt(encode_bytes)
    text_decrypted = unpad(text_decrypted)
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted


def aes_encrypt(iv: str, key: str, sign_str: str) -> str:
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf8'))
    pad_pkcs7 = pad(sign_str.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypt_aes = aes.encrypt(pad_pkcs7)
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    encrypted_text_str = encrypted_text.replace("\n", "")
    return encrypted_text_str
