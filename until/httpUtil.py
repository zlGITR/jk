import requests
import json
from common.commonData import CommonData
class Httpuntil:
    def __init__(self):
       self.http=requests.session()
       self.headers = {'Content-Type': 'application/json;charset=utf-8'}
    def post(self,path,data):
        host=CommonData.host
        if CommonData.token is not None:
            self.headers['token']=CommonData.token
        json_data=json.dumps(data)
        resp_login = self.http.post(url=host+path,
                         proxies=CommonData.proxies,
                         data=json_data,
                         headers=self.headers)
        assert  resp_login.status_code==200
        resp_dict=json.loads(resp_login.text)
        return resp_dict