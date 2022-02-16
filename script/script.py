# encoding: utf-8
# !/usr/bin/env python
import datetime
import random
from time import sleep

import pytest

from common.login import ApiBase
from common.login import login

class Def():
    #创建子租户
    def create_zuhu(tenantName="省分-山西",tenantAdminLoginId="sx"):
        province_dit = ['省分-黑龙江', '省分-辽宁', '省分-吉林', '省分-河北', '省分-河南', '省分-湖北', '省分-湖南', '省分-山东', '省分-山西', '省分-陕西', '省分-安徽', '省分-浙江', '省分-江苏',
                        '省分-福建', '省分-广东', '省分-海南', '省分-四川', '省分-云南', '省分-贵州', '省分-青海', '省分-甘肃', '省分-江西', '省分-台湾', '省分-内蒙古', '省分-宁夏',
                        '省分-新疆', '省分-西藏', '省分-广西', '省分-北京', '省分-上海', '省分-天津', '省分-重庆', '省分-香港', '省分-澳门']
        login_name = ['hlj', 'ln', 'jl', 'hb', 'hn', 'hubei', 'hunan', 'sd', 'sx', 'sanxi', 'ah', 'zj', 'js',
                        'fj', 'gd', 'hainan', 'sc', 'yn', 'gz', 'qh', 'gs', 'jx', 'tw', 'nmg', 'nx',
                        'xj', 'xz', 'gx', 'bj', 'sh', 'tj', 'cq', 'xg', 'am']
        for i in range(34):
            tenantName=province_dit[i]
            tenantAdminLoginId=login_name[i]

            create_zuhu_body={"tenantName":tenantName,"tenantMemo":tenantName.split('-')[1],"orderId":"","tenantAdminId":"","tenantAdminLoginId":tenantAdminLoginId,"password":"123456","tenantParent":"tenant_system","tenantAdminMobile":"18812341234","tenantAdminEmail":"18812341234@bonc.com.cn"}
            create_zuhu_repose=ApiBase.http.post(path='/datasience/system/tenant/save',body=create_zuhu_body)
            print('创建子租户',create_zuhu_repose.json())
            #print(create_zuhu_body)

    #批量随机登录租户账号
    def random_login_zuhu():
        #随机执行x次
        x=0
        while x<random.randint(1,50):
            login_name = ['hlj', 'ln', 'jl', 'hb', 'hn', 'hb', 'hn', 'sd', 'sx', 'sanxi', 'ah', 'zj', 'js',
                          'fj', 'gd', 'hainan', 'sc', 'yn', 'gz', 'qh', 'gs', 'jx', 'tw', 'nmg', 'nx',
                          'xj', 'xz', 'gx', 'bj', 'sh', 'tj', 'cq', 'xg', 'am']
            username = login_name[random.randint(0, 33)]

            #username登录n次
            n=0
            while n<random.randint(1,50):
                login(username=username,password='123456')
                n+=1
                #sleep(3)
            print(username+'登录了'+str(n)+'次')

            x+=1
        print('执行了 ' + str(x) + '次')

    #创建组织机构
    def create_organization():
        province_dit = ['黑龙江省', '辽宁省', '吉林省', '河北省', '河南省', '湖北省', '湖南省', '山东省', '山西省', '陕西省', '安徽省', '浙江省', '江苏省',
                        '福建省', '广东省', '海南省', '四川省', '云南省', '贵州省', '青海省', '甘肃省', '江西省', '台湾省', '内蒙古自治区', '宁夏回族自治区',
                        '新疆维吾尔自治区', '西藏自治区', '广西壮族自治区', '北京市', '上海市', '天津市', '重庆市', '香港特别行政区', '澳门特别行政区']
        for i in range(5,39):
            name=province_dit[i-5]
            create_organization_body={"orgName":name,"orgCode":i,"orgType":"2","parentId":"","orgMemu":name,"orderId":"4","isPublic":"","orgStatus":""}
            create_organization_response=ApiBase.http.post(path="/datasience/system/org/save",body=create_organization_body)
            print("创建组织机构",create_organization_response.json())

    #新增10个模型效果回收
    def creat_model_operation():
        for i in range(1,11):
            body={"modelName":2,"datasource":2,"eventName":"hdnc活动名称","effectSource":"xgly效果来源"+str(i),"supportPlatform":"zcpt支撑平台","supportScene":"zccj支撑场景","provinceCode":"010","cityCode":"010_001","beginTime":"2021/12/23","endTime":"2021/12/31","targetNum":"99"+str(i),"contactNum":"88"+str(i),"successNum":"77"+str(i),"intentionNum":"66"+str(i),"marketingPolicy":"营销政策"*50,"eventDescription":"活动描述"*125,"modelSuggestion":"模型优化建议bjbj"*20}
            creat_model_operation_respose=ApiBase.http.post(path="/datasience/vbap3/dsc/model/effect/recycle",body=body)
            print("新增模型回收",creat_model_operation_respose.json())
            #print(body)

    # 分享项目：输入项目id、项目名称
    def share_project(originalId="?",assetsName="？"):
        share_body = {"assetsId":"","assetsName":assetsName,"assetsDesc":"123","originalId":originalId,"deleteDataSet":"1",
                      "coverUrl":"data:image/png;base64,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",
                      "assetsType":"PROJECT","shareScope":"1","tagModelList":[],"email":"18812341234@bonc.com.cn","telephone":"18812341234","applyMessage":"cs","contactUser":"fzq","supplier":"3#%#5G","modelSummary":"cs模型概述","advantages":[{"title":"特色优势1","content":"特色优势111"},{"title":"特色优势2","content":"特色优势222"},{"title":"特色优势3","content":"特色优势333"}],"applicationModel":[{"title":"应用场景1","content":"应用场景111","coverUrl":"/imagepool/2021-12-16/8757005239382435273.jpg"},{"title":"应用场景2","content":"应用场景222","coverUrl":"/imagepool/2021-12-16/8757005239382435273.jpg"},{"title":"应用场景3","content":"应用场景333","coverUrl":"/imagepool/2021-12-16/8757005239382435273.jpg"}]}

        response = ApiBase.http.post(path="/datasience/assets/info/share",body=share_body)
        print('分享项目',response.json())
        #print(ApiBase.token)

    #订阅项目:输入商店项目名称
    def apply_project(search_name='?',applyName='fzqdy'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')):
        #搜索项目名称（保证搜索结果唯一），获取assetsid
        search_body={"type":"0","search":search_name,"tagIds":[],"orderBy":"","currPage":1,"pageSize":99}
        search_res=ApiBase.http.post(path="/datasience/assets/homepage/getAssetsCard",body=search_body)
        assetsId=search_res.json()["data"]["assetList"][0]["assetsId"]

        dy_body={"assetsId":assetsId,"mobileNo":"18812341234","email":"18812341234@bonc.com.cn","applyMessage":"cs","applyId":"","assetsType":"PROJECT","applyName":applyName,"contactUser":"fzq","userName":"mxhs"}
        dy_res=ApiBase.http.post(path="/datasience/assets/from/market/apply",body=dy_body)
        print(dy_res.json())
        print("订阅项目",applyName)

    #创建空项目：输入项目名称
    def create_project(projectName='fzq'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')):
        #创建空项目
        create_project_body={"projectName":projectName,"isPublic":"","projectDesc":"项目简介","icon":"","tags":[],"contractor":"承建方","owner":"归属放","creatorPhone":"18812341234","useScene":"3"}
        create_project_response = ApiBase.http.post(path="/datasience/management/project/saveProject",body=create_project_body)
        project_id = create_project_response.json()['data']['project']['id']
        #print('创建空项目', create_project_response.json())
        print(projectName)
        return project_id,projectName

    # 添加notebook算子：输入项目id、拖入画布的数据集id
    def add_notebook(project_id="?", dataset_id='?'):
        # 获取项目内的画板flowid
        get_flow_list_by_projectid_response = ApiBase.http.post(
            path="/datasience/ai-schedule/v2/flow/getFlowlistByProjectid", body={"projectId": project_id})
        flow_id = get_flow_list_by_projectid_response.json()['data']['flows'][0]['flowId']

        # 将数据集拖至画布中,并获取新数据集的ID
        data_mart_to_project_body = {
            "projectId": project_id,
            "dataSetIds": [dataset_id],
            "dataSetType": "flow",
            "projectName": ""
        }
        data_mart_to_project_res = ApiBase.http.post(path="/datasience/vbap3/dsc/dataMartToProject",
                                                     body=data_mart_to_project_body)
        # 获取新数据集的ID
        newDataSetId = data_mart_to_project_res.json()['data']['newDataSetId']

        sleep(2)
        # 调用get_all接口查询内部和外部数据集在画板中的一些信息
        get_all_res = ApiBase.http.get(path="/datasience/ai-schedule/v2/flow/getAll",
                                       params={"flowId": flow_id, "projectId": project_id})
        # 添加算子传参body里的node_id、node_type_id
        node_id = ""
        node_type_id = ""
        # node_Id=''
        for item in get_all_res.json()["data"]["nodes"]:
            if item["exploreDatasetId"] == newDataSetId:
                node_id = item["nodeId"]
                nodeName = item["nodeName"]
                node_type_id = item["nodeTypeId"]
                break

            # #空值处理获取表字段的url拼接
            # if item["nodeTypeId"] == newDataSetId:
            #     node_Id=item["nodeId"]
            #     print(node_Id)
            #     break

        # 添加notebook算子
        # 保存数据集,获取notebook传参的nodeId  --"nodeTypeId": "24"
        output_node_id = \
        ApiBase.http.post(path="/datasience/ai-schedule/v2/data/saveResource", params={"projectId": project_id},
                          body={"type": 0, "nodeTypeId": "24",
                                "resource": {"projectId": project_id,
                                             "dataSetName": 'notebook' + datetime.datetime.now().strftime(
                                                 '%Y%m%d%H%M%S'), "dataConnectionId": "",
                                             "schema": ""}
                                }).json()["data"]["nodeInfo"]["nodeId"]

        params = {"projectId": project_id}
        add_notebook_body = {"flowId": flow_id,
                             "operator": {"nodeId": "", "nodeType": 1, "nodeTypeId": "24"},
                             "out": [{"nodeId": output_node_id}],
                             "in": [{"nodeId": node_id}],
                             "params": None,
                             "myparams": [],
                             "seniorParams": {"imageId": 1, "resourceTemplateId": 1, "kernalId": 1, "example": 1}}
        add_notebook_reponse = ApiBase.http.post(path="/datasience/ai-schedule/v2/operator/saveParamsNew",
                                                 params=params, body=add_notebook_body)
        # print(add_notebook_body )
        print('添加notebook算子', add_notebook_reponse.json())

        # 添加空值处理算子
        # 获取数据集全部列字段拼接，用来传参
        # print('fgh',node_id,'jg')
        list = []
        x = ApiBase.http.get(path="/datasience/ai-schedule/v2/operator/2/" + node_id + "/getParamsNew")
        for i in x.json()['data']['params']['datasetColumns']:
            list.append(i['name'])
        field_str = ",".join(list)
        # print('field_str:',field_str)

        add_kzcl_body = {"flowId": flow_id,
                         "operator": {"nodeId": "", "nodeType": 1, "nodeTypeId": "2"},
                         "out": [{"nodeName": '空值处理' + datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                                  "nodeType": 0, "nodeId": ""}],
                         "in": [{"nodeId": node_id}],
                         "params": [{"paramId": None, "paramName": "inputpath",
                                     "paramValue": node_type_id, "paramTypeId": 90, "isInOrOut": True},
                                    {"paramId": None, "paramName": "output", "paramValue": None,
                                     "paramTypeId": 91,
                                     "isInOrOut": True}
                                    ],
                         "myparams": [{
                             "nullProcessColumnData": [
                                 {"field": field_str,
                                  "replaceValue": "1",
                                  "replaceWay": "value"}
                             ]}],
                         "seniorParams": {"resourceTemplateId": 7, "sparkExecutorId": 60}}
        # 添加空值处理算save_params_new_re子，获取返回的算子ID:nodeId
        add_kzcl_res = ApiBase.http.post(path="/datasience/ai-schedule/v2/operator/saveParamsNew",
                                         params={"projectId": project_id}, body=add_kzcl_body)
        # assert save_params_new_res.json()['code'] == 1000
        # save_params_new_nodeId = save_params_new_res.json()["data"]["nodeId"]
        print('添加空值处理算子', add_kzcl_res.json())

        # 添加比例拆分算子
        # 保存输出数据集
        first_node_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        output_node_name = first_node_name + '比例拆分output'
        cutoffs_node_name = first_node_name + '比例拆分cutoffs'
        a = ApiBase.http.post(path="/datasience/ai-schedule/v2/data/saveResource", params={"projectId": project_id},
                              body={
                                  "type": 0,
                                  "nodeTypeId": 13,
                                  "resource": {
                                      "projectId": project_id,
                                      "dataSetName": output_node_name,
                                      "dataConnectionId": "",
                                      "schema": ""
                                  }
                              })
        output_node_id, output_paramValue = a.json()['data']['nodeInfo']['nodeId'], a.json()['data']['nodeInfo'][
            'nodeTypeId']
        b = ApiBase.http.post(path="/datasience/ai-schedule/v2/data/saveResource", params={"projectId": project_id},
                              body={
                                  "type": 0,
                                  "nodeTypeId": 13,
                                  "resource": {
                                      "projectId": project_id,
                                      "dataSetName": cutoffs_node_name,
                                      "dataConnectionId": "",
                                      "schema": ""
                                  }
                              })
        cutoffs_node_id, cutoffs_paramValue = b.json()['data']['nodeInfo']['nodeId'], b.json()['data']['nodeInfo'][
            'nodeTypeId']

        # 添加比例拆分算子，获取返回的算子ID:nodeId
        add_blcf_body = {"flowId": flow_id,
                         "operator": {"nodeId": "", "nodeType": 1, "nodeTypeId": "13"},
                         "out": [{"nodeId": output_node_id},
                                 {"nodeId": cutoffs_node_id}
                                 ],
                         "in": [{"nodeId": node_id}],
                         "params": [{"paramId": None, "paramValue": node_type_id, "isInOrOut": True}],
                         "myparams": [
                             {"fromDataset":
                                  {"datasetId": node_type_id,
                                   "nodeId": node_id,
                                   "datasetName": first_node_name,
                                   "fieldsInfo": [
                                       {"displayName": "ZERO列", "fieldType": "MEASURE", "fieldId": "c_29345"},
                                       {"displayName": "MEAN列", "fieldType": "MEASURE", "fieldId": "c_34285"},
                                       {"displayName": "STD", "fieldType": "MEASURE", "fieldId": "c_STD"},
                                       {"displayName": "CV", "fieldType": "MEASURE", "fieldId": "c_CV"},
                                       {"displayName": "INC列", "fieldType": "MEASURE", "fieldId": "c_53317"},
                                       {"displayName": "OPP", "fieldType": "MEASURE", "fieldId": "c_OPP"},
                                       {"displayName": "CS", "fieldType": "MEASURE", "fieldId": "c_CS"},
                                       {"displayName": "IS_OUTNET", "fieldType": "MEASURE",
                                        "fieldId": "c_IS_OUTNET"}
                                   ]
                                   },
                              "outputDataset": [
                                  {"datasetId": output_paramValue,
                                   "nodeId": output_node_id,
                                   "datasetName": output_node_name, "condition": None, "percentage": 50},
                                  {"datasetId": cutoffs_paramValue,
                                   "nodeId": cutoffs_node_id,
                                   "datasetName": cutoffs_node_name, "condition": None, "percentage": 50}
                              ]
                              }],
                         "seniorParams":
                             {"resourceTemplateId": 7, "sparkExecutorId": 60}}
        add_blcf_res = ApiBase.http.post(path="/datasience/ai-schedule/v2/operator/saveParamsNew",
                                         params={"projectId": project_id}, body=add_blcf_body)
        # assert save_params_new_res.json()['code'] == 1000
        # save_params_new_nodeId = save_params_new_res.json()["data"]["nodeId"]
        print("添加比例拆分算子", add_blcf_res.json())

        # 添加抽样算子
        add_cy_body = {"flowId": flow_id,
                       "operator": {
                           "nodeId": "",
                           "nodeType": 1,
                           "nodeTypeId": "11"
                       },
                       "out": [
                           {"nodeName": '抽样' + datetime.datetime.now().strftime('%Y%m%d%H%M%S'), "nodeType": 0,
                            "nodeId": ""}
                       ],
                       "in": [
                           {"nodeId": node_id}
                       ],
                       "params": [
                           {"paramId": "", "paramName": "inputpath", "paramValue": node_type_id,
                            "paramTypeId": 1207, "isInOrOut": "true"},
                           {"paramName": "output", "paramTypeId": 1208, "isInOrOut": "true"},
                           {"paramId": None, "paramName": "withreplacement", "paramValue": "True"},
                           {"paramId": None, "paramName": "fraction", "paramValue": "0.2"},
                           {"paramId": None, "paramName": "method", "paramValue": "sample"},
                           {"paramId": None, "paramName": "col"}
                       ],
                       "myparams": [],
                       "seniorParams": {
                           "resourceTemplateId": 7,
                           "sparkExecutorId": 60}
                       }
        add_cy_res = ApiBase.http.post(path="/datasience/ai-schedule/v2/operator/saveParamsNew",
                                       params={"projectId": project_id}, body=add_cy_body)
        print('添加抽样算子', add_cy_res.json())

        # 添加pyspark算子
        output_node_id = \
            ApiBase.http.post(path="/datasience/ai-schedule/v2/data/saveResource", params={"projectId": project_id},
                              body={"type": 0, "nodeTypeId": "241",
                                    "resource": {"projectId": project_id,
                                                 "dataSetName": 'pyspark' + datetime.datetime.now().strftime(
                                                     '%Y%m%d%H%M%S'), "dataConnectionId": "",
                                                 "schema": ""}
                                    }).json()["data"]["nodeInfo"]["nodeId"]
        add_pyspark_body = {
            "flowId": flow_id,
            "operator": {
                "nodeId": "",
                "nodeType": 1,
                "nodeTypeId": "241"
            },
            "out": [{
                "nodeId": output_node_id
            }],
            "in": [{
                "nodeId": node_id
            }],
            "params": None,
            "myparams": [],
            "seniorParams": {
                "imageId": 1,
                "resourceTemplateId": 7,
                "kernalId": 1,
                "example": 1,
                "sparkExecutorId": 60
            }
        }
        add_pyspark_res = ApiBase.http.post(path="/datasience/ai-schedule/v2/operator/saveParamsNew",
                                            params={"projectId": project_id}, body=add_pyspark_body)
        print('添加pyspark算子', add_pyspark_res.json())

        # 添加python算子
        output_node_id = \
            ApiBase.http.post(path="/datasience/ai-schedule/v2/data/saveResource", params={"projectId": project_id},
                              body={"type": 0, "nodeTypeId": "5",
                                    "resource": {"projectId": project_id,
                                                 "dataSetName": 'python' + datetime.datetime.now().strftime(
                                                     '%Y%m%d%H%M%S'), "dataConnectionId": "",
                                                 "schema": ""}
                                    }).json()["data"]["nodeInfo"]["nodeId"]
        add_python_body = {
            "flowId": flow_id,
            "operator": {
                "nodeId": "",
                "nodeType": 1,
                "nodeTypeId": "5"
            },
            "out": [{
                "nodeId": output_node_id
            }],
            "in": [{
                "nodeId": node_id
            }],
            "params": None,
            "myparams": [],
            "seniorParams": {
                "imageId": 1,
                "resourceTemplateId": 1,
                "kernalId": 1,
                "example": 1
            }
        }
        add_python_res = ApiBase.http.post(path="/datasience/ai-schedule/v2/operator/saveParamsNew",
                                           params={"projectId": project_id}, body=add_python_body)
        print('添加python算子', add_python_res.json())

        # 添加sql算子
        add_sql_body = {
            "flowId": flow_id,
            "operator": {
                "nodeId": "",
                "nodeType": 1,
                "nodeTypeId": "6"
            },
            "out": [{
                "nodeName": 'sql' + datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                "nodeType": 0,
                "nodeId": ""
            }],
            "in": [{
                "nodeId": node_id
            }],
            "params": [{
                "paramId": None,
                "paramValue": None,
                "isInOrOut": True
            }],
            "myparams": [],
            "seniorParams": {
                "imageId": 1,
                "resourceTemplateId": 7,
                "kernalId": 1,
                # "example": 1,
                "sparkExecutorId": 60
            }
        }
        add_sql_res = ApiBase.http.post(path="/datasience/ai-schedule/v2/operator/saveParamsNew",
                                        params={"projectId": project_id}, body=add_sql_body)
        print('添加sql算子', add_sql_res.json())

    #运行所有算子节点
    def run_all_nodeMultiOpera(project_id):
        # 获取项目内的画板flowid
        get_flow_list_by_projectid_response = ApiBase.http.post(
            path="/datasience/ai-schedule/v2/flow/getFlowlistByProjectid", body={"projectId": project_id})
        flow_id = get_flow_list_by_projectid_response.json()['data']['flows'][0]['flowId']

        # 调用get_all接口查询内部和外部数据集在画板中的一些信息
        get_all_res = ApiBase.http.get(path="/datasience/ai-schedule/v2/flow/getAll",
                                       params={"flowId": flow_id, "projectId": project_id})
        # 添加算子传参body里的node_id、node_type_id
        node_id = ""
        node_id_list=[]
        for item in get_all_res.json()["data"]["nodes"]:
            node_id_list.append(item["nodeId"])
            #print(node_id_list)
            try:
                for i in item['children']:
                    node_id_list.append(i)
                    #print(node_id_list)
            except:
                pass
                #print("item['children']:error")

        for i in node_id_list:
            try:
                body={"operaType":"run","nodeIds":[i]}
                res=ApiBase.http.post(path='/datasience/ai-schedule/v2/multiOpera/nodeMultiOpera',params={"projectId":project_id},body=body)
                jobId=res.json()['data']['jobId']
                #print("运行算子节点jobId：",jobId)
            except:pass
                #print('运行算子节点error')

    #创建项目+添加算子+分享
    def c_p_s(dataset_id='vbap1882d37d6540055d1d021567'):
        #创建空项目
        project_id,projectName=Def.create_project()
        # 重复添加算子
        for i in range(5):
            #添加算子
            Def.add_notebook(project_id=project_id,dataset_id=dataset_id)
        #运行所有算子节点
        Def.run_all_nodeMultiOpera(project_id=project_id)
        #分享项目
        #Def.share_project(project_id,assetsName=projectName)










##########################调用方法############################################
#Def.share_project(originalId="6ec9b71cf801455cb260cb746fcc5d5d",assetsName="fzq30")
#Def.create_project()
#Def.add_notebook(project_id="6ec9b71cf801455cb260cb746fcc5d5d",dataset_id='vbap16ea4f056a07ff728c25897f')
#Def.create_zuhu()
Def.random_login_zuhu()
#Def.create_organization()
#Def.creat_model_operation()

#Def.add_notebook(project_id="e88896e4719d49c8a6e48bcdea0c451e",dataset_id='vbap1882d37d6540055d1d021567')

#Def.c_p_s(dataset_id="vbap6b6add9bc47030424fb1c95d")

#Def.apply_project(search_name='fzq算子123')