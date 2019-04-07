import pytest
import requests
import json
from until.httpUtil import Httpuntil
from common.commonData import CommonData
http = Httpuntil()
@pytest.fixture(scope='session',autouse=True)
def login():
    url="/sys/login"
    data={}
    data["userName"]=CommonData.mobile
    data["password"] = CommonData.password
    resp=http.post(url,data)
    CommonData.token=resp["object"]["token"]
    assert resp['code'] == 200
    print("登陆成功")
    yield
    url = "/sys/logout"
    data = {'token': CommonData.token}
    resp = http.post(url, data)
    assert resp['code'] == 200
    print("退出成功")