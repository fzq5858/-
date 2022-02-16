# import json
#
# from common.conf_basic import ConfBasic
# from utils.request_handler import RequestHandler
#
# #path = "/fnode-api/login"
# import requests
#
# from utils.request_handler import RequestHandler
#
# path ="http://hbdev.bonc.tech/datasience/management/login"
# body = {"username": 'fzq', "password": 'fzq'}
# response = requests.post(url=path, headers={'Content-Type': 'application/json;charset=UTF-8'},data=json.dumps(body))
# guid = response.json()['data']['guid']
# token = response.json()['data']['token']
# print(guid,token,ConfBasic.domain)

#
# for i in range(10):
#     tenantName = i
#     print(tenantName)

# import random
#
# x=1
# while x<random.randint(1,1000):
#     x+=1
# print(x)

# a='sssh-hhhoiuy'
# b=a.split('-')[1]
# print(b)
list=[]
a=['1','2','3','4','5']
for i in a:
    list.append(i)
field_str=",".join(list)
print(field_str)

class A:
    def a():
        print('123')

    def b():
        A.a()

A.b()

b=[1,2,3]
c=[4]
c.append(b)
print(c)

a={"1":"2"}
b={"2":"4","3":"4"}
c=dict(a,**b)
print(c)

def Log(prefix,**data):
    print(prefix+'\t'.join(data.values()))
    print(data)
Log('[Notice]',ip='127.0.0.1',port='80',userid='1234')