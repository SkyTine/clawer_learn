import json

import time
import requests
from datetime import datetime

url = "http://ics.chinasoftinc.com:30122/insertHealthyRecord.Action"

header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; YAL-AL50 Build/HUAWEIYAL-AL50; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 HuaWei-AnyOffice/1.0.0/com.huawei.welink",
    "Host": "ics.chinasoftinc.com:30122",
    "Connection": "keep-alive",
    "Content-Length": "304",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*"
}

data = {
    "questionContent": {
        "h1001": "非封控区、管控区、防范区范围",
        "h1002": "暂无同住人",
        "h1003": "未到岗，周末正常休假中",
        "h1004": "未被隔离",
        "h1005": "是",
        "h1006": "绿色",
        "h1007": "2022年06月09日",
        "h1008": "阴性",
        "h1009": "已接种第三针"
    },
    "source": 1,
    "lobNumber": "336794"
}

#zaiwindows下打开C盘文件会遇见无权访问的问题
path = ""

if __name__ == '__main__':
    # 参数修改
    if datetime.today().weekday() > 4:  # 0-6:周一到周日 / 周末不上班
        data["questionContent"]["h1003"] = "未到岗，周末正常休假中"
    else:
        data["questionContent"]["h1003"] = "在岗，我司现场"
    # 请求
    data = json.dumps(data)
    res = requests.post(url=url, data=data, headers=header)
    file = path + "/welinkInsertHealthyRecord.log"
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with open(file, mode="a", encoding="utf-8") as log:
        log.write(now + ": " + res.text + "\n")
    log.close()
