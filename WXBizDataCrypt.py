import base64
import json
from Crypto.Cipher import AES
#need to install Crypto.Cipher
#pip install pycrypto
class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey
    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        #important:
        #json.loads only take string
        #unpad function return a bytes variable
        #need to decode('utf-8')
        #if has error: UnicodeDecodeError: 'utf-8' codec can't decode byte
        #this means decrypting failed
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)).decode('utf-8'))
        print(decrypted)
        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')
        return decrypted
    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
