import urllib.request
import threading
import time

class AccessTokenManager :
    _instance_Lock = threading.Lock()
    AccessToken = ""
    AccessTime = time.time()
    AccessExpiresIn = 0

    def __new__(cls,*arg,**kwargs):
        with AccessTokenManager._instance_Lock:
            if not hasattr(AccessTokenManager,"_instance"):
                AccessTokenManager._instance = object.__new__(cls)  
        return AccessTokenManager._instance

    def __init__(self,appid,secretid):
        self.AppId = appid
        self.SecretId = secretid
        self.Url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&"

    def getAccessToken(self):
        AccessLeftTime = self.AccessExpiresIn - (time.time() - self.AccessTime)
        if self.AccessToken == None or self.AccessToken == "" or  AccessLeftTime <= 0: 
            self.Url += "appid="
            self.Url += self.AppId
            self.Url += "&secret="
            self.Url += self.SecretId

            resu = urllib.request.urlopen(self.Url)
            data = resu.read().decode()

            self.AccessToken = data['access_token']
            self.AccessExpiresIn = data['expires_in']
            self.AccessTime = time.time()

        return self.AccessToken



