# encoding: utf-8
# !/usr/bin/env python
from common.conf_basic import ConfBasic
from utils.request_handler import RequestHandler




def login(username=ConfBasic.username, password=ConfBasic.password):
    #path = "/fnode-api/login"
    path ="/datasience/management/login/"
    body = {"username": username, "password": password}
    response = RequestHandler(None, None).post(path=path, body=body)
    guid = response.json()['data']['guid']
    token = response.json()['data']['token']
    return guid,token

class ApiBase:
    guid,token=login()
    http = RequestHandler(guid,token)