iv = ""
key = ""

djencrypt = {
    "channel": "wx_xcx",
    "platform": 6,
    "platCode": "mini",
    "mpChannel": "wx_xcx",
    "appVersion": "8.18.5",
    "xcxVersion": "8.18.5",
    "appName": "paidaojia",
    # "functionId": "order/list", 功能id
    # "body": "{\"startIndex\":0,\"dataSize\":10}", 请求的数据体
    "afsImg": "",
    "lat_pos": 39.919037,
    "lng_pos": 116.39027,
    "lat": 31.25296,
    "lng": 117.29288,
    "city_id": 1116,
    "deviceToken": "a5ff6d2b-****-****-****-c61aabdd419d", #UUID字符串 Cookie中获取
    "deviceId": "a5ff6d2b-****-****-****-c61aabdd419d",  #UUID字符串 Cookie中获取
    "deviceModel": "appmodel",
    "business": "",
    "traceId": "a5ff6d2b-****-****-****-c61aabdd419d1650667784691",  # UUID + 时间戳
    "channelCode": "",
    "signNeedBody": 1,
    "signKeyV1": "04c347aebd33c15025e03e4fea053bb1262ba0f68264c414461621b2ea087cc1"  # 此参数不受影响，暂不处理
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 "
                  "Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type": "application/x-www-form-urlencoded",
    "Host": "daojia.jd.com"
}

main_url = "https://daojia.jd.com/client"
