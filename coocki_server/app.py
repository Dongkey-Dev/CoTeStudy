from flask import Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

import handler_df as hdf
import pandas as pd
import json
import os

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

DF_BOOK = hdf.get_book()

@app.route('/cookie_action/regist_auction', methods=['POST'])
def regist():
    df = DF_BOOK.copy()
    result = request.json
    return result
    
@api.route('/cookie_auction/call_auction')  # url pattern으로 name 설정
class Auction_Register(Resource):
    def post(self):
        df = hdf.get_book()
        request.json.get

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)