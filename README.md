
#### 使用

`python install -r requirements.txt`

#### Cookie
请在小程序 **_京东到家_** 抓取登录后的Cookie


#### 测试用例
如有其它小程序逆向 联系V:Code-Bin
```
cookie = 你抓取的cookie
match_sid = re.search(r'o2o_m_h5_sid=([\w-]+)', cookie).group(1)
match_device_id = re.search(r'deviceid_pdj_jd=([\w-]+)', cookie).group(1)
headers['Cookie'] = cookie
headers['sid'] = match_sid
djencrypt["deviceToken"] = match_device_id
djencrypt["deviceId"] = match_device_id
djencrypt["traceId"] = f'{match_device_id}{int(time.time() * 1000)}'
# 测试方法 自行修改
print(get_my_order()) #获取订单列表
```

#### 注意

**部分代码并没有完成，但已有测试参数，请自行修改**

## 声明

#### 本项目仅供技术研究，请勿用于任何商业用途，请勿用于非法用途，如有任何人凭此做何非法事情，均于作者无关，特此声明。