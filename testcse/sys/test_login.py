import pytest
from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("登陆模块")
class Test_Login:
    @allure.story('登陆成功')
    def test_login_success(self):
        url = "/sys/login"
        data = {'userName': CommonData.mobile,
                'password': CommonData.password
                }
        resp = http.post(url, data)
        assert resp['code'] == 200
        assert resp['msg'] == "操作成功"
        assert resp['object']['userId'] == 138
        print("登陆成功，断言成功")

    @allure.story('登陆失败')
    def test_login_fail(self):
        url = "/sys/login"
        data = {'userName': "",
                'password': CommonData.password
                }
        resp = http.post(url, data)
        assert resp['code'] == 3010
        assert resp['msg'] == "此账户禁止登陆"

    @allure.story('登陆失败1')
    def test_login_fail1(self):
        url = "/sys/login"
        data = {'userName': CommonData.mobile,
                'password': ""
                }
        resp = http.post(url, data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户名或密码错误"
