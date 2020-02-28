# -*- coding = UTF-8 -*-
from flask import Flask
from flask_restful import Api
from wx_login import WxLogin


app = Flask(__name__)

api = Api(app)

api.add_resource(WxLogin, '/wx_register')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
