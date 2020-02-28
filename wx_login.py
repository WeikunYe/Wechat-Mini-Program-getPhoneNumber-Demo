from flask_restful import Resource, reqparse, request
from WXBizDataCrypt import WXBizDataCrypt
import requests

class WxLogin(Resource):

    appID = "your app id"
    AppSecret = "your app serect"
    url_code = "https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={appsecret}&js_code={code}&grant_type=authorization_code"
    url_retoken = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appid={appid}&grant_type=refresh_token&refresh_token={refresh_token}"
    url_info = "https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}&lang=zh_CN"
    openIdUrl = "https://api.weixin.qq.com/sns/jscode2session?"

    def get(self):
        #get code from request
        code = request.args.get('code')
        #get iv from request
        iv = request.args.get('iv')
        #get encrypted data from request
        encryptedData = request.args.get('encryptedData')
        #printing..
        print(code)
        print(iv)
        print(encryptedData)
        #request parameter
        param = {
            'js_code': code,
            'appid': WxLogin.appID,
            'secret': WxLogin.AppSecret,
            'grant_type': 'authorization_code',
        }
        #make request to wechat server
        resp = requests.get(WxLogin.openIdUrl, params=param)
        #make responds to json
        jsonfied_resp = resp.json()
        #printing...
        print(str(jsonfied_resp))
        #get session key
        session_key = jsonfied_resp.get("session_key")
        #initial WXBizDataCrypt instance with app ID and session key
        pc = WXBizDataCrypt(WxLogin.appID, session_key)
        #decrypt data with iv
        result = pc.decrypt(encryptedData, iv)
        #printing
        print(result)
        #return the data you need
        return {'purePhoneNumber': result['purePhoneNumber'], 'countryCode': result['countryCode']}, 201