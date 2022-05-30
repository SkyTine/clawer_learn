# -*- coding: utf8 -*-
import time

import io
import requests
import json

url = 'https://app.xiaoyuan.ccb.com/channelManage/outbreak/addOutbreak'

header = {
    "Host": "app.xiaoyuan.ccb.com",
    "Connection": "keep-alive",
    "Content-Length": "1260",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; YAL-AL50 Build/HUAWEIYAL-AL50; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36jianronghuixue/1.3.0",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://app.xiaoyuan.ccb.com",
    "X-Requested-With": "com.ccb.xiangdaxiaoyuan",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://app.xiaoyuan.ccb.com/LHECRESM/DZK/index2022052702.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en-US;q=0.7,en;q=0.6",
    "Cookie": "Hm_lpvt_bf7b9e35db490d77feb7724936d9c8e6=1582080835; IN012=12001|XnP26; IN031=31002|YUp14; tsgcx=e755cc70-4c01-4aff-a53c-aa490cec7858; IN011=11001|Yg46w; Hm_lvt_5761b93726e2d73c5433fac2d362d57c=1645696103; Hm_lpvt_5761b93726e2d73c5433fac2d362d57c=1645696103; _ga=GA1.2.2088659826.1645696103; sid=b97795f6-583a-41de-aa64-19f68ab11892; tgw_l7_route=608417dba25267713d0f2b720788c555; IN008=8002|YpQo8; IN001=1001|YpQo/; IN010=10002|YpQo/"
}

data = {
    "stuClass": "9999",
    "schoolId": "10530",
    "schoolName": "湘潭大学",
    "stId": "201905556806",
    "userId": "A3231003158096364061085808",
    "stName": "向亚欣",
    "locationAddr": "湖南省湘潭市雨湖区博学路",
    "id": "E01584FE11B9DBC8E0539349FD0A0D31",
    "departments": "302e63bf3d6840a981608c411cecfe34",
    "isContact": "N",
    "isFever": "0",
    "isWuhan": "N",
    "nowArea": "湖南省湘潭市雨湖区",
    "familyaddress": "湘潭大学琴湖18栋",
    "familyStatus": "0",
    "diagnosisTreatment": "",
    "nowStatus": "0",
    "healthStatus": "3",
    "isLevel": "N",
    "isbackLive": "N",
    "trafficTool": "",
    "backTrafficTool": "",
    "levelDate": "",
    "backtime": "",
    "arriveAddr": "",
    "trafficNo": "",
    "backTrafficNo": "",
    "professional": "9D7B8587B2C74DA8E0539349FD0A7824",
    "personType": "",
    "personCategory": "null",
    "temperature": 36.7,
    "remarks": "无",
    "timeToLeaveHuBei": "",
    "dateOfDisengagement": "",
    "otherSymptoms": "",
    "nowStatusStartTime": "",
    "familyStatusStartTime": "",
    "feverStartTime": "",
    "coughStartTime": "",
    "fatigueStartTime": "",
    "diarrheaStartTime": "",
    "coldStartTime": "",
    "headacheStartTime": "",
    "noseStartTime": "",
    "runnyStartTime": "",
    "throatStartTime": "",
    "conjunctivaStartTime": "",
    "isAppearDiagnosis": "N",
    "isVaccinate": "1",
    "vaccineType": "2",
    "injectTimes": "2",
    "otherDesc": "null",
    "isContactWithDiagnosis": "N",
    "isInSchool": "",
    "stMobile": "18674420953"
}

path = ""

if __name__ == '__main__':
    data = json.dumps(data)
    res = requests.post(url=url, data=data, headers=header)
    file = path + "/outbreak.log"
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with io.open(file, mode="a", encoding="utf-8") as log:
        log.write(now + ": " + res.text + "\n")
    log.close()
