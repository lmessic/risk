# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:00:17 2021

@author: jlche
"""


# coding=utf-8
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import urllib
import numpy as np
import pandas as pd
 
app = Flask(__name__)
CORS(app, supports_credentials=True)
 
 
@app.route("/quotaCal", methods=["GET", "POST"])
def quotaCal():
    args = request.get_json()
    
    para = pd.read_excel('风险限额系数需求.xlsx',sheet_name='Sheet2')
    para1,para2 = para.loc[(para['工作年限']==args['work_year']) & 
                             (para['性别']==args['gender']) & 
                             (para['省份']==args['region']) & 
                             (para['学历']==args['edu']) & 
                             (para['行业门类']==args['industry']),['para1','para2']].values[0]
    
    income_total = args['monthincome']*12*((1+para1+0.04)+(1+para1+0.04)**2+(1+para1+0.04)**3)
    promote = para2
    house = args['house'] * 0.02 * 3
    asset = args['asset'] * ((1+0.05)**3)
    
    final_quota_lower,final_quota_upper = int((income_total+promote+house+asset)*0.8), int((income_total+promote+house+asset)*1.2)
 
    info = {}
    info['lower'] = int(final_quota_lower/100)*100
    info['upper'] = int(final_quota_upper/100)*100

    return jsonify(info)
 
 
if __name__ == "__main__":
    app.config["JSON_AS_ASCII"] = False
    app.run(host="127.0.0.1", port=8000)