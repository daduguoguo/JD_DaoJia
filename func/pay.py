import json

from common.common import gen_params
from common.function import SUBMIT_ORDER, PAY
from util.request_util import req_get, req_post


def submit_order():
    """
    提交订单
    :return:
    """
    body = {
        "deliverType": "",
        "fromSource": 5,
        "jingBeansNum": 0,
        "source": 2,
        "orgCode": "349682",
        "storeId": "11933426",
        "cityId": 1116,
        "longitude": 117.289024,
        "latitude": 31.896015,
        "orderPayType": "first",
        "addressId": "0",
        "firstPlaceVoucherCode": "",
        "promiseDate": "",
        "usePlatPointsFlag": False,
        "useGiftCardFlag": False,
        "checkVipFlag": "",
        "purchaseVipTypeId": "",
        "redPacketCode": None,
        "firstPlaceRedPacketCode": "",
        "selectedDiscountType": None,
        "selectDiscountThreshold": None,
        "selectedDiscountMoney": None,
        "freightCouponCode": None,
        "couponCacheId": "",
        "lastAddressId": "",
        "lastDeliverType": 1,
        "lastPromiseTime": {},
        "lastDeliverFee": "",
        "marketTagParam": {},
        "userOperateType": 0,
        "deliveryClerkFeeId": None,
        "deliveryClerkFeeTipId": None,
        "orderPageId": "",
        "openState": "",
        "currentDiseasesCacheId": "",
        "memberOpenState": None,
        "grabCouponList": [],
        "educationInfo": None,
        "preSaleSkuInfos": [
            {
                "skuCount": 1,
                "skuId": "",
                "skuServiceList": [],
                "skuType": 0,
                "spuId": ""
            }
        ],
        "saleType": 1,
        "specialBusinessTagList": None,
        "packUseFlag": None
    }
    res = req_get(SUBMIT_ORDER, gen_params(SUBMIT_ORDER, body))
    return json.loads(res)


def pay():
    body = {
        "couponCacheId": "acf3d28a-aedf-4164-8c47-db9862785d3d",
        "addressId": 94342,
        "coupons": [
            "1651047027191DTqIYx1925786775-1028749576#1773411331"
        ],
        "deliveryType": "1",
        "generalAddress": 0,
        "jdBeansCount": 0,
        "deliveryTip": "立即送达",
        "orderPayType": 4,
        "storeId": "11933426",
        "signatureKey": "A5640733BA72F4894DC76FE2557F2453",
        "storeName": "华润万家-濉溪店",
        "stockOutOption": "缺货时电话与我沟通",
        "unique": "d091569e-8c91-4a2e-a778-64f279503fb4",
        "aging": 5,
        "coordType": 2,
        "fromSource": 5,
        "orderAgingType": "0",
        "terminalType": 2,
        "orgCode": "349682",
        "orderBuyerRemark": "",
        "ordererName": None,
        "ordererMobile": None,
        "specialRemark": None,
        "platformPoints": 0,
        "sendTime": "2022-04-27 17:27:00",
        "deliveryTime": "2022-04-27 18:27:00",
        "expectedDeliveryBeginTime": "2022-04-27 17:27:00",
        "expectedDeliveryTime": "2022-04-27 18:27:00",
        "arriveType": 1,
        "affectedTime": 0,
        "promiseBusinessVersion": "dj_new_promise_v3",
        "mobileSafeFlag": True,
        "useGiftCard": "0",
        "giftCardPwd": "",
        "redPackageCode": "",
        "purchaseVip": False,
        "purchaseVipTypeId": 1020520030,
        "promotionType": None,
        "freightCouponCode": "",
        "promotionMoney": None,
        "promotionRealMoney": None,
        "checkPayMoney": "¥237.8",
        "deliveryClerkFeeId": None,
        "orderBusinessTagType": 0,
        "prescriptionInfo": {},
        "educationInfo": None,
        "orderInvoiceOpenMark": 2,
        "orderInvoiceMoneyDetail": "发票金额不包含包装服务、配送费和服务费，如需开具此部分发票请联系客服解决",
        "freightInvoiceFlag": 0,
        "serviceInvoiceFlag": 0,
        "orderPageId": "734cbb48-0dad-461e-bc19-a9664b6ec157",
        "buyMerchantMemberFlag": False,
        "settlementPayMoney": 23780,
        "hasMerchantMemberFloorFlag": False,
        "hasVipFloorFlag": False,
        "userChooseFreightDiscountFlag": False,
        "userChooseCouponFlag": False,
        "submitOrderLayerType": "",
        "submitOrderLayerCheckedFlag": "",
        "saleType": 1,
        "skuList": [
            {
                "skuCount": 1,
                "skuId": "",
                "skuServiceList": [],
                "skuType": 0,
                "spuId": ""
            }
        ],
        "specialBusinessTagList": None,
        "packUseFlag": None,
        "extendInfo": "A5640733BA72F4894DC76FE2557F2453",
        "selfPickPhone": "",
        "riskTokenId": "9e564208-ea39-4947-b0e3-e44ee430267c",
        "pickerValue": None
    }
    res = req_post(PAY, gen_params(PAY, body))
    return json.loads(res)
