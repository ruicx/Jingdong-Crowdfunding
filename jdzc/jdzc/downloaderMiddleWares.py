
# -*- coding: utf-8 -*-

'''
name:       downloaderMiddleWares.py
usage:      --
author:     [[
date:       2018-02-19 20:44:49
version:    1.0
Env.:       Python 3.6.4, WIN 10
'''


import random


class HttpProxyMiddleware(object):
    proxy_pool = [
        'http://171.11.138.246:30944',
        'http://120.42.124.165:26979',
        'http://222.85.50.69:42877',
        'http://180.111.227.133:39897',
        'http://180.120.201.11:44047',
        'http://113.128.26.160:30277',
        'http://117.62.113.88:42031',
        'http://121.205.74.6:47797',
        'http://115.202.245.197:27212',
        'http://123.163.21.210:40259'
    ]

    def process_request(self, request, spider):
        # request.meta['proxy'] = "http://127.0.0.1:8118"
        request.meta['proxy'] = random.choice(self.proxy_pool)
