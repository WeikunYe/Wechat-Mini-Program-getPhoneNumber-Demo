# Wechat-Mini-Program-getPhoneNumber-Demo

A demo for Wechat Mini Program getPhoneNumber API with Python Flask

Steps:

1. user presses the getPhoneNumber button
2. wx.login get code, encrypted data, and iv
3. send code encrpyted data and iv to server
4. sever send request to Wechat server with code to get openid and session key
5. use session key, iv, to decrypt encrypted data to get user info (phone number, location .etc)

Very Important:
Make sure the login status has been cleared before login. Otherwise, the session key recieved is not able to decrypt data.
