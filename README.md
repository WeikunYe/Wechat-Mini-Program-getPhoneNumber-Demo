# Wechat-Mini-Program-getPhoneNumber-Demo

A demo for Wechat Mini Program getPhoneNumber API with Python Flask

Steps:

1. getPhoneNumber
2. The user selects the phone number.
3. Verify with SMS
4. wx.login API to get code, encrypted data, and iv
5. Send code encrpyted data and iv to server
6. Sever send request to Wechat server with code to get openid and session key
7. Use session key, iv, to decrypt encrypted data to get user info (phone number, location .etc)

Very Important:
Make sure the login status has been cleared before login. Otherwise, the session key recieved is outdated and it is not able to decrypt data.
