#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-11-13 15:51:44
# @Author  : Zhen-chuan (ding_zhenchuan@163.com)
# @Link    : https://github.com/Zhen-chuan
# @Version : $Id$

#!/usr/bin/env python
# coding=utf-8
# Python 2.7.3
# File: GetCity.py
# 获取IP所在国家/省份/城市
import urllib2
import httplib
import json

'''
返回信息的结构
{"ret":1,"start":"54.52.163.0","end":"54.57.3.255","country":"美国","province":"新泽西州","city":"Woodbridge","district":"","isp":"联通","type":"","desc":""}
'''
def GetCity(ip, city):
	response = urllib2.urlopen('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=' + ip)
	htmlStr = response.read()
	cityInfo = htmlStr.decode("unicode-escape");	
	st = json.loads(cityInfo);
	city[0] = st["country"]
	city[1] = st["province"]
	city[2] = st["city"]

'''
# 测试代码
city = ["", "", ""]
GetCity("54.54.194.134", city)
print city
'''
