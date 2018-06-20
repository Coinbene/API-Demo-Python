# -*- coding: utf-8 -*-
from utils import *



#  获取最新价
def get_ticker(symbol):
    """
    symbol必填，为all或交易对代码:btcusdt
    """
    url = market_url + "ticker?symbol=" + str(symbol)
    return http_get_nosign(url)


#  获取挂单
def get_orderbook(symbol, depth=200):
    """
    depth为选填项，默认为200
    """
    url = market_url + "orderbook?symbol=" + symbol + "&depth=" + str(depth)
    return http_get_nosign(url)


#  获取成交记录
def get_trade(symbol, size=300):
    """
    size:获取记录数量，按照时间倒序传输。默认300
    """
    url = market_url + "trades?symbol=" + symbol + "&size=" + str(size)
    return http_get_nosign(url)


#  查询账户余额
def post_balance(dic):
    """
    以字典形式传参
    apiid:可在coinbene申请,
    secret:个人密钥(请勿透露给他人),
    timestamp:时间戳,
    account:默认为exchange，
    """
    url = trade_url + "balance"
    return http_post_sign(url, dic)


#  下单
def post_order_place(dic):
    """
    以字典形式传参
    apiid,symbol,timestamp
    type:可选 buy-limit/sell-limit
    price:购买单价
    quantity:购买数量
    """
    url = trade_url + "order/place"
    return http_post_sign(url, dic)


#  查询委托
def post_info(dic):
    """
    以字典形式传参
    apiid,timestamp,secret,orderid
    """
    url = trade_url + "order/info"
    return http_post_sign(url, dic)


#  查询当前委托
def post_open_orders(dic):
    """
    以字典形式传参
    apiid,timestamp,secret,symbol
    """
    url = trade_url + "order/open-orders"
    return http_post_sign(url, dic)


#  撤单
def post_cancel(dic):
    """
    以字典形式传参
    apiid,timestamp,secret,orderid
    """
    url = trade_url + "order/cancel"
    return http_post_sign(url, dic)
