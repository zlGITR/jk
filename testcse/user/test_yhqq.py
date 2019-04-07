# from common.commonData import CommonData
# from conftest import http
# class Test_yhqq:
#     def test_zhuce(self):
#             path = '/user/saveOrUpdateUser'
#             data = {
#                     "nickName": "yhlf",
#                     "userName": "15935153264",
#                     "telNo": "",
#                     "email": "",
#                     "address": "",
#                     "roleIds": "2",
#                     "regionId": 1,
#                     "regionLevel": 1
#                       }
#             resp = http.post(path, data)
#             print("注册成功")
#             name=data["nickName"]
#             user=data["userName"]
#             id=self.login(user)
#             self.huoqu(id,name)
#     def login(self,user):
#         url = "/sys/login"
#         data = {}
#         data["userName"] = user
#         data["password"] = "123456"
#         resp = http.post(url, data)
#         print("登陆成功")
#         assert resp['code'] == 200
#         return  resp['object']['userId']
#     def  huoqu(self,id,name):
#         url = "/user/loadUserList"
#         data = {'pageSize': 30,
#                 'pageCurrent':1}
#         resp = http.post(url, data)
#         print("获取成功")
#         assert resp['object']['list'][0]['nickName'] == name
#         assert resp['object']['list'][0]['id']==id
