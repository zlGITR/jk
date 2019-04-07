from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("修改密码模块")
class Test_changepassword:
    @allure.story("修改密码")
    def test_changepassword_success(self):
        path = '/sys/changePwd'
        data = {'token': CommonData.token,'userId':138,'userName':'15935153095','oldPwd':'123456','password':'12345'}
        resp = http.post(path, data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        print('修改成功')
        self.changepassword()
        print('恢复密码')
    def changepassword(self):
        path = '/sys/changePwd'
        data = {'token': CommonData.token,'userId':138,'userName':'15935153095','oldPwd':'12345','password':'123456'}
        resp = http.post(path, data)
        assert resp['code']==200
        print('修改成功')