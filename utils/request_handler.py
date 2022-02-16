# encoding: utf-8
# !/usr/bin/env python
import json
import os
import random
from pathlib import Path
import requests
from requests_toolbelt import MultipartEncoder
from os.path import dirname

#from config import ConfBasic
#from utils.tools import get_pro_root_path, save_log
from common.conf_basic import ConfBasic


class RequestHandler:

    domain = ConfBasic.domain
    headers = ConfBasic.headers
    # timeout = ConfBasic.timeout
    # log = ConfBasic.log
    # log_flag = ConfBasic.log_flag

    def __init__(self, guid, token):
        self.guid = guid
        self.token = token

        # 处理接口的url中没有guid和token时的场景
        if self.guid is None and self.token is None:
            self.authentication_dict = None
        else:
            self.authentication_dict = {'guid': self.guid, 'token': self.token}

    def get(self, path=None, params=None, headers=headers,  **kwargs)-> requests.Response:
        # 拼接url
        path = self.domain + path

        # 处理请求url中的params和guid与token的组合
        if params is None:
            merge_params = self.authentication_dict
        else:
            merge_params = dict(params, **self.authentication_dict)

        # 发送requests的get请求，返回响应结果对象
        try:
            response = requests.get(url=path, params=merge_params, headers=headers,  **kwargs)

            # 保存日志
            #save_log(response, self.log, self.log_flag)

            return response
        except Exception as e:
            print(e)

    def delete(self, path=None, params=None, body=None, headers=headers,  **kwargs)-> requests.Response:
        # 拼接url
        path = self.domain + path

        # 处理请求url中的params和guid与token的组合
        if params is None:
            merge_params = self.authentication_dict
        else:
            merge_params = dict(params, **self.authentication_dict)

        # 发送requests的delete请求，返回响应结果对象
        try:
            response = requests.delete(url=path, params=merge_params, data=json.dumps(body), headers=headers,  **kwargs)

            # 保存日志
            #save_log(response, self.log, self.log_flag)

            return response
        except Exception as e:
            print(e)

    def post(self, path=None, params=None, headers=headers, body=None, fields_file='srcFile', files=None, stance_type='application/octet-stream',  **kwargs)-> requests.Response:
        # 拼接url
        path = self.domain + path

        # 处理请求url中的params和guid与token的组合
        if params is None:
            merge_params = self.authentication_dict
        else:
            merge_params = dict(params, **self.authentication_dict)

        # body在上传文件的时候需要是None
        # fields_file是上传文件时的key('file', 'srcFile',...)，具体根据实际抓到的请求来传参
        # files是具体的文件名称，文件是需要放在resources下面的
        # stance_type是上传文件对应的协议，如文本类型就是application/octet-stream，等等
        try:
            if files:
                headers = {}
                dataset_file = Path(dirname(dirname(__file__)) + os.sep) / "test" / "case_file" / files
                with open(dataset_file, 'rb') as f:
                    data = f.read()
                multipart_encoder = MultipartEncoder(
                    fields={
                        fields_file: (files.split('/')[-1], data, stance_type)
                    },
                    boundary='----' + str(random.randint(1e28, 1e29 - 1))
                )
                headers['Content-Type'] = multipart_encoder.content_type
                response = requests.post(url=path, params=merge_params, headers=headers, data=multipart_encoder,  **kwargs)
            else:
                response = requests.post(url=path, params=merge_params, headers=headers, data=json.dumps(body),  **kwargs)

            # 保存日志
            #save_log(response, self.log, self.log_flag)

            return response
        except Exception as e:
            print(e)
