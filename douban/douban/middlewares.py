#coding:utf-8
import random
import base64
from settings import PROXIES
from settings import USER_AGENTS

class RandomUserAgent(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', user_agent)
        print user_agent

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)

        if proxy['user_password'] is None:
            request.meta['proxy'] = 'http://' + proxy['ip_port']
        else:
            #需要添加代理的用户验证，注意需要将用户名密码base64编码
            user_password = base64.b64encode(proxy['user_password'])
            request.meta['proxy'] = 'http://' + proxy['ip_port']
            request.headers['Proxy-Authorization'] = 'Basic '+ user_password

        print proxy['ip_port']
