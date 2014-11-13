#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-11-13 15:39:49
# @Author  : Zhen-chuan (ding_zhenchuan@163.com)
# @Link    : https://github.com/Zhen-chuan
# @Version : $Id$


import urllib2
import httplib

def GetIP():
	response = urllib2.urlopen('http://ip.dnsexit.com/index.php')
	htmlStr = response.read()
	return htmlStr

'''
# 测试代码
print GetIP()
'''