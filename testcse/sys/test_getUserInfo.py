import pytest
from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("获取用户模块")
class Test_getuser:
     @allure.story("获取用户成功")
     def test_getuserinfo_success(self):
        path='/sys/getUserInfo'
        data={'token':CommonData.token}
        resp= http.post(path,data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        print("获取用户成功")

     @allure.story("获取用户成功")
     def test_getuserinfo_fail(self):
         path = '/sys/getUserInfo'
         data = {'token': ""}
         resp = http.post(path, data)
         assert resp['code'] == 200
         assert resp['msg'] == '操作失败'
         print("获取用户成功")