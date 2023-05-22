# -*- coding: utf-8 -*-
from urllib import parse
import base64
import hashlib
import time
import requests
import json
URL = "https://webapi.xfyun.cn/v1/service/v1/ocr/handwriting"
APPID = '347f4226'
API_KEY = "ca0b732b1ebc17a08b2980109516fd91"
def getHeader(language,location):
    curTime = str(int(time.time()))
    param = "{\"language\":\""+language+"\",\"location\":\""+location+"\"}"
    paramBase64 = base64.b64encode(param.encode('utf-8'))

    m2 = hashlib.md5()
    str1 = API_KEY + curTime + str(paramBase64, 'utf-8')
    m2.update(str1.encode('utf-8'))
    checkSum = m2.hexdigest()
	# 组装http请求头
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header
def getBody(filepath):
    with open(filepath, 'rb') as f:
        imgfile = f.read()
    data = {'image': str(base64.b64encode(imgfile), 'utf-8')}
    return data
def getText(img):
    # 语种设置
    language = "en"
    # 是否返回文本位置信息
    location = "false"
    # 图片上传接口地址
    r = requests.post(URL, headers=getHeader(language, location), data=str(img,'utf-8'))
    result = str(r.content,'utf-8')
    data = json.loads(result)
    content = jsonpath.jsonpath(data,'$..content') # 文件对象   jsonpath语法
    return ' '.join(content)
